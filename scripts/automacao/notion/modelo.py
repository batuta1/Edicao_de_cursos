"""F4 (sem rede): do csv monta o que deve estar no Notion para cada curso."""
from ..checklist import leitura


def montar(linhas):
    """[{nome, status, progresso (0 a 1), responsavel (João | Marina | None)}]. Linha sem nome é ignorada."""
    saida = []
    for l in linhas:
        nome = leitura.valor(l, "Curso")
        if not nome:
            continue
        autor, _ = leitura.autor_da_linha(l)
        saida.append({"nome": nome, **leitura.situacao(l), "responsavel": autor})
    return saida


def tabela(itens):
    """Texto em colunas com o que seria enviado ao Notion (usado no ensaio sem token)."""
    L = [f'{"Curso":45} {"Status":12} {"Prog.":>5}  Responsável']
    for i in itens:
        L.append(f'{i["nome"][:45]:45} {i["status"]:12} {round(i["progresso"] * 100):>4}%  {i["responsavel"] or "-"}')
    return "\n".join(L)
