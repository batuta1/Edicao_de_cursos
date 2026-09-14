Plano de Aula 1 de um Mini-Curso:
```DOS
      # MÓDULO 1: O QUE É CLAUDE DESKTOP? (VISÃO GERAL)

      ## Seção 1.1: Claude Desktop vs Web (claude.ai)

      ### 📸 Sugestão de Prints:
      - Tela lado a lado: claude.ai web vs Claude Desktop app
      - Interface do Desktop mostrando abas (Chat, Code, Cowork)
      - Ícone do aplicativo na taskbar/dock

      ## Descrição

      **O que mudou?** Você conhece [claude.ai](https://claude.ai) (web). Claude Desktop é a **versão aplicativo** do mesmo Claude, mas com superpoderes para trabalhar com código.

      ### Objetivos da Aula:
      - Entender a diferença entre Web e Desktop
      - Conhecer o que Desktop oferece que Web não oferece
      - Entender por que Desktop é preferível para desenvolvimento

      ### Habilidades Esperadas:
      - ✅ Explicar as 3 diferenças principais entre Web e Desktop
      - ✅ Saber quando usar Web e quando usar Desktop
      - ✅ Identificar os 3 principais diferenciais do Desktop

      ---

      ## Seção 1.2: Diferenças Principais

      ### Conteúdo:

      | Aspecto | Web (claude.ai) | Desktop |
      |--------|-----------------|---------|
      | **Acesso a Arquivos Locais** | ❌ Não | ✅ **Sim** |
      | **Velocidade** | Normal | **Mais rápido** (menos latência) |
      | **Terminal Integrado** | ❌ Não | ✅ **Sim** |
      | **Sessões Offline** | ❌ Não | ⚠️ Limitado |
      | **Git Integration** | ❌ Não | ✅ **Sim** |
      | **Integração com Arquivos** | Cola manual | ✅ **Automática** |
      | **Abas (Chat, Code, Cowork)** | Parcial | ✅ **Todas** |

      ### O Grande Diferencial: Acesso ao Sistema de Arquivos Local

      **Web (claude.ai):**
      ```
      Você: "Aqui está meu código" (copia manualmente)
      Claude: (lê o que você colou)
      ```

      **Desktop:**
      ```
      Claude: (acessa todo seu projeto automaticamente)
      Você: "Mude este arquivo"
      Claude: (modifica direto no seu disco)
      ```

      Isto muda **tudo**. Você não copia/cola. Claude vê seu projeto inteiro. Trabalha de verdade.

      ---

      ## Seção 1.3: Casos de Uso Ideais para Desktop

      ### Conteúdo:

      **Use Desktop quando:**
      - ✅ Trabalhando com projeto real (múltiplos arquivos)
      - ✅ Precisa de terminal integrado
      - ✅ Quer que Claude altere código automaticamente
      - ✅ Trabalhando offline ou com latência alta

      **Use Web quando:**
      - ✅ Perguntando conceito rápido ("O que é REST API?")
      - ✅ Sem acesso ao aplicativo
      - ✅ Em computador compartilhado

      ---

      ## Seção 1.4: As Três Abas: Chat, Code, Cowork

      ### 📸 Sugestão de Prints:
      - Interface Desktop com as 3 abas visíveis no topo
      - Aba Chat aberta
      - Aba Code aberta (com projeto)
      - Aba Cowork aberta

      ### Conteúdo:

      **Aba Chat:** Perguntas gerais, explicações conceituais  
      > "Explique o que é um loop for"  
      > "Qual é a diferença entre variável global e local?"

      **Aba Code:** Trabalhar com arquivos reais do seu projeto  
      > "Corrija os erros neste projeto"  
      > "Adicione função para calcular média"

      **Aba Cowork:** Agente automático que trabalha sozinho em background  
      > "Execute testes, crie relatório, envie resumo — tudo sem supervisão"

      **Analogia:** Chat é perguntar, Code é trabalhar na bancada, Cowork é contratar um assistente.

      ---

      ## Pílula Hands-on: Identificar Casos de Uso (5 minutos)

      Para cada tarefa abaixo, escreva qual aba você usaria (Chat, Code ou Cowork):

      1. "Explique o que é um ponteiro em C"  
         Aba: ________

      2. "Mude os 3 arquivos deste projeto para usar nomes em português"  
         Aba: ________

      3. "Execute testes todas as noites e avise se falhar"  
         Aba: ________

      4. "Me mostre um exemplo de construtor em Python"  
         Aba: ________

      5. "Revise meu relatório de laboratório e sugira melhorias"  
         Aba: ________

      **Respostas esperadas:** 1-Chat, 2-Code, 3-Cowork, 4-Chat, 5-Code
```

Plano de Aula 2 de um Mini-Curso:

```DOS
      # MÓDULO 14: SKILLS E COMANDOS

      ## Seção 14.1: Automatizar Tarefas Repetidas

      ### 📸 Sugestão de Prints:
      - Menu "/" mostrando comandos disponíveis
      - Botão "+" para adicionar skill
      - Skill sendo executada

      ## Descrição

      **Skills** são tarefas **reutilizáveis**. Define uma vez, usa sempre.

      ### Objetivos da Aula:
      - Entender o que é skill
      - Usar skills existentes
      - Criar skill personalizada

      ### Habilidades Esperadas:
      - ✅ Acessar comandos com "/"
      - ✅ Usar skill existente
      - ✅ Entender poder de automação

      ---

      ## Seção 14.2: Usando Skills

      ### 📸 Sugestão de Prints:
      - Menu "/" aberto mostrando /check, /test, etc
      - Skill executada instantaneamente

      ### Conteúdo:

      **Algumas skills existentes:**
      - `/check` — verifica se código está pronto
      - `/test` — roda testes
      - `/lint` — verifica formatação e estilo
      - `/doc` — gera documentação

      **Como usar:**

      1. Comece a escrever "/" na aba Code
      2. Menu mostra skills disponíveis
      3. Clique skill desejada
      4. Skill é executada

      Exemplo:
      ```
      Você digita: /test
      Claude: "Vou executar pytest"
            [Testes rodam]
            [Resultado mostrado]
      ```

      ---

      ## Seção 14.3: Criando Skills Pessoais

      ### Conteúdo:

      Você pode criar skills customizadas. Exemplo:

      ```
      Skill: /review-code

      Descrição: Revisa código e checa:
      - Type hints presentes?
      - Docstrings presentes?
      - Sem erros óbvios?
      - Segue padrões do projeto?

      Sempre que você digita /review-code, Claude executa esta checklist.
      ```

      ---

      ## Pílula Hands-on: Usar Skills (5 minutos)

      1. **Aba Code aberta**
      2. **Digite "/" para ver skills disponíveis**
      3. **Teste uma skill** (ex: `/test`)
      4. **Observe resultado**
```