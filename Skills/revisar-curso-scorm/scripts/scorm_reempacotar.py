"""
Fases 6+7 do pipeline: funde as licoes editadas no curso, serializa para Base64 e
reinsere no pacote SCORM, gerando um .zip novo.

O .zip de entrada nunca e' modificado. Todo o resto do pacote (fontes, JS, CSS, imagens,
manifest) e' copiado sem alteracao — so' o arquivo que carrega o payload muda. A verificacao
final confere isso comparando o tamanho de cada entrada do zip antigo com o novo.

Uso:
    # so' funde e serializa (para colagem manual, fluxo original do projeto):
    python scorm_reempacotar.py curso.json licoes_extraidas_X/ --base64-saida curso_editado_base64.txt

    # fluxo completo, gerando tambem o pacote revisado:
    python scorm_reempacotar.py curso.json licoes_extraidas_X/ \
        --base64-saida curso_editado_base64.txt \
        --json-saida curso_editado.json \
        --pacote-original ../Curso.zip --pacote-saida ../Curso-REVISADO.zip
"""
import argparse
import base64
import json
import pathlib
import re
import sys
import zipfile

ALVO_DEFAULT = 'scormcontent/runtime-data.js'
ALVO_LEGACY = 'scormcontent/index.html'


def fundir(curso_path, pasta_licoes):
    curso = json.loads(pathlib.Path(curso_path).read_text(encoding='utf-8'))
    por_id = {l['id']: l for l in curso['course']['lessons']}

    editadas = []
    for arq in sorted(pathlib.Path(pasta_licoes).glob('licao_*.json')):
        c = json.loads(arq.read_text(encoding='utf-8'))
        licao = c['lesson']
        if licao['id'] not in por_id:
            raise SystemExit(f'{arq.name}: lesson.id fora do curso. Pasta e curso nao batem.')
        editadas.append((c.get('numero_da_licao', 9999), licao, arq.name))

    if len(editadas) != len(por_id):
        raise SystemExit(
            f'QUANTIDADE DE LICOES MUDOU: curso tem {len(por_id)}, pasta tem {len(editadas)}.'
        )

    editadas.sort(key=lambda x: x[0])
    curso['course']['lessons'] = [l for _, l, _ in editadas]
    for numero, licao, nome in editadas:
        print(f'   licao {numero:02d}: {licao.get("title")}   <- {nome}')
    return curso


def serializar(curso):
    compacto = json.dumps(curso, ensure_ascii=False, separators=(',', ':'))
    b64 = base64.b64encode(compacto.encode('utf-8')).decode('ascii')
    # round-trip: o Base64 tem que voltar a ser exatamente o mesmo objeto
    if json.loads(base64.b64decode(b64).decode('utf-8')) != curso:
        raise SystemExit('ROUND-TRIP FALHOU. Nada foi gravado.')
    return b64


def reempacotar(pacote_in, pacote_out, b64):
    zin = zipfile.ZipFile(pacote_in)
    nomes = zin.namelist()
    if ALVO_DEFAULT in nomes:
        alvo = ALVO_DEFAULT
        padrao = r'(__jsonp\("runtime-data\.js",")[A-Za-z0-9+/=]+("\))'
    elif ALVO_LEGACY in nomes:
        alvo = ALVO_LEGACY
        padrao = r'(deserialize\(")[A-Za-z0-9+/=]+("\))'
    else:
        raise SystemExit('Formato do pacote nao reconhecido.')

    original = zin.read(alvo).decode('utf-8')
    novo = re.sub(padrao, lambda m: m.group(1) + b64 + m.group(2), original, count=1)
    if novo == original:
        raise SystemExit(f'SUBSTITUICAO NAO OCORREU em {alvo}. Confira o padrao.')

    # zipfile nao substitui entradas in-place: reescreve o pacote trocando so' o alvo
    with zipfile.ZipFile(pacote_out, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            dados = novo.encode('utf-8') if item.filename == alvo else zin.read(item.filename)
            zout.writestr(item, dados)

    za, zb = zipfile.ZipFile(pacote_in), zipfile.ZipFile(pacote_out)
    if len(za.namelist()) != len(zb.namelist()):
        raise SystemExit('QUANTIDADE DE ARQUIVOS NO PACOTE MUDOU!')
    difs = [n for n in za.namelist()
            if n != alvo and za.getinfo(n).file_size != zb.getinfo(n).file_size]
    print(f'   alvo substituido       : {alvo}')
    print(f'   arquivos no pacote     : {len(zb.namelist())}')
    print(f'   alterados fora do alvo : {len(difs)} {difs[:5] if difs else ""}')
    if difs:
        raise SystemExit('!! O pacote novo diverge do original fora do arquivo alvo.')

    conferido = zb.read(alvo).decode('utf-8')
    m = re.search(r'"([A-Za-z0-9+/=]{500,})"', conferido)
    d = json.loads(base64.b64decode(m.group(1) + '=' * (-len(m.group(1)) % 4)).decode('utf-8'))
    print(f'   titulo no pacote novo  : {d["course"]["title"]} ({len(d["course"]["lessons"])} licoes)')
    return alvo


def main():
    p = argparse.ArgumentParser(description='Funde licoes editadas, serializa e reempacota o SCORM.')
    p.add_argument('curso_original')
    p.add_argument('pasta_licoes')
    p.add_argument('--base64-saida', required=True, help='arquivo .txt com o Base64 final')
    p.add_argument('--json-saida', help='opcional: grava tambem o curso fundido em JSON')
    p.add_argument('--pacote-original', help='.zip SCORM de entrada (nao e modificado)')
    p.add_argument('--pacote-saida', help='.zip SCORM revisado a gerar')
    args = p.parse_args()

    print('Fundindo licoes editadas no curso...')
    curso = fundir(args.curso_original, args.pasta_licoes)

    if args.json_saida:
        pathlib.Path(args.json_saida).write_text(
            json.dumps(curso, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'JSON fundido gravado: {args.json_saida}')

    print('Serializando para Base64 (com verificacao de round-trip)...')
    b64 = serializar(curso)
    destino_b64 = pathlib.Path(args.base64_saida)
    if destino_b64.exists():
        backup = destino_b64.with_suffix(destino_b64.suffix + '.bak')
        backup.write_text(destino_b64.read_text(encoding='utf-8'), encoding='utf-8')
        print(f'   backup da versao anterior: {backup.name}')
    destino_b64.write_text(b64, encoding='utf-8', newline='')
    print(f'Base64 gravado: {destino_b64}  ({len(b64):,} caracteres)')

    if args.pacote_original and args.pacote_saida:
        print('Reempacotando o SCORM...')
        reempacotar(args.pacote_original, args.pacote_saida, b64)
        print(f'Pacote revisado: {args.pacote_saida}')
    else:
        print('(Pacote SCORM nao gerado — use --pacote-original e --pacote-saida se quiser.)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
