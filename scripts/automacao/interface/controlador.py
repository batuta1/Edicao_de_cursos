"""O que a janela da automação faz, sem nenhum widget (testável sem abrir janela).

A janela só coordena entradas, ações e resultados; toda regra mora aqui ou em `automacao.atualizar`.
Fluxo seguro: `ensaio()` mostra o que mudaria; `aplicar()` só roda depois de um ensaio da mesma seleção.
"""
import hashlib
import os

from .. import ambiente, caminhos
from ..atualizar import ETAPAS, ErroDeEtapa, executar
from ..checklist import buscar, leitura
from ..notion import api, modelo, sincronizar

ROTULOS = {"checklist": "Checklist (baixar planilha da joao e gerar o csv)",
           "extrator": "Extrator (atualizar o registro de cursos)",
           "autores": "Autores (preencher autor.json)",
           "notion": "Notion (Status, Responsável e Progresso)"}


class Controlador:
    """Estado da sessão: qual ensaio já foi feito e o que ele mostrou."""

    def __init__(self):
        ambiente.carregar()
        self._ensaio = None          # chave do último ensaio concluído (ver `_chave`)
        self.itens = []              # modelo (curso, status, progresso, responsável) do último ensaio/aplicação do Notion
        self.resultados = []         # resultado por curso devolvido pelo Notion

    # ---------------------------------------------------------------- ambiente
    def motivos(self, selecionadas=()):
        """{etapa: motivo por escrito de a etapa não poder rodar, ou None se pode}. `selecionadas` ajusta o motivo (ex.: o csv virá do checklist)."""
        csv_existe = buscar.csv_atual() is not None
        csv_vira = "checklist" in selecionadas
        sem_cursos = None if caminhos.CURSOS.is_dir() else "a pasta Cursos/ não existe nesta branch (ela está na main)"
        sem_csv = None if (csv_existe or csv_vira) else "falta o csv: marque também a etapa Checklist"
        return {
            "checklist": None,
            "extrator": sem_cursos,
            "autores": sem_cursos or sem_csv or (None if (caminhos.REGISTRO.is_file() or "extrator" in selecionadas)
                                                 else "falta Cursos/registro-de-cursos.json: marque também o Extrator"),
            "notion": sem_csv or (None if os.environ.get("NOTION_TOKEN") else "NOTION_TOKEN não definido (veja a aba Notion)"),
        }

    def token_definido(self):
        """True se `NOTION_TOKEN` existe no ambiente (o valor nunca é lido para exibição)."""
        return bool(os.environ.get("NOTION_TOKEN"))

    def testar_conexao(self):
        """Consulta o banco do Notion (só leitura). Devolve (título da fonte de dados, [(coluna, tipo, papel ou "")]).

        Levanta `api.ErroNotion` com a mensagem pronta para mostrar (token, acesso ao banco, colunas faltando).
        """
        cliente = api.Notion()
        fonte = cliente.banco(os.environ.get("NOTION_DATA_SOURCE_ID") or os.environ.get("NOTION_DATABASE_ID") or api.PAGINA_PADRAO)
        mapa = api.mapear_colunas(fonte["properties"])                       # erra com a lista de colunas se faltar alguma das 4
        papel_de = {nome: papel for papel, (nome, _tipo, _p) in mapa.items()}
        colunas = [(nome, p["type"], papel_de.get(nome, "")) for nome, p in fonte["properties"].items()]
        return "".join(t["plain_text"] for t in fonte.get("title", [])) or fonte["id"], colunas

    # ---------------------------------------------------------------- execução
    def _chave(self, etapas):
        """Identifica o ensaio: as etapas e, se o csv não vai ser rebaixado, a impressão digital dele."""
        etapas = tuple(sorted(etapas))
        csv_ = buscar.csv_atual()
        digital = None
        if "checklist" not in etapas and csv_ is not None:
            digital = hashlib.sha256(csv_.read_bytes()).hexdigest()
        return etapas, digital

    def pode_aplicar(self, etapas):
        """True só se já houve um ensaio concluído desta mesma seleção (e do mesmo csv, quando ele não será rebaixado)."""
        return self._ensaio is not None and self._ensaio == self._chave(etapas)

    def esquecer_ensaio(self):
        """Chamar quando a seleção muda: o ensaio anterior deixa de valer."""
        self._ensaio = None

    def rodar(self, etapas, ensaio, commit, saida=print, cancelar=None, progresso=None):
        """Roda as etapas escolhidas (a lógica é a de `automacao.atualizar`). Devolve 0 (terminou) ou 1 (interrompido).

        `ensaio=True`: não grava nada. `ensaio=False` (aplicar): exige um ensaio anterior da mesma seleção, senão `ErroDeEtapa`.
        """
        etapas = [e for e in ETAPAS if e in etapas]
        if not etapas:
            raise ErroDeEtapa("Marque ao menos uma etapa.")
        if not ensaio and not self.pode_aplicar(etapas):
            raise ErroDeEtapa("Faça um Ensaio desta mesma seleção antes de Aplicar.")
        cancelar = cancelar or (lambda: False)
        self.itens, self.resultados = [], []
        codigo = executar(dry_run=ensaio, notion=False, commit=commit, etapas=[e for e in etapas if e != "notion"], saida=saida, cancelar=cancelar)
        if codigo == 0 and "notion" in etapas:
            codigo = self._notion(ensaio, saida, cancelar, progresso)
        if codigo == 0 and ensaio:
            self._ensaio = self._chave(etapas)
        elif not ensaio:
            self._ensaio = None                              # depois de aplicar, um novo ensaio é necessário
        return codigo

    def _notion(self, ensaio, saida, cancelar, progresso):
        """Etapa Notion da execução: monta o modelo do csv e chama `sincronizar` (ensaio ou de verdade). Devolve 0 ou 1 (interrompido)."""
        csv_ = buscar.csv_atual()
        if csv_ is None:
            raise ErroDeEtapa("Não há csv. Aplique a etapa Checklist antes.")
        self.itens = modelo.montar(leitura.ler(csv_))
        self.resultados = sincronizar.sincronizar(self.itens, dry_run=ensaio, saida=saida, cancelar=cancelar, progresso=progresso)
        return 1 if cancelar() else 0

    # ---------------------------------------------------------------- resultados
    def linhas_da_tabela(self):
        """[(curso, status, progresso em %, responsável, resultado)] para a tabela. Vazio se o Notion não rodou."""
        por_nome = {i["nome"]: i for i in self.itens}
        saida = []
        for r in self.resultados:
            i = por_nome.get(r["nome"], {})
            saida.append((r["nome"], i.get("status", ""), f'{round(i.get("progresso", 0) * 100)}%', i.get("responsavel") or "-", r["resultado"]))
        return saida

    def quantos_mudariam(self):
        """Quantos cursos o último ensaio do Notion marcou como `atualizado` (para a confirmação antes de Aplicar)."""
        return sum(1 for r in self.resultados if r["resultado"] == "atualizado")
