// Checklist da revisão em seis pontos — conta os itens marcados e mostra o fechamento.
// Este bloco nao trava o Continue (hasCustomCompletion = false): o E7c testa so a pasta em assets/.
(function () {
  var caixas = Array.prototype.slice.call(document.querySelectorAll('.itens input'));
  var barra = document.getElementById('barra');
  var contagem = document.getElementById('contagem');
  var final = document.getElementById('final');

  function atualizar() {
    var marcados = caixas.filter(function (c) { return c.checked; }).length;
    caixas.forEach(function (c) { c.closest('li').classList.toggle('feito', c.checked); });
    barra.style.width = (marcados / caixas.length * 100) + '%';
    contagem.textContent = marcados + ' de ' + caixas.length + ' pontos conferidos';
    final.hidden = marcados !== caixas.length;
  }

  caixas.forEach(function (c) { c.addEventListener('change', atualizar); });
  document.getElementById('recomecar').addEventListener('click', function () {
    caixas.forEach(function (c) { c.checked = false; });
    atualizar();
  });
  atualizar();
})();
