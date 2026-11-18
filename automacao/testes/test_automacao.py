"""uv run python -m unittest discover -s automacao/testes -t ."""
import csv
import tempfile
import unittest
from pathlib import Path

import openpyxl

from automacao.autores import casar
from automacao.checklist import buscar, leitura, xlsx_para_csv
from automacao.notion import api, modelo
from automacao.texto import slug


class Versao(unittest.TestCase):
    def test_maior_versao(self):
        nomes = ["checklist-producao-de-cursos-60-dias-v0-3.xlsx", "checklist-producao-de-cursos-60-dias-v0-10.xlsx",
                 "checklist-producao-de-cursos-60-dias-v0-4.xlsx", "outro.xlsx"]
        self.assertEqual(buscar.escolher_mais_recente(nomes), "checklist-producao-de-cursos-60-dias-v0-10.xlsx")
        self.assertIsNone(buscar.escolher_mais_recente(["x.xlsx"]))


class Conversor(unittest.TestCase):
    def test_virgula_quebra_acento_numero(self):
        with tempfile.TemporaryDirectory() as t:
            x = Path(t) / "a.xlsx"
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = xlsx_para_csv.ABA
            ws.append(["Curso", "Obs", "Nº"])
            ws.append(["MCP - Essentials", "um, dois\nlinha 2 ação", 97.0])
            ws.append([None, None, None])
            wb.save(x)
            saida = xlsx_para_csv.converter(x, saida=lambda *_: None)
            with saida.open(encoding="utf-8") as f:
                linhas = list(csv.reader(f))
        self.assertEqual(linhas, [["Curso", "Obs", "Nº"], ["MCP - Essentials", "um; dois linha 2 ação", "97"]])


class Regras(unittest.TestCase):
    def linha(self, **kw):
        base = {"Curso": "X", "Meta até 12 dez": "", "João": "", "Marina": "", "Responsável": "", "E1–2 Ementa": "", "E3 P": "", "E4 R": "",
                "E5 R": "", "E6 T": ""}
        base.update(kw)
        return base

    def test_autor(self):
        self.assertEqual(leitura.autor_da_linha(self.linha(Responsável="Marina Moreno"))[0], "Marina")
        self.assertEqual(leitura.autor_da_linha(self.linha(**{"João": "x"}))[0], "João")
        self.assertEqual(leitura.autor_da_linha(self.linha(Marina="x"))[0], "Marina")
        self.assertIsNone(leitura.autor_da_linha(self.linha(**{"João": "x", "Marina": "x"}))[0])
        self.assertIsNone(leitura.autor_da_linha(self.linha())[0])

    def test_status_progresso(self):
        self.assertEqual(leitura.situacao(self.linha()), {"status": "Aguardando", "progresso": 0.0})
        s = leitura.situacao(self.linha(**{"E1–2 Ementa": "x", "E3 P": "x", "E4 R": "x"}))
        self.assertEqual((s["status"], round(s["progresso"], 2)), ("Em produção", 0.6))
        todas = {"E1–2 Ementa": "x", "E3 P": "x", "E4 R": "x", "E5 R": "x", "E6 T": "x"}
        self.assertEqual(leitura.situacao(self.linha(**todas))["status"], "Concluído")
        self.assertEqual(leitura.situacao(self.linha(**{"Meta até 12 dez": "publicado"})), {"status": "Aguardando", "progresso": 0.0})   # a meta não é o estado


class Casamento(unittest.TestCase):
    def test_slug_titulo_e_ambiguo(self):
        reg = {"cursos": [
            {"empresa": "iaclube", "curso": "mcp-essentials", "versao": "v7", "ficha": None},
            {"empresa": "OpenAI", "curso": "chatgpt-word-essentials", "versao": "v1", "ficha": {"curso": {"titulo": "ChatGPT + Word - Essentials"}}},
            {"empresa": "A", "curso": "dupla", "versao": "v1", "ficha": None},
            {"empresa": "B", "curso": "dupla", "versao": "v1", "ficha": None}]}
        c, amb, sem, sobras = casar.casar(["MCP - Essentials", "ChatGPT + Word - Essentials", "ChatGPT Doc - Essentials", "dupla", "Curso Novo"], casar.indice(reg))
        self.assertEqual(c["MCP - Essentials"]["curso"], "mcp-essentials")
        self.assertIn("dupla", amb)
        self.assertEqual(c["ChatGPT + Word - Essentials"]["curso"], "chatgpt-word-essentials")
        self.assertEqual(sem, ["ChatGPT Doc - Essentials", "Curso Novo"])   # só casa exato; não chuta
        self.assertEqual(slug("Ação Ótima"), "acao-otima")


class NotionPayload(unittest.TestCase):
    def test_numero_percentual_e_status(self):
        self.assertEqual(api.carga("progresso", "number", {"number": {"format": "percent"}}, 0.6)[1], {"number": 0.6})
        self.assertEqual(api.carga("progresso", "number", {"number": {"format": "number"}}, 0.6)[1], {"number": 60})
        self.assertEqual(api.carga("status", "status", {}, "Concluído")[1], {"status": {"name": "Concluído"}})
        self.assertEqual(api.valor_atual({"type": "select", "select": {"name": "João"}}), "João")

    def test_mapear_colunas(self):
        props = {"Nome do curso": {"type": "title"}, "Status": {"type": "status"}, "Responsável": {"type": "select"},
                 "Progresso": {"type": "number", "number": {"format": "percent"}}}
        self.assertEqual(api.mapear_colunas(props)["progresso"][1], "number")
        with self.assertRaises(api.ErroNotion):
            api.mapear_colunas({"Nome do curso": {"type": "title"}})

    def test_modelo(self):
        itens = modelo.montar([{"Curso": "A", "João": "x", "E1–2": "x", "E3": ""}, {"Curso": ""}])
        self.assertEqual([(i["nome"], i["status"], i["responsavel"]) for i in itens], [("A", "Em produção", "João")])


if __name__ == "__main__":
    unittest.main()
