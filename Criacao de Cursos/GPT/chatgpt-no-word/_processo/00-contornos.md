# Contornos — ChatGPT no Word

Documento da Fase 0. Define os limites do curso antes de qualquer aula ser escrita. Se algo aqui
mudar, as fases seguintes precisam ser refeitas, não remendadas.

## Objeto base

**ChatGPT aplicado à produção de documentos no Microsoft Word.**

O curso trata do uso do ChatGPT como assistente de escrita para documentos do Word: redigir
primeiras versões, reescrever trechos, resumir, ajustar registro, estruturar sumários e revisar
texto — e, quando o plano permitir, gerar e editar arquivos `.docx` diretamente.

O curso **não** é sobre o Microsoft Copilot, nem sobre o Word em si. O Word entra como destino do
texto; o ChatGPT, como ferramenta de apoio à redação.

## Público-alvo

Professores universitários (docentes do ensino superior), de qualquer área do conhecimento,
inteiramente novatos no uso de inteligência artificial generativa para trabalho de escrita.

Consequências assumidas:

- Escrevem muito e escrevem textos longos: planos de ensino, ementas, pareceres, relatórios de
  projeto, capítulos, editais internos, e-mails institucionais, feedback a alunos.
- Têm exigência alta de correção factual e de autoria — o curso precisa tratar checagem, plágio e
  dados de aluno como assunto de primeira ordem, não como observação final.
- Não são administradores de TI. Nada pode depender de instalar suplemento com privilégio de
  administrador, porque em muitas universidades isso é bloqueado.
- Tempo escasso. Cada exercício precisa produzir algo aproveitável no trabalho real.

## Pré-requisitos

- Nenhum conhecimento prévio de inteligência artificial.
- Saber usar o Word no nível básico: abrir, digitar, salvar, aplicar um estilo de título.
- Conta no ChatGPT (o plano gratuito é suficiente para a maior parte do curso).

## Recursos necessários

- Computador com Microsoft Word instalado (Word 2021 ou superior, ou Microsoft 365) **ou** o Word
  na web.
- Navegador com acesso à internet.
- Conta ChatGPT ativa (gratuita, Go, Plus, Pro, Business, Enterprise ou Edu).
- Um documento real de trabalho do próprio participante, para usar nos exercícios. Recomenda-se
  trabalhar sobre uma **cópia**, nunca sobre o original.

## Natureza

Curso curto, introdutório, prático e **autoinstrucional**. Não há instrutor ao vivo: nenhum passo
pode depender de explicação em tempo real, e todo exercício precisa de critério de êxito verificável
pelo próprio participante.

## Carga horária alvo

| Trilha | Alvo |
|---|---|
| Essentials | 100 a 130 minutos |
| Hands-on | 90 a 120 minutos |

> **Decisão declarada.** Os modelos base das Fases 1–3 sugerem 60–90 min por trilha, mas os
> prompts-mestre do Articulate (Fase 7) exigem 100–130 min em Essentials e 90–120 min em Hands-on.
> Adotou-se desde a Fase 0 a carga horária maior, para que o roteiro final, o cálculo da MET e a
> versão do Rise 360 descrevam o mesmo curso.

## Estrutura definida

| Trilha | Unidades |
|---|---|
| Essentials | Módulo 0 (preparação e limites) + Módulos 1 a 4 (conteúdo) + Módulo 5 (síntese) |
| Hands-on | Preparação + Oficinas 1 a 4 + Projeto Final + A Parte dos Dez |

## Material-fonte

`../../ConteudoBruto/ConteudoBrutoWordCHATGPT_OpenAI.txt`

Reúne três blocos de origem distinta e confiabilidade distinta:

| Bloco | Origem | Tratamento |
|---|---|---|
| Criação e edição de documentos, planilhas e apresentações com o ChatGPT Trabalho | Central de Ajuda da OpenAI | Fonte primária. Usado como está. |
| Perguntas frequentes sobre uploads de arquivos (limites, retenção, treinamento) | Central de Ajuda da OpenAI | Fonte primária. Base do módulo de segurança. |
| "How to Use ChatGPT to Write and Edit Word Documents" | Artigo de terceiros | Fluxo de copiar e colar e lista de prompts: consistente com a prática, aproveitado. |
| Guia sobre o plugin/editor "Revise" | **Material promocional de terceiros** | Não estrutura nenhum módulo. Ver decisão abaixo. |

### Decisão sobre o produto "Revise"

Boa parte do material-fonte é texto de venda de um editor de terceiros chamado Revise. O curso
**não** é construído em torno dele, por três motivos: é produto pago de fornecedor externo, sua
disponibilidade não foi verificada de forma independente, e recomendá-lo a docentes implicaria
enviar documentos institucionais a mais um serviço.

O curso adota, no lugar, os caminhos documentados pela própria OpenAI e pela Microsoft:

1. Copiar e colar entre o navegador e o Word — funciona em qualquer versão e em qualquer plano.
2. Enviar o `.docx` ao ChatGPT para leitura, resumo e extração.
3. Pedir ao ChatGPT um `.docx` pronto para baixar.
4. Suplementos de terceiros da loja do Office, apresentados com suas limitações declaradas.

Ferramentas de terceiros são citadas uma vez, como categoria, com o critério de avaliação que o
docente deve aplicar antes de adotar qualquer uma. Nenhuma é recomendada nominalmente.

## Fato central que o curso precisa deixar explícito

**Não existe suplemento oficial da OpenAI para o Microsoft Word.** Existe para o Excel e para o
PowerPoint; para o Word, não. Quem espera uma barra lateral igual à do Copilot vai procurá-la e não
vai encontrar. O Módulo 0 abre por aí.

## Pendências de validação humana

Estes pontos vieram do material-fonte, que é datado, e devem ser conferidos antes da publicação:

1. Inexistência de suplemento oficial da OpenAI para o Word — conferir na loja de suplementos do
   Office e na Central de Ajuda da OpenAI.
2. Limites de upload (512 MB por arquivo; 2 milhões de tokens por arquivo de texto; 80 arquivos a
   cada 3 horas; 3 uploads por dia no plano gratuito; 25 GB por usuário).
3. Limites de arquivos por projeto (Plus até 20; Pro, Team, Education e Business até 40).
4. Comportamento de retenção: exclusão em até 30 dias após apagar a conversa.
5. Política de treinamento por plano: Business, Enterprise e Edu não treinam por padrão; Plus e Pro
   treinam salvo desativação nos controles de dados.
6. Disponibilidade do `@Template-Creator`, `@Documents` e do fluxo de modelos do ChatGPT Trabalho,
   que dependem de plano e de configurações do espaço de trabalho.
7. Recuperação visual de imagens em PDF apenas no Enterprise.
