// Funções comuns aos blocos HTML do curso Perplexity - Essentials.

// Avisa o Rise (uma vez) que a atividade foi concluída: libera o Continue "completeBlock".
var __concluido = false;
function concluir(idFinal, texto) {
  if (__concluido) return;
  __concluido = true;
  if (idFinal) document.getElementById(idFinal).textContent = texto;
  window.parent.postMessage({ type: 'complete' }, '*');
}

// Copia o texto de um elemento; se a LMS bloquear a área de transferência, deixa o texto selecionado.
function ligarCopia(idBotao, idSaida, idMsg, rotulo) {
  document.getElementById(idBotao).addEventListener('click', function () {
    var el = document.getElementById(idSaida), msg = document.getElementById(idMsg);
    var texto = el.value !== undefined ? el.value : el.textContent;
    function ok() { msg.textContent = rotulo + ' copiado.'; msg.className = 'feedback info'; }
    function falhou() {
      if (el.select) { el.select(); } else {
        var r = document.createRange(); r.selectNodeContents(el);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      }
      var copiou = false; try { copiou = document.execCommand('copy'); } catch (e) {}
      if (copiou) { ok(); } else { msg.textContent = 'O texto está selecionado: use Ctrl+C (ou Cmd+C) para copiar.'; msg.className = 'feedback info'; }
    }
    if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(texto).then(ok, falhou); } else { falhou(); }
  });
}

// Atividade de classificação: cada caso tem uma resposta certa entre as opções.
// cfg = { casos: [{t, extra?, r, p}], opcoes: {chave: rotulo}, dicaErro, idLista, idPlacar, idBarra,
//         rotuloPlacar, aoConcluir: function () {} }
function classificador(cfg) {
  var certos = {}, lista = document.getElementById(cfg.idLista);
  cfg.casos.forEach(function (caso, i) {
    var c = document.createElement('div'); c.className = 'item';
    var titulo = document.createElement('p'); titulo.className = 'f'; titulo.id = cfg.idLista + '-c' + i;
    titulo.textContent = caso.t;
    c.appendChild(titulo);
    if (caso.extra) {
      var ex = document.createElement('div'); ex.className = 'extra'; ex.innerHTML = caso.extra; c.appendChild(ex);
    }
    var g = document.createElement('div'); g.className = 'opcoes'; g.setAttribute('role', 'group');
    g.setAttribute('aria-labelledby', titulo.id);
    var fb = document.createElement('div'); fb.className = 'feedback'; fb.setAttribute('aria-live', 'polite');
    Object.keys(cfg.opcoes).forEach(function (k) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'btn'; b.textContent = cfg.opcoes[k];
      b.setAttribute('data-k', k); b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function () {
        g.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        if (k === caso.r) {
          certos[i] = true; c.className = 'item certo';
          fb.textContent = 'Correto. ' + caso.p; fb.className = 'feedback ok';
        } else {
          delete certos[i]; c.className = 'item errado';
          fb.textContent = 'Não é “' + cfg.opcoes[k] + '”. ' + (caso.dica || cfg.dicaErro); fb.className = 'feedback erro';
        }
        placar();
      });
      g.appendChild(b);
    });
    c.appendChild(g); c.appendChild(fb); lista.appendChild(c);
  });
  function placar() {
    var n = Object.keys(certos).length, total = cfg.casos.length;
    document.getElementById(cfg.idPlacar).textContent = n + ' de ' + total + ' ' + cfg.rotuloPlacar;
    document.getElementById(cfg.idBarra).style.width = (100 * n / total) + '%';
    if (n === total && cfg.aoConcluir) cfg.aoConcluir();
  }
  placar();
}

// Checklist: libera quando todos os itens estão marcados.
function checklist(itens, idLista, idPlacar, idBarra, rotuloPlacar, aoConcluir) {
  var marcados = {}, lista = document.getElementById(idLista);
  itens.forEach(function (txt, i) {
    var l = document.createElement('label'); l.className = 'chk';
    var c = document.createElement('input'); c.type = 'checkbox';
    var s = document.createElement('span'); s.textContent = txt;
    c.addEventListener('change', function () {
      if (c.checked) { marcados[i] = true; l.classList.add('feito'); } else { delete marcados[i]; l.classList.remove('feito'); }
      atualizar();
    });
    l.appendChild(c); l.appendChild(s); lista.appendChild(l);
  });
  function atualizar() {
    var n = Object.keys(marcados).length;
    document.getElementById(idPlacar).textContent = n + ' de ' + itens.length + ' ' + rotuloPlacar;
    document.getElementById(idBarra).style.width = (100 * n / itens.length) + '%';
    if (n === itens.length) aoConcluir();
  }
  atualizar();
}
