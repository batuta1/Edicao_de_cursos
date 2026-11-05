# Contornos — ChatGPT no PowerPoint

Documento da Fase 0. Define os limites do curso antes de qualquer aula ser escrita. Se algo aqui
mudar, as fases seguintes precisam ser refeitas, não remendadas.

## Objeto base

**ChatGPT para PowerPoint — o suplemento oficial da OpenAI dentro do Microsoft PowerPoint.**

Diferente do curso irmão sobre o Word, aqui existe integração nativa: o ChatGPT aparece como uma
barra lateral dentro do próprio PowerPoint e trabalha sobre a apresentação aberta, preservando a
estrutura editável dos slides. O curso trata de instalar esse suplemento, usá-lo para criar um
primeiro rascunho a partir de material de origem, revisar e ampliar apresentações existentes,
ajustar a apresentação a um público específico, e interrogar a narrativa de um deck.

O curso **não** é sobre design gráfico de slides, nem sobre o Copilot da Microsoft.

## Público-alvo

Professores universitários (docentes do ensino superior), de qualquer área do conhecimento,
inteiramente novatos no uso de inteligência artificial generativa.

Consequências assumidas:

- Produzem apresentações em volume alto e sob pressão de tempo: aulas, bancas, defesas, congressos,
  reuniões de colegiado, relatórios de projeto para agências de fomento.
- Já têm o conteúdo em outro formato — artigo, capítulo, plano de ensino, planilha de resultados — e
  o gargalo é transformá-lo em estrutura de slides.
- A instituição frequentemente controla a instalação de suplementos. O curso precisa cobrir o
  caminho do usuário comum **e** dizer com clareza o que fazer quando o caminho está bloqueado.
- Rigor factual inegociável: um número errado em um slide de banca ou de agência de fomento tem
  custo real.

## Pré-requisitos

- Nenhum conhecimento prévio de inteligência artificial.
- Saber usar o PowerPoint no nível básico: criar slide, digitar em caixa de texto, aplicar um tema,
  salvar.
- Conta no ChatGPT (o plano gratuito funciona, com uso limitado).

## Recursos necessários

- Computador com Microsoft PowerPoint instalado — versão que suporte suplementos do Office
  (PowerPoint 2021 ou superior, ou Microsoft 365). **Pendente de validação:** a versão mínima exata
  não consta do material-fonte.
- Permissão para adicionar suplementos do Office, **ou** um administrador do Microsoft 365 disposto
  a implantar o suplemento pelo arquivo de manifesto.
- Navegador com acesso à internet.
- Conta ChatGPT ativa (Free, Go, Plus, Pro, Business, Enterprise ou Edu).
- Uma apresentação real do próprio participante e um documento de origem (artigo, plano de ensino,
  anotações), para os exercícios. Trabalhar sempre sobre **cópia**.

## Natureza

Curso curto, introdutório, prático e **autoinstrucional**. Nenhum passo pode depender de explicação
ao vivo; todo exercício precisa de critério de êxito verificável pelo próprio participante.

## Carga horária alvo

| Trilha | Alvo |
|---|---|
| Essentials | 100 a 130 minutos |
| Hands-on | 90 a 120 minutos |

> **Decisão declarada.** Adotou-se desde a Fase 0 a carga horária dos prompts-mestre do Articulate
> (Fase 7), em vez dos 60–90 min dos modelos base, para que roteiro, cálculo da MET e versão do
> Rise 360 descrevam o mesmo curso.

## Estrutura definida

| Trilha | Unidades |
|---|---|
| Essentials | Módulo 0 (instalação e limites) + Módulos 1 a 4 (conteúdo) + Módulo 5 (síntese) |
| Hands-on | Preparação + Oficinas 1 a 4 + Projeto Final + A Parte dos Dez |

## Material-fonte

`../../ConteudoBruto/ConteudoBrutoPowerPointCHATGPT_OpenAI.txt`

Documento único, da Central de Ajuda da OpenAI, sobre o ChatGPT para PowerPoint. É fonte primária e
o mais confiável dos três materiais brutos deste lote — mas também o mais curto (cerca de 11 KB).

Consequência: **este é o curso com maior risco de o autor completar lacunas por conta própria.**
Tudo o que não estiver no material-fonte precisa entrar em formulação genérica, com sinalização de
conferência, e não como afirmação sobre a interface.

O que o material-fonte cobre e sustenta:

- O que o suplemento é e para quem serve.
- Caminho de instalação pelo Marketplace da Microsoft e caminho alternativo via manifesto.
- Como usar bem: especificidade, pedir o plano antes de editar, usar material de origem, revisar.
- Seis prompts de exemplo.
- Limitações declaradas: aderência a modelos, edições avançadas, resultados incorretos.
- Skills e apps: o que são, como acessar, controles de administrador.
- Disponibilidade e preços, consumo de créditos (10 a 50 por mensagem com GPT-5.5).
- Privacidade: a Microsoft pode ler o conteúdo dos arquivos, pelos termos do Marketplace.
- Erro conhecido de SSO no suplemento do Office.

## Fatos centrais que o curso precisa deixar explícitos

1. **A Microsoft pode ler o conteúdo dos arquivos do PowerPoint**, como parte dos Termos de Serviço
   do Marketplace de Suplementos. Isso muda a conversa sobre dados sensíveis de alunos e de
   pesquisa, e precisa aparecer antes do primeiro uso real.
2. **O ChatGPT pode editar ou excluir conteúdo da apresentação.** A recomendação da própria OpenAI é
   duplicar o arquivo antes de trabalhos importantes. Isso vira regra de ouro do curso.
3. **A instalação pode estar bloqueada pela instituição.** O curso precisa de um caminho declarado
   para esse caso, e não pode tratá-lo como exceção rara.

## Pendências de validação humana

1. Versão mínima do PowerPoint compatível com o suplemento (não consta do material-fonte).
2. Nomes exatos dos itens de menu em português: `Página Inicial > Suplementos` — conferir se a
   interface em pt-BR usa exatamente esses rótulos.
3. Disponibilidade do suplemento na conta institucional do participante.
4. Consumo de créditos (10 a 50 por mensagem com GPT-5.5) e datas de vigência da cobrança flexível.
5. Existência e nomes das Skills e apps disponíveis na interface do PowerPoint.
6. Comportamento atual do erro de SSO e se a correção pelo ACS ainda se aplica.
7. Disponibilidade em Residência de Dados da UE, Residência de Inferência e Gerenciamento de Chaves
   Empresariais — depende da implantação do espaço de trabalho.

---

## Revisão de 7 de outubro de 2026 — novo material-fonte

Acrescentado o material-fonte `../compilado-chatgpt-powerpoint.txt`: síntese em português, redigida
em palavras próprias, do mesmo artigo da Central de Ajuda da OpenAI, consultado em 7 de outubro de
2026. Passa a ser a **fonte de referência principal**; a fonte antiga permanece como apoio para a
redação em português de mensagens de interface (por exemplo, o texto literal do erro de SSO).

**O que não muda:** objeto base, público-alvo, pré-requisitos, recursos, natureza, carga horária
alvo e estrutura. Por isso as fases seguintes foram **revisadas**, e não refeitas do zero. O registro
completo está em `03-integracao-compilado.md`.

**Fato central acrescentado:**

4. **Há duas administrações, não uma.** Quem administra o Microsoft 365 controla a instalação do
   suplemento; quem administra o espaço de trabalho do ChatGPT controla a habilitação do recurso e
   dos apps. Em conta institucional, o suplemento pode estar instalado e ainda não funcionar.

**Pendências revistas:**

- Item 2 (rótulos de menu): o compilado fornece os rótulos em inglês — `Home > Add-ins` e, no centro
  de administração, `Integrated apps > Deploy Add-in > Upload custom apps`. Os rótulos em português
  continuam a conferir.
- Item 4 (créditos): confirmado na data de consulta (10 a 50 créditos por mensagem com GPT-5.5;
  mesmas tarifas do ChatGPT para Excel/Sheets). Continua sujeito a alteração.
- Item 6 (SSO): o compilado registra que a pergunta da fonte cita nominalmente o suplemento do Excel.
  Conferir se o erro ocorre igualmente no PowerPoint.
- **Novo:** liberação gradual do recurso — confirmar se ainda há contas sem acesso por esse motivo.
- **Novo:** nome exato da opção, nas configurações do espaço de trabalho do ChatGPT, que habilita o
  ChatGPT para PowerPoint.
