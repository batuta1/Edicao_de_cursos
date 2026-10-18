"""
Servidor local de teste: igual ao `python -m http.server`, mas manda o navegador nunca usar cache.

Motivo (DIARIO, E6): ao regerar um pacote na mesma pasta, o navegador reaproveitou o
runtime-data.js antigo e mostrou a versao anterior do curso. Com `no-store`, cada carga busca
os arquivos de novo.

Uso: python servidor_sem_cache.py [porta]   (serve a pasta onde este arquivo esta)
"""
import functools
import http.server
import pathlib
import sys


class SemCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()


if __name__ == '__main__':
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    pasta = str(pathlib.Path(__file__).resolve().parent)
    handler = functools.partial(SemCache, directory=pasta)
    with http.server.ThreadingHTTPServer(('127.0.0.1', porta), handler) as srv:
        print(f'Servindo {pasta} em http://127.0.0.1:{porta} (sem cache)')
        srv.serve_forever()
