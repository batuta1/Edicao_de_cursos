"""Testes do controlador (sem janela) e da janela montada num `Tk` escondido.

    uv run python -m unittest discover -s scripts/automacao/testes -t scripts
"""
import tkinter as tk
import unittest
from pathlib import Path
from tkinter import messagebox, ttk
from unittest import mock

from automacao.atualizar import ErroDeEtapa
from automacao.interface import controlador, tela


class ControladorSemJanela(unittest.TestCase):
    """Regras da janela que não precisam de widgets."""
    def setUp(self):
        """Prepara o cenário de cada teste."""
        self.ctl = controlador.Controlador()

    def test_sem_cursos_extrator_e_autores_ficam_indisponiveis(self):
        """Sem a pasta Cursos/, extrator e autores ficam indisponíveis com o motivo escrito."""
        with mock.patch.object(controlador.caminhos, "CURSOS", Path("/nao/existe")):
            m = self.ctl.motivos(["checklist", "extrator", "autores"])
        self.assertIsNone(m["checklist"])
        self.assertIn("Cursos/", m["extrator"])
        self.assertIn("Cursos/", m["autores"])

    def test_notion_sem_token_tem_motivo(self):
        """Sem NOTION_TOKEN, a etapa Notion fica indisponível e o motivo cita o token."""
        with mock.patch.dict(controlador.os.environ, {}, clear=False) as env:
            env.pop("NOTION_TOKEN", None)
            with mock.patch.object(controlador.buscar, "csv_atual", return_value=Path("x.csv")):
                self.assertIn("NOTION_TOKEN", self.ctl.motivos([])["notion"])

    def test_aplicar_exige_ensaio_da_mesma_selecao(self):
        """Aplicar só vale depois de um ensaio da mesma seleção; mudar a seleção invalida o ensaio."""
        self.assertFalse(self.ctl.pode_aplicar(["notion"]))
        with self.assertRaises(ErroDeEtapa):
            self.ctl.rodar(["notion"], ensaio=False, commit=False)
        self.ctl._ensaio = self.ctl._chave(["notion"])
        self.assertTrue(self.ctl.pode_aplicar(["notion"]))
        self.assertFalse(self.ctl.pode_aplicar(["notion", "checklist"]))     # outra seleção: o ensaio não vale
        self.ctl.esquecer_ensaio()
        self.assertFalse(self.ctl.pode_aplicar(["notion"]))

    def test_sem_etapa_marcada_da_erro(self):
        """Rodar sem nenhuma etapa marcada dá erro claro."""
        with self.assertRaises(ErroDeEtapa):
            self.ctl.rodar([], ensaio=True, commit=False)

    def test_linhas_da_tabela_juntam_modelo_e_resultado(self):
        """A tabela junta o que seria enviado (modelo) com o resultado do Notion, e conta os que mudariam."""
        self.ctl.itens = [{"nome": "A", "status": "Em produção", "progresso": 0.6, "responsavel": "João"}]
        self.ctl.resultados = [{"nome": "A", "resultado": "atualizado", "detalhe": ""}, {"nome": "B", "resultado": "não achou no Notion", "detalhe": ""}]
        self.assertEqual(self.ctl.linhas_da_tabela()[0], ("A", "Em produção", "60%", "João", "atualizado"))
        self.assertEqual(self.ctl.quantos_mudariam(), 1)


class JanelaEscondida(unittest.TestCase):
    """A janela montada num Tk escondido."""
    def setUp(self):
        """Prepara o cenário de cada teste."""
        try:
            self.raiz = tk.Tk()
        except tk.TclError:
            self.skipTest("sem ambiente gráfico")
        self.raiz.withdraw()
        self.ctl = controlador.Controlador()
        with mock.patch.object(controlador.caminhos, "CURSOS", Path("/nao/existe")):
            tela.montar(self.raiz, tk, ttk, messagebox, self.ctl)
            self.raiz.update()

    def tearDown(self):
        """Fecha a janela escondida depois de cada teste."""
        self.raiz.destroy()

    def test_duas_abas_e_etapas_indisponiveis_com_motivo(self):
        """A janela tem duas abas e mostra o motivo das etapas indisponíveis."""
        self.assertEqual(len(self.raiz.abas.tabs()), 2)
        self.assertEqual(self.raiz.caixas["extrator"].instate(["disabled"]), True)
        self.assertIn("indisponível", self.raiz.avisos["extrator"].cget("text"))

    def test_aplicar_comeca_bloqueado_e_a_area_de_texto_e_somente_leitura(self):
        """O botão Aplicar começa bloqueado e a área do relatório é somente leitura."""
        self.assertEqual(str(self.raiz.botoes["Aplicar"].cget("state")), "disabled")
        self.assertEqual(str(self.raiz.relatorio_texto.cget("state")), "disabled")


if __name__ == "__main__":
    unittest.main()
