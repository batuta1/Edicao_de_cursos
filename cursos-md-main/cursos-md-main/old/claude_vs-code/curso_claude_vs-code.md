<link rel="stylesheet" href="../.css/style.css">

# Platforms and Integrations: Use Claude Code in VS Code
## Roteiro Completo — Developer Experience Edition

**Versão:** 2.0 (Refatorado com foco em DX)  
**Público-alvo:** Desenvolvedores iniciantes e intermediários (Engenharia, Ciência de Dados, Full-Stack)  
**Tempo total:** 4-6 horas de prática  
**Pré-requisito:** Noções básicas de terminal e um projeto Git já iniciado (ou vazio)

---

## AULA 1 — Claude Code: O Que Muda Na Sua IDE?

### Entender o Ecossistema

**Objetivos da Aula:**
- Compreender o que Claude Code adiciona ao VS Code vs. usar Claude web
- Entender o modelo de segurança (o que sai de sua máquina, o que fica local)
- Identificar casos de uso onde Claude Code é mais efetivo

**Habilidades Esperadas:**
- Capacidade de descrever diferenças entre Chat web, CLI e extensão VS Code
- Compreensão clara de o que Claude pode/não pode fazer
- Decisão informada: "Devo usar Claude Code ou Chat web para essa tarefa?"

### Conteúdo Conceitual

#### 📌 Mapa Mental: Claude no Seu Fluxo

```
Seu Projeto (Local)
├── VS Code (Editor)
│   ├── Claude Code (Extensão)
│   │   ├── Acesso a arquivos abertos
│   │   ├── Referência a linhas de código
│   │   └── Terminal integrado
│   └── Outros (Git, Debug, etc.)
└── Servidores Anthropic (Remoto)
    └── Processa prompts e retorna respostas
```

**Diferenças Críticas:**

| Aspecto | Claude Web | Claude Code (VS Code) | CLI (Claude Desktop) |
|---------|------------|----------------------|----------------------|
| Acesso a arquivos locais | ❌ Upload manual | ✅ Automático (abertos) | ✅ Automático (path) |
| Contexto do projeto | ❌ Você copia/cola | ✅ Referencia automática | ✅ Contexto completo |
| Integração IDE | ❌ Tab separada | ✅ Painel integrado | ✅ Terminal integrado |
| Diff review | ❌ Não disponível | ✅ Lado a lado | ✅ Terminal output |
| Ideal para | Perguntas pontuais | Trabalho em projeto | Automação, scripts |

#### 🔐 Modelo de Segurança e Dados

**O Que Sai de Sua Máquina (Enviado para Anthropic):**
- Conteúdo dos arquivos que você referencia
- Seu prompt / pergunta
- Metadados: nome do arquivo, linhas selecionadas

**O Que Fica Local:**
- Sua chave de API (armazenada no keychain/credstore do SO)
- Histórico de conversas (salvo em `~/.anthropic/` ou equiv.)
- Arquivos do projeto (não são copiados para servidor)

**⚠️ Nunca envie por Claude Code:**
```
❌ Chaves de API de terceiros
❌ Senhas, tokens de autenticação
❌ Dados sensíveis (PII, HIPAA, dados financeiros)
❌ Código sob NDA ou proprietário sem aprovação
❌ Informações de negócio confidencial
```

#### 📊 Casos de Uso Recomendados

**✅ Claude Code é forte em:**
1. Refatoração de funções com contexto do projeto
2. Debugging com análise do código real
3. Geração de testes unitários baseado no código existente
4. Documentação automática de código
5. Revisão de código (pull request helper)
6. Explicação de erros com stack trace

**⚠️ Claude Web é melhor para:**
1. Questões teóricas (algoritmos, arquitetura)
2. Brainstorming sem código
3. Explicações educacionais
4. Comparar múltiplas ferramentas

---

## AULA 2 — Instalação e Configuração Inicial

### Pré-Requisitos: O Checklist Real

**Objetivos da Aula:**
- Verificar requisitos técnicos do seu ambiente
- Identificar potenciais bloqueios (proxy, permissões, SO)
- Planejar instalação antes de executar

**Habilidades Esperadas:**
- Capacidade de verificar versão do VS Code
- Saber se há restrições de instalação de extensões
- Entender diferenças de caminho entre SO

### Checklist por Contexto de Uso

#### Contexto 1: Notebook Pessoal (Windows/Mac/Linux)

```markdown
- [ ] VS Code versão 1.95.0 ou superior instalado
  - Verificar: Help → About (Windows/Linux) ou Code → About (Mac)
- [ ] Acesso à pasta de extensões (nenhuma restrição)
- [ ] Conexão com internet estável
- [ ] Conta Anthropic criada em claude.ai
- [ ] Terminal funcionando (cmd.exe no Windows, zsh/bash no Mac/Linux)
```

#### Contexto 2: Máquina de Laboratório (Gerenciada por TI)

```markdown
⚠️ ATENÇÃO: Máquinas gerenciadas podem ter restrições.

ANTES de instalar, PERGUNTE ao seu admin TI:
1. "Posso instalar extensões do VS Code?"
2. "Há restrição de firewall/proxy?"
3. "Claude Code é permitido (política de dados)?"
4. "Há política sobre envio de código para servidores externos?"

Se a resposta for "NÃO": Use Claude Web ou CLI em máquina pessoal.
```

#### Contexto 3: Máquina Corporativa (VPN, Proxy)

```markdown
Bloqueadores comuns:
- Proxy corporativo (requer autenticação)
- Firewall restritivo (whitelist de domínios)
- Política MDM que desativa extensões

Solução:
1. Verifique se api.anthropic.com está whitelisted
2. Configure proxy no VS Code (File → Preferences → Settings → "proxy")
3. Se não conseguir: use Claude Web em navegador corporativo (mais permissivo)
```

---

### Instalação Passo a Passo (Windows 11)

**📸 Sugestão de Print 1:** VS Code aberto com menu Extensions (Ctrl+Shift+X)

#### Passo 1: Abrir a Aba de Extensões

```
1. Abra VS Code
2. Pressione Ctrl + Shift + X (ou Cmd + Shift + X no Mac)
3. Uma barra lateral deve aparecer à esquerda mostrando "Extensions"
```

**📸 Sugestão de Print 2:** Campo de pesquisa com "claude" digitado, mostrando resultados

#### Passo 2: Procurar e Instalar Claude Code

```
1. No campo de pesquisa (topo da aba Extensions), digite: claude code
2. Procure pela extensão oficial (publicada por Anthropic Inc.)
3. Clique no botão "Install" (verde)
4. Aguarde a instalação (deve levar 30-60 segundos)
```

**📸 Sugestão de Print 3:** Botão "Install" mudando para "Uninstall" ou indicador de carregamento

#### Passo 3: Recarregar VS Code (Se Necessário)

```
1. Após instalar, o VS Code pode pedir para recarregar
2. Clique em "Reload" na notificação
3. Ou: Ctrl + Shift + P (Paleta de Comandos) → "Developer: Reload Window"
```

---

### Instalação Passo a Passo (macOS — Intel)

**Diferenças em relação a Windows:**

| Etapa | Windows | macOS Intel | macOS Apple Silicon |
|-------|---------|-------------|-------------------|
| Atalho Extensions | Ctrl + Shift + X | Cmd + Shift + X | Cmd + Shift + X |
| Armazenar Chaves | Credential Manager | Keychain | Keychain (rosetta) |
| Pasta Extensões | `%USERPROFILE%\.vscode\extensions` | `~/.vscode/extensions` | `~/.vscode/extensions` |
| CLI Path | `C:\Users\[user]\AppData\Local\Programs\Microsoft VS Code\bin` | `/Applications/Visual Studio Code.app/Contents/Resources/app/bin` | Mesmo (Rosetta) |

**📸 Sugestão de Print 4:** Menu Apple no macOS mostrando "About Visual Studio Code" para verificação de versão

---

### Instalação Passo a Passo (Linux — Ubuntu 22.04 LTS)

**Caso 1: VS Code Já Instalado via Snap ou APT**

```bash
# Verificar versão instalada
code --version

# Resultado esperado:
# 1.95.0 (ou superior)
# ...
```

**Caso 2: VS Code Não Instalado**

```bash
# Instalar VS Code no Ubuntu via APT (oficial)
sudo apt update
sudo apt install code

# Ou via Snap
sudo snap install code --classic
```

**📸 Sugestão de Print 5:** Terminal exibindo `code --version` com output da versão

---

### Configuração de Chave de API Anthropic

**Objetivos:**
- Conectar VS Code ao sua conta Anthropic
- Armazenar chave de forma segura no SO

**Habilidades Esperadas:**
- Saber onde encontrar a chave de API
- Entender diferença entre API key e senha da conta
- Armazenar seguramente (não em `.env` versionado)

#### Passo 1: Gerar Chave de API

```
1. Abra https://console.anthropic.com (faça login com sua conta Claude)
2. Navegue até: API Keys (menu esquerdo) ou Settings → API Keys
3. Clique em "Create API Key"
4. Dê um nome descritivo (ex: "VS Code Dev Machine")
5. Copie a chave (você verá apenas uma vez!)
6. Guarde em lugar seguro (não commit em Git)
```

**📸 Sugestão de Print 6:** Tela do console Anthropic mostrando página de API Keys com botão "Create API Key"

#### Passo 2: Configurar VS Code

Agora que você tem a chave, insira no VS Code:

**Método 1: Prompt Automático (Recomendado)**

```
1. Abra VS Code
2. Clique no ícone Spark (Claude Code) na barra lateral ou:
   Ctrl + Shift + P → "Claude Code: Sign In"
3. Uma caixa de diálogo aparecerá solicitando chave de API
4. Cole a chave e pressione Enter
5. VS Code armazenará no Keychain (Mac) / Credential Manager (Windows) / Pass (Linux)
```

**📸 Sugestão de Print 7:** Diálogo de entrada de API Key no VS Code

**Método 2: Variável de Ambiente (Para Scripting/CLI)**

```bash
# No seu shell (.bashrc, .zshrc, .profile, etc.)
export ANTHROPIC_API_KEY="sk-ant-xxxxxx..."

# Depois recarregue:
source ~/.bashrc
```

**⚠️ NUNCA faça isto:**
```bash
# ❌ ERRADO: Versionando chave em .env
ANTHROPIC_API_KEY=sk-ant-xxxxx
git add .env
git commit -m "Add API key"  # 😱 EXPOSTO!

# ✅ CORRETO: Adicionar .env ao .gitignore
echo ".env" >> .gitignore
git add .gitignore
```

---

### Verificação de Instalação

**Checklist Final:**

```markdown
- [ ] VS Code está versão 1.95+
- [ ] Extensão Claude Code aparece na aba Extensions
- [ ] Ícone Spark (⚡) visível na barra lateral esquerda
- [ ] Clicando no ícone, painel de chat abre
- [ ] Ao fazer primeira pergunta, recebe resposta (sem erro de autenticação)
```

**Teste Rápido:**

```
1. Clique no ícone Spark
2. Digite: "Hello Claude! What is 2+2?"
3. Claude deve responder: "2+2 equals 4"
```

Se funcionou: ✅ **Instalação completa!**  
Se vir erro de autenticação: ⏮️ Volte ao Passo 2, método de chave de API

---

## AULA 3 — Sua Primeira Conversa Produtiva

### Entender o Painel de Claude Code

**Objetivos da Aula:**
- Navegar pela interface do Claude Code
- Diferenciar modos de interação (chat vs. edit)
- Usar contexto de arquivo para melhorar respostas

**Habilidades Esperadas:**
- Capacidade de referenciar trechos de código em prompts
- Compreensão de como Claude Code acessa o arquivo aberto
- Saber quando usar "Ask Claude" vs. "Edit Code"

---

### Anatomia da Interface

**📸 Sugestão de Print 1:** Painel Claude Code com projeto aberto mostrando:
- Chat history à esquerda
- Input field no fundo
- Botões de ação (Create, Edit, etc.)

```
┌─────────────────────────────────────────────────────────┐
│ Claude Code Painel                                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Chat History (Conversas Anteriores)                   │
│  ├─ "Help me refactor this function"                  │
│  ├─ "Write tests for login module"                    │
│  └─ "Explain this error"                              │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  [Input Field para nova pergunta]                       │
│  [⚙️ Settings] [🔄 New Chat] [📌 Pin]                  │
└─────────────────────────────────────────────────────────┘
```

---

### Primeira Pergunta: Contexto É Tudo

#### Cenário: Você tem um arquivo Python aberto

**Arquivo: `utils.py`**

```python
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item['price']
    return total
```

**❌ Pergunta Ruim (sem contexto):**
```
"Como melhorar essa função?"
```

Claude responde genericamente, sem saber qual função você quer melhorar.

---

**✅ Pergunta Boa (com contexto):**

```
"Vejo que tenho uma função calculate_total() no arquivo aberto.
Ela itera um dicionário e soma preços. 
Sugira uma versão mais Pythônica usando sum() e list comprehension.
Não faça a mudança ainda, só mostre o código novo em um bloco de código."
```

Claude **vê** a função aberta, **entende** o contexto, e **responde especificamente**.

---

### Prática Guiada: Primeira Tarefa Real

**Setup:**

1. Abra VS Code
2. Crie um arquivo chamado `demo.py`:

```python
def greet(name):
    message = "Hello, " + name + "!"
    print(message)
    return message

# Teste
greet("Alice")
```

**Tarefa 1: Pedir Explicação**

```
Pergunta para Claude Code:
"Vejo que tenho uma função greet() que concatena strings.
Quero entender se há forma mais eficiente ou Pythônica de fazer isso.
Explique as alternativas disponíveis em Python."
```

**📸 Sugestão de Print 2:** Resposta do Claude no painel mostrando:
- Explicação sobre f-strings vs concatenação
- Exemplo com f-strings
- Exemplo com .format()

**Tarefa 2: Pedir Plano Antes de Editar**

```
Pergunta para Claude Code:
"Baseado na sua resposta, mostre-me o PLANO de mudanças
que você faria na função greet(). Não edite o código ainda,
apenas liste os passos: 
1. Trocar concatenação por f-string
2. Considerar type hints
3. ..."
```

**Tarefa 3: Aceitar ou Rejeitar Mudança**

```
Pergunta para Claude Code:
"OK, vá em frente e refatore a função usando f-strings e type hints."
```

Ele mostrará um **diff** lado a lado (antes/depois). Você **revisa e aprova**.

**📸 Sugestão de Print 3:** Diff viewer mostrando mudanças lado a lado com botões "Accept" / "Reject"

---

### Atalhos Essenciais

| Ação | Atalho Windows | Atalho Mac |
|------|---|---|
| Abrir Claude Code | Ctrl + Shift + C | Cmd + Shift + C |
| Paleta de Comandos | Ctrl + Shift + P | Cmd + Shift + P |
| Procurar arquivo | Ctrl + P | Cmd + P |
| Selecionar linhas | Clique + Shift | Clique + Shift |
| Nova chat session | Via menu Claude Code | Via menu Claude Code |

---

## AULA 4 — Contexto de Projeto: O Superpoder do Claude Code

### Usando Arquivos Abertos Como Contexto

**Objetivos da Aula:**
- Aproveitar contexto automático de arquivos abertos
- Usar `@filename` para referenciar explicitamente
- Construir prompts que levam em conta estrutura do projeto

**Habilidades Esperadas:**
- Saber quais arquivos Claude vê (abertos + selecionados)
- Capacidade de criar prompts multi-arquivo
- Decisão: quando copiar código vs. usar referência

---

### O Que Claude Code Pode "Ver"

```markdown
✅ Claude Code acessa automaticamente:
1. Arquivo aberto no editor (o conteúdo completo)
2. Seleção (se você selecionar linhas específicas)
3. Símbolos do arquivo (funções, classes, imports)

❌ Claude Code NÃO acessa automaticamente:
1. Arquivos não abertos (mesmo no projeto)
2. Histórico Git
3. Variáveis de ambiente ou secrets
4. Dependências instaladas (node_modules, venv)
```

---

### Sintaxe `@mention` para Referências Explícitas

**Formato:**

```
No seu prompt, use @filename para referenciar arquivo específico:

"Estou trabalhando em @api.py e preciso chamar uma função de @utils.py.
Como fazer import correto?"
```

**Limitações:**
- Só funciona com arquivos que você abre
- Recomendado para projetos com <5 arquivos principais
- Para projetos grandes, considere CLI com path completo

---

### Caso de Uso: Refatoração Multi-Arquivo

**Cenário Real:**

Você tem um projeto estruturado:

```
projeto/
├── models.py       (Modelos de dados)
├── services.py     (Lógica de negócio)
├── api.py          (Rotas e endpoints)
└── tests/
    └── test_api.py (Testes unitários)
```

**Tarefa:** Adicionar novo campo `email` ao modelo User e fazer mudanças cascata.

**Passo 1: Abrir Arquivos Relevantes**

```
1. Abra models.py (mostra classe User atual)
2. Abra services.py (mostra onde User é usado)
3. Abra api.py (mostra endpoints que retornam User)
```

**📸 Sugestão de Print 1:** VS Code com 3 abas abertas, visíveis ao usuário

**Passo 2: Formular Pergunta Contextualizada**

```
"Vejo que tenho 3 arquivos abertos:
- @models.py com classe User(id, name, phone)
- @services.py com função get_user(id) que retorna User
- @api.py com endpoint GET /user/<id> que usa get_user()

Preciso adicionar campo 'email' ao User. 
Mostre-me PLANO de mudanças necessárias em cada arquivo.
Não faça edições ainda."
```

Claude analisará os 3 arquivos e dirá:

```
Plano:
1. models.py: Adicionar email: str = "" ao __init__ de User
2. services.py: Atualizar get_user() para retornar email (se BD tiver)
3. api.py: Endpoint já retorna User completo, sem mudança
4. tests/test_api.py: Adicionar teste com email preenchido
```

**Passo 3: Executar Mudanças Sequencialmente**

```
Pergunta 1: "Refatore @models.py para adicionar email"
Pergunta 2: "Refatore @services.py para incluir email"
Pergunta 3: "Gere testes para @test_api.py cobrindo cenário com email"
```

Você revisa e aceita cada um.

**📸 Sugestão de Print 2:** Histórico de chat mostrando 3 perguntas, cada uma afetando arquivo diferente

---

### Boas Práticas: Quando Usar Contexto Automático vs. Explícito

| Situação | Abordagem | Por quê |
|----------|-----------|--------|
| 1 arquivo, pergunta pontual | Automático (arquivo aberto) | Simples e rápido |
| 2-3 arquivos relacionados | Automático + @mention | Deixa claro qual arquivo |
| Projeto inteiro (10+ arquivos) | CLI com path ou Chat web | Mais controle do contexto |
| Arquivo muito grande (10k linhas) | Selecionar trecho específico | Reduce noise no prompt |
| Análise de dependências | Chat web + upload | Melhor para overview |

---

## AULA 5 — Refatoração: Melhorando Código Existente

### Pattern: Ask → Plan → Review → Accept

**Objetivos da Aula:**
- Executar refatoração com segurança
- Revisar diffs antes de aceitar
- Aprender padrões de bom refactoring

**Habilidades Esperadas:**
- Capacidade de descrever problema a refatorar
- Compreensão de diff viewer
- Decisão: aceitar, rejeitar ou pedir ajustes

---

### Caso de Uso 1: Simplificar Lógica Complexa

**Arquivo: `validators.py`**

```python
def is_valid_email(email):
    if email is None:
        return False
    if email == "":
        return False
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True
```

**Problema:** Código com muitos `if` aninhados. Difícil de ler.

**Passo 1: Pedir Análise**

```
"Vejo que tenho uma função is_valid_email() com múltiplos ifs.
Analise e sugira forma mais concisa e Pythônica.
Mostre a versão melhorada em um bloco de código, mas não faça
mudança no arquivo ainda."
```

Claude sugere:

```python
def is_valid_email(email):
    if not email or "@" not in email:
        return False
    local, domain = email.split("@", 1)
    return "." in domain and local and domain
```

**Passo 2: Pedir Plano Detalhado**

```
"Antes de você fazer a mudança, explique:
1. O que mudou na lógica?
2. Há casos que a nova versão trata diferente?
3. Há trade-offs (ex: performance vs. readability)?"
```

Claude detalha:

```
Mudanças:
1. Combinou primeiros 2 ifs em um (email pode ser None ou "")
2. Usa split() com maxsplit=1 para evitar erro se houver múltiplos @
3. Valida domain corretamente

Trade-off:
- Novo código é mais conciso (melhor para manutenção)
- Mas depende de compreensão de split() e boolean short-circuit
  (menos explícito para iniciante)
```

**Passo 3: Aceitar e Revisar Diff**

```
"OK, faça a refatoração em is_valid_email()."
```

Claude mostra **diff viewer**:

```diff
- def is_valid_email(email):
-     if email is None:
-         return False
-     if email == "":
-         return False
+ def is_valid_email(email):
+     if not email or "@" not in email:
+         return False
-     if "@" not in email:
-         return False
-     if "." not in email.split("@")[1]:
-         return False
+     local, domain = email.split("@", 1)
+     return "." in domain and local and domain
```

**📸 Sugestão de Print 1:** Diff viewer com cores (vermelho/verde) mostrando antes/depois

**Passo 4: Aceitar Mudança**

Clique "Accept" e arquivo é atualizado.

---

### Caso de Uso 2: Remover Duplicação

**Arquivo: `handlers.py`**

```python
def handle_user_signup(data):
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    
    if not name or not email or not phone:
        return {"error": "Missing fields"}
    
    return save_user(name, email, phone)

def handle_admin_signup(data):
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    role = data.get('role', 'viewer').strip()
    
    if not name or not email or not role:
        return {"error": "Missing fields"}
    
    return save_admin(name, email, role)
```

**Problema:** Código repetido em múltiplas funções (pattern extraction).

**Pergunta:**

```
"Vejo duplicação entre handle_user_signup() e handle_admin_signup().
Ambas validam e extraem dados de forma similar.

Sugira uma forma de refatorar para eliminar duplicação usando:
1. Uma função utilitária de validação compartilhada
2. Ou usando decorator
3. Ou outra abordagem que você considere melhor

Mostre o código refatorado. Não aplique ainda."
```

Claude propõe:

```python
def validate_and_extract(data, required_fields):
    """Extrair e validar campos obrigatórios."""
    extracted = {}
    for field in required_fields:
        value = data.get(field, '').strip()
        if not value:
            return None, {"error": f"Missing field: {field}"}
        extracted[field] = value
    return extracted, None

def handle_user_signup(data):
    extracted, error = validate_and_extract(data, ['name', 'email', 'phone'])
    if error:
        return error
    return save_user(**extracted)

def handle_admin_signup(data):
    extracted, error = validate_and_extract(data, ['name', 'email', 'role'])
    if error:
        return error
    return save_admin(**extracted)
```

**Vantagens:**
- ✅ Menos código repetido
- ✅ Mesma lógica de validação em um lugar
- ✅ Fácil de estender (adicionar novo campo)

---

### Padrão de Refatoração: 5-Step Protocol

**Sempre siga este padrão para refatoração segura:**

```markdown
1. ASK: "Analise [função]. Sugira melhorias em [aspecto específico]."
2. EXPLAIN: "Explique o trade-off entre seu código e o original."
3. PLAN: "Liste os passos exatos que vai fazer."
4. DIFF: "Mostre a mudança lado a lado (não aplique)."
5. ACCEPT/REJECT: "Vou aceitar" ou "Pode refatorar diferente?"
```

Se você **rejeitar** em algum passo, Claude propõe alternativa sem perder contexto.

---

## AULA 6 — Geração de Testes Unitários

### Test-Driven Development com Claude Code

**Objetivos da Aula:**
- Usar Claude para gerar testes baseado em código existente
- Entender cobertura de casos (happy path, edge cases)
- Integrar testes ao seu fluxo de trabalho

**Habilidades Esperadas:**
- Capacidade de descrever cenários de teste
- Compreensão de frameworks de teste (unittest, pytest, Jest)
- Revisar testes gerados e adaptar conforme necessário

---

### Caso de Uso 1: Função Python com Pytest

**Arquivo: `math_ops.py`**

```python
def factorial(n):
    """Retorna n!"""
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

**Passo 1: Pedir Testes**

```
"Tenho função factorial(n) que calcula fatorial.
Gere testes unitários usando pytest que cubram:
1. Caso normal (n=5)
2. Casos extremos (n=0, n=1)
3. Erro de entrada negativa
4. Tipo incorreto (ex: string)

Crie arquivo test_math_ops.py com esses testes."
```

Claude gera:

```python
import pytest
from math_ops import factorial

def test_factorial_normal():
    assert factorial(5) == 120
    assert factorial(4) == 24

def test_factorial_edge_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_invalid_type():
    with pytest.raises(TypeError):
        factorial("5")
```

**📸 Sugestão de Print 1:** Arquivo `test_math_ops.py` aberto mostrando testes gerados

**Passo 2: Executar Testes**

```bash
# No terminal integrado do VS Code
pytest test_math_ops.py -v

# Resultado:
# test_math_ops.py::test_factorial_normal PASSED
# test_math_ops.py::test_factorial_edge_cases PASSED
# test_math_ops.py::test_factorial_negative PASSED
# test_math_ops.py::test_factorial_invalid_type PASSED
# 
# ============ 4 passed in 0.23s ============
```

**📸 Sugestão de Print 2:** Terminal mostrando output de `pytest` com testes passando

**Passo 3: Cobertura de Código**

```bash
# Instalar cobertura (uma vez)
pip install pytest-cov

# Executar com relatório de cobertura
pytest test_math_ops.py --cov=math_ops --cov-report=html

# Resultado:
# Name          Stmts   Miss  Cover
# math_ops.py       9      0   100%
# Total             9      0   100%
```

100% de cobertura = todas as linhas são testadas.

---

### Caso de Uso 2: Função JavaScript com Jest

**Arquivo: `utils.js`**

```javascript
function calculateDiscount(price, customerType) {
  const discounts = {
    regular: 0,
    member: 0.1,
    vip: 0.2
  };
  
  if (!discounts.hasOwnProperty(customerType)) {
    throw new Error("Invalid customer type");
  }
  
  return price * (1 - discounts[customerType]);
}

module.exports = calculateDiscount;
```

**Pergunta:**

```
"Gere testes com Jest para função calculateDiscount().
Cobertura: preço normal, todos tipos de cliente, tipo inválido.
Arquivo: utils.test.js"
```

Claude gera:

```javascript
const calculateDiscount = require('./utils');

describe('calculateDiscount', () => {
  it('should apply 0% discount for regular customers', () => {
    expect(calculateDiscount(100, 'regular')).toBe(100);
  });

  it('should apply 10% discount for members', () => {
    expect(calculateDiscount(100, 'member')).toBe(90);
  });

  it('should apply 20% discount for VIP', () => {
    expect(calculateDiscount(100, 'vip')).toBe(80);
  });

  it('should throw error for invalid customer type', () => {
    expect(() => calculateDiscount(100, 'invalid')).toThrow('Invalid customer type');
  });
});
```

**Executar:**

```bash
npm test utils.test.js

# PASS  utils.test.js
# ✓ should apply 0% discount for regular customers
# ✓ should apply 10% discount for members
# ✓ should apply 20% discount for VIP
# ✓ should throw error for invalid customer type
```

---

### Padrão: Arrange-Act-Assert (AAA)

Bons testes seguem padrão AAA:

```python
def test_example():
    # ARRANGE: Preparar dados
    input_data = {"name": "Alice", "age": 30}
    
    # ACT: Executar função
    result = process_user(input_data)
    
    # ASSERT: Verificar resultado
    assert result["greeting"] == "Hello, Alice!"
    assert result["is_adult"] == True
```

Claude Code segue este padrão automaticamente. Se não seguir, você pode pedir:

```
"Refatore os testes para usar padrão Arrange-Act-Assert."
```

---

### Checklist: Testes de Qualidade

Antes de aceitar testes gerados, verifique:

```markdown
- [ ] Cobre happy path (entrada válida normal)
- [ ] Cobre edge cases (n=0, lista vazia, None)
- [ ] Cobre erros esperados (exception handling)
- [ ] Cobre casos de limite (muito grande, muito pequeno)
- [ ] Nome dos testes descreve claramente o que testam
- [ ] Usa asserts específicas (não genéricas)
- [ ] Tempo de execução razoável (<0.1s por teste)
```

Se algum falta, peça:

```
"Adicione teste para cenário X (edge case)."
```

---

## AULA 7 — Documentação Automática de Código

### Gerando Docstrings e README

**Objetivos da Aula:**
- Usar Claude para criar documentação de alta qualidade
- Entender diferentes estilos de docstring (Google, NumPy, RST)
- Documentar API automática

**Habilidades Esperadas:**
- Capacidade de indicar estilo de documentação preferido
- Revisão crítica de documentação gerada
- Integração com ferramentas de docs (Sphinx, MkDocs)

---

### Caso de Uso 1: Docstring em Python (Google Style)

**Arquivo: `data_processor.py`**

```python
def normalize_dataset(df, columns=None, method='zscore'):
    if columns is None:
        columns = df.columns
    
    if method == 'zscore':
        return (df[columns] - df[columns].mean()) / df[columns].std()
    elif method == 'minmax':
        return (df[columns] - df[columns].min()) / (df[columns].max() - df[columns].min())
    else:
        raise ValueError(f"Unknown method: {method}")
```

**Pergunta:**

```
"Função normalize_dataset() em @data_processor.py carece de documentação.
Adicione docstring em estilo Google que inclua:
1. Descrição clara do que faz
2. Args com tipo e descrição
3. Returns com tipo
4. Raises para exceções
5. Exemplo de uso

Não aplique mudança ainda, mostre a docstring."
```

Claude gera:

```python
def normalize_dataset(df, columns=None, method='zscore'):
    """Normaliza colunas de DataFrame usando técnica especificada.
    
    Aplica normalização estatística a colunas selecionadas de um DataFrame.
    Suporta Z-score (padronização) e Min-Max (normalização 0-1).
    
    Args:
        df (pd.DataFrame): DataFrame com dados a normalizar.
        columns (list, optional): Lista de colunas a normalizar.
            Se None, normaliza todas. Padrão: None.
        method (str, optional): Técnica de normalização.
            - 'zscore': (x - mean) / std
            - 'minmax': (x - min) / (max - min)
            Padrão: 'zscore'.
    
    Returns:
        pd.DataFrame: Colunas normalizadas. Outras colunas mantidas.
    
    Raises:
        ValueError: Se method não está em ['zscore', 'minmax'].
        KeyError: Se coluna especificada não existe em df.
    
    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
        >>> normalized = normalize_dataset(df, columns=['A'])
        >>> normalized['A'].mean()
        0.0
        >>> normalized['A'].std()
        1.0
    """
```

**📸 Sugestão de Print 1:** Função com docstring completa em VS Code

---

### Caso de Uso 2: README.md para Projeto

**Estrutura do Projeto:**

```
meu_projeto/
├── src/
│   ├── models.py
│   ├── processors.py
│   └── api.py
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md (vazio ou falta)
```

**Pergunta:**

```
"Gere um README.md profissional para meu projeto.
Inclua:
1. Título e descrição (1-2 linhas)
2. Requisitos (Python 3.8+, pandas, flask)
3. Instalação (passo a passo)
4. Uso (exemplos de código)
5. Estrutura de pastas
6. Contribuindo
7. Licença"
```

Claude gera:

```markdown
# Meu Projeto

Processador de dados com API REST para normalização estatística.

## Requisitos

- Python 3.8+
- pandas >= 1.3.0
- flask >= 2.0.0

## Instalação

```bash
git clone https://github.com/seu-usuario/meu-projeto.git
cd meu-projeto
pip install -r requirements.txt
```

## Uso

### Como biblioteca

```python
from src.processors import normalize_dataset
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]})
normalized = normalize_dataset(df, method='zscore')
```

### Como API

```bash
python -m src.api
# Servidor rodando em http://localhost:5000

curl -X POST http://localhost:5000/normalize \
  -H "Content-Type: application/json" \
  -d '{"data": [1, 2, 3], "method": "zscore"}'
```

## Estrutura do Projeto

```
meu_projeto/
├── src/
│   ├── models.py       - Estruturas de dados
│   ├── processors.py   - Funções de processamento
│   └── api.py          - Endpoints Flask
├── tests/              - Testes unitários
└── README.md           - Este arquivo
```

## Contribuindo

1. Faça fork
2. Crie branch para feature (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Abra Pull Request

## Licença

MIT - veja LICENSE para detalhes
```

**📸 Sugestão de Print 2:** Arquivo README.md renderizado mostrando formatação Markdown completa

---

### Caso de Uso 3: Comentários Inline para Lógica Complexa

**Arquivo: `algorithm.py`**

```python
def optimize_path(graph, start, end):
    visited = set()
    queue = [(start, [start])]
    
    while queue:
        node, path = queue.pop(0)
        
        if node == end:
            return path
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None
```

**Pergunta:**

```
"Função optimize_path() implementa BFS (Breadth-First Search).
O código é correto mas pouco comentado. Adicione:
1. Comentário de docstring explicando algoritmo
2. Inline comments explicando cada seção (initialization, loop, etc.)
3. Comentário sobre complexidade (time/space)"
```

Claude refatora:

```python
def optimize_path(graph, start, end):
    """Encontra caminho mais curto entre nós usando BFS.
    
    Implementa algoritmo Breadth-First Search que explora
    nós camada por camada, garantindo menor número de passos.
    
    Complexidade:
    - Tempo: O(V + E) onde V=vértices, E=arestas
    - Espaço: O(V) para fila e conjunto visited
    """
    # Rastrear nós já explorados
    visited = set()
    # Fila de (nó_atual, caminho_até_aqui)
    queue = [(start, [start])]
    
    # BFS: processar nós por nível
    while queue:
        node, path = queue.pop(0)
        
        # Checagem de sucesso: chegou no destino
        if node == end:
            return path
        
        # Skip se já visitado (evita ciclos)
        if node in visited:
            continue
        
        visited.add(node)
        
        # Adicionar vizinhos não-visitados à fila
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    # Sem caminho encontrado
    return None
```

---

### Integração com Gerador de Docs (Sphinx)

Para projetos maiores com Sphinx:

```bash
# Estrutura esperada
projeto/
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── api.rst
├── src/
│   └── mymodule.py
└── requirements-docs.txt
```

**Pergunta ao Claude Code:**

```
"Gere arquivo docs/api.rst que documenta módulo @mymodule.py
usando automodule directive do Sphinx.
Mostre como incluir em docs/index.rst para gerar HTML."
```

Claude gera documentação que se integra ao seu fluxo de docs automaticamente.

---

## AULA 8 — Debugging com Claude Code

### Usar IA para Diagnosticar Erros

**Objetivos da Aula:**
- Descrever erro/stack trace para Claude
- Usar Claude para debugar código
- Entender quando usar debugger vs. Claude Code

**Habilidades Esperadas:**
- Capacidade de coletar informações de erro (stack trace, logs)
- Hipóteses de debugging
- Reproduzir erro em contexto fornecido

---

### Caso de Uso 1: Exception with Stack Trace

**Cenário:**

Seu código levanta exceção:

```
Traceback (most recent call last):
  File "app.py", line 45, in process_data
    result = calculate(data['value'])
  File "math_ops.py", line 12, in calculate
    return data / (data - threshold)
ZeroDivisionError: division by zero
```

**❌ Pergunta Vaga:**

```
"Meu código está com erro. Como fix?"
```

Claude não sabe qual erro.

---

**✅ Pergunta Boa:**

```
"Tenho ZeroDivisionError em @math_ops.py linha 12.
Stack trace:
```
ZeroDivisionError: division by zero
  File "math_ops.py", line 12, in calculate
    return data / (data - threshold)
```

A função calculate(data) deveria sempre funcionar mesmo se
data == threshold. Qual é o problema e como fix?"
```

Claude vê contexto claro:

1. Lê `calculate()` em math_ops.py
2. Identifica: `data - threshold` pode ser zero
3. Sugere: adicionar guarda contra divisão por zero

---

### Caso de Uso 2: Logic Error (Sem Exception)

**Cenário:**

Código roda mas resultado está errado:

```python
# Em data_processor.py
def filter_users(users, min_age=18):
    result = []
    for user in users:
        if user['age'] > min_age:
            result.append(user)
    return result

# Teste
users = [
    {'name': 'Alice', 'age': 17},
    {'name': 'Bob', 'age': 18},
    {'name': 'Charlie', 'age': 20}
]

adults = filter_users(users)
# Esperado: [Bob, Charlie] (age >= 18)
# Real: [Charlie] (age > 18)
```

**Pergunta:**

```
"Função filter_users() em @data_processor.py filtra por min_age.
Esperado: retorna usuários com age >= min_age (inclusive).
Real: retorna apenas age > min_age (exclusive).

Problema: deve ser >= não >.
Corrija."
```

Claude identifica e corrige:

```python
if user['age'] >= min_age:  # Mudou de > para >=
    result.append(user)
```

**📸 Sugestão de Print 1:** Diff mostrando mudança de `>` para `>=`

---

### Caso de Uso 3: Performance Issue

**Cenário:**

Código funciona mas é lento:

```python
def find_duplicates(items):
    """Encontra itens duplicados (O(n²))."""
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**Problema:** O(n²) é lento para listas grandes.

**Pergunta:**

```
"Função find_duplicates() em @data_processor.py usa nested loops (O(n²)).
Para listas com 100k itens, fica muito lento.

Sugira versão mais eficiente usando set ou dict."
```

Claude refatora para O(n):

```python
def find_duplicates(items):
    """Encontra duplicados em O(n)."""
    seen = set()
    duplicates = []
    
    for item in items:
        if item in seen:
            if item not in duplicates:  # Evitar duplicatas na resposta
                duplicates.append(item)
        else:
            seen.add(item)
    
    return duplicates
```

**Benchmark:**

```python
import time

items = list(range(100_000)) * 2  # 200k items com duplicatas

# Old (O(n²))
start = time.time()
result_old = find_duplicates_old(items)
print(f"Old: {time.time() - start:.2f}s")  # ~5 segundos

# New (O(n))
start = time.time()
result_new = find_duplicates_new(items)
print(f"New: {time.time() - start:.2f}s")  # ~0.01 segundos
```

**50x mais rápido!**

---

### Debugging Checklist

Quando seu código tem problema:

```markdown
1. [ ] Tenho stack trace completo? (copie do terminal)
2. [ ] Arquivo está aberto em VS Code? (Claude vê contexto)
3. [ ] Forneci input mínimo para reproduzir? (ex: dados de teste)
4. [ ] Descrevi o resultado esperado vs. real?
5. [ ] Verifiquei se é exception vs. logic error vs. performance?
```

Se tiver tudo, pergunte ao Claude Code.

---

## AULA 9 — Automação: Scripts e Tasks

### Gerar Scripts Auxiliares

**Objetivos da Aula:**
- Usar Claude para criar scripts de automação
- Integrar scripts no seu workflow (Makefile, npm scripts)
- Tratamento de erros em scripts

**Habilidades Esperadas:**
- Escrita de bash/Python scripts
- Entender quando automação é necessária
- Manutenção de scripts gerados

---

### Caso de Uso 1: Makefile para Tarefas Comuns

**Projeto Python:**

```
projeto/
├── src/
├── tests/
├── Makefile
└── requirements.txt
```

**Pergunta:**

```
"Gere um Makefile que automatize tarefas comuns:
1. install: instalar dependências
2. test: rodar testes com cobertura
3. lint: verificar qualidade (black, pylint)
4. format: formatar código
5. clean: remover arquivos temporários
6. docs: gerar documentação com Sphinx

Formato: make test, make lint, etc."
```

Claude gera:

```makefile
.PHONY: install test lint format clean docs help

help:
	@echo "Tarefas disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instalar dependências
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test: ## Rodar testes com cobertura
	pytest tests/ -v --cov=src --cov-report=html
	@echo "✓ Cobertura disponível em htmlcov/index.html"

lint: ## Verificar qualidade de código
	black --check src/ tests/
	pylint src/
	mypy src/

format: ## Formatar código
	black src/ tests/
	isort src/ tests/

clean: ## Limpar arquivos temporários
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache/ htmlcov/ .mypy_cache/
	rm -rf dist/ build/ *.egg-info/

docs: ## Gerar documentação
	cd docs && make html
	@echo "✓ Documentação em docs/_build/html/index.html"
```

**Uso:**

```bash
make install   # Instala tudo
make test      # Roda testes
make lint      # Verifica qualidade
make clean     # Limpa cache

make help      # Lista tudo
```

**📸 Sugestão de Print 1:** Terminal exibindo `make help` com lista de tarefas

---

### Caso de Uso 2: Deploy Script

**Arquivo: `deploy.sh`**

**Pergunta:**

```
"Gere script deploy.sh que:
1. Verifica se branch é main (evita deploy de feature branches)
2. Roda testes (fail if not pass)
3. Faz build (ex: npm run build para Node)
4. Deploy para staging
5. Notifica sucesso/erro

Inclua tratamento de erros com 'set -e'."
```

Claude gera:

```bash
#!/bin/bash
set -e  # Exit se qualquer comando falhar

BRANCH=$(git rev-parse --abbrev-ref HEAD)
ENVIRONMENT="${1:-staging}"

echo "🚀 Deploy Script"
echo "Branch: $BRANCH"
echo "Ambiente: $ENVIRONMENT"

# Verificar branch
if [ "$BRANCH" != "main" ] && [ "$ENVIRONMENT" = "production" ]; then
    echo "❌ Erro: Só deploy para produção a partir de 'main'"
    exit 1
fi

# Rodar testes
echo "🧪 Rodando testes..."
npm test

# Build
echo "🔨 Build em progresso..."
npm run build

# Deploy
echo "📦 Enviando para $ENVIRONMENT..."
case $ENVIRONMENT in
    staging)
        npm run deploy:staging
        ;;
    production)
        npm run deploy:prod
        ;;
    *)
        echo "❌ Ambiente inválido"
        exit 1
        ;;
esac

echo "✅ Deploy completo!"
```

**Uso:**

```bash
chmod +x deploy.sh
./deploy.sh staging      # Deploy para staging
./deploy.sh production   # Deploy para produção
```

---

### Caso de Uso 3: Git Hooks com Claude

**Problema:** Developers commitam código sem rodar testes primeiro.

**Solução:** Pre-commit hook que roda testes automaticamente.

**Pergunta:**

```
"Gere .git/hooks/pre-commit que:
1. Roda testes
2. Verifica linting
3. Bloqueia commit se falhar
4. Mostra tempo de execução

Salve em arquivo chamado pre-commit-hook.sh"
```

Claude gera:

```bash
#!/bin/bash
echo "🔍 Pre-commit check..."

START=$(date +%s)

# Testes
echo "  Testing..."
npm test --bail || {
    echo "❌ Testes falharam. Commit abortado."
    exit 1
}

# Lint
echo "  Linting..."
npm run lint || {
    echo "❌ Lint errors. Commit abortado."
    exit 1
}

END=$(date +%s)
DURATION=$((END - START))

echo "✅ Tudo OK! ($DURATION segundos)"
exit 0
```

**Instalação:**

```bash
cp pre-commit-hook.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Agora, `git commit` automaticamente roda testes.

**📸 Sugestão de Print 2:** Terminal mostrando output de pre-commit hook durante commit

---

## AULA 10 — Segurança de Dados e Compliance

### O Que Não Enviar para Claude Code

**Objetivos da Aula:**
- Identificar dados sensíveis
- Entender política de retenção de dados Anthropic
- Configurar Claude Code para ambientes regulados

**Habilidades Esperadas:**
- Classificação de dados (público vs. privado vs. sensível)
- Decisão: usar Claude Code vs. alternativas
- Documentação de uso de IA em projeto

---

### Classificação de Dados

```markdown
🟢 SEGURO enviar para Claude:
✅ Código aberto ou não-sensível
✅ Exemplos didáticos
✅ Estrutura de projeto (nomes de pastas, imports)
✅ Erros de sintaxe e stack traces (sem dados)
✅ Explicações de conceitos

🟡 CUIDADO com:
⚠️ Dados de cliente (nomes, emails, phones)
⚠️ Logs contendo PII (Personally Identifiable Info)
⚠️ Configurações com secrets (API keys)
⚠️ Dados de negócio sensível
⚠️ Propriedade intelectual

🔴 NUNCA enviar:
❌ Senhas, tokens, API keys
❌ Números de Documento (RG, CPF, Passaporte)
❌ Dados financeiros (CC, IBAN, etc.)
❌ Informações médicas (HIPAA, sensível)
❌ Dados pessoais de terceiros sem consentimento
```

---

### Exemplo: Remover Dados Sensíveis de Stack Trace

**❌ Stack Trace com Sensibilidades:**

```python
Traceback (most recent call last):
  File "auth.py", line 34, in login
    user = db.query(User).filter(email='alice@company.com').first()
  File "db.py", line 12, in query
    return session.query(model)
KeyError: 'alice@company.com'
```

**Problema:** Email está exposto. Não envie assim para Claude.

---

**✅ Stack Trace Sanitizado:**

```python
Traceback (most recent call last):
  File "auth.py", line 34, in login
    user = db.query(User).filter(email=email).first()
  File "db.py", line 12, in query
    return session.query(model)
KeyError: 'user_email'
```

**Melhor:** Dados específicos foram removidos, lógica é clara.

---

### Caso de Uso: Verificar Arquivo Antes de Enviar

**Workflow:**

```markdown
1. Abra arquivo em VS Code
2. Antes de fazer pergunta ao Claude Code:
   - Scan rápido: há strings com números, emails, senhas?
   - Se SIM: remova ou generalize
   - Se NÃO: safe para compartilhar

3. Pergunta é OK? Envie.
4. Documentar: "Usei Claude Code em auth.py para debugar erro de login."
```

---

### Integração com Política de Dados (LGPD/GDPR)

Se seu projeto processa dados de usuários europeus:

```markdown
LGPD (Lei Geral de Proteção de Dados - Brasil):
- Dados pessoais não devem sair do Brasil sem consentimento
- Solução: Use Claude Desktop CLI local ou considere alternativas

GDPR (Europa):
- Dados de EU citizens têm proteção máxima
- Ao usar Claude Code, você envia dados para Anthropic (USA)
- Anthropic tem Data Processing Agreement (DPA) disponível
- Recomendação: Obtenha consentimento ou use alternativas locais
```

**Melhor Prática:**

Documenta em seu projeto:

```markdown
# Data Privacy Policy

## Uso de Claude Code

Claude Code (VS Code extension) é usado apenas para:
- Debugging de erros de sintaxe
- Refatoração de código
- Geração de testes

Dados enviados para Anthropic:
- Trecho de código (nunca dados de usuários)
- Stack traces

Dados NÃO enviados:
- Informações de usuários (PII)
- Dados sensíveis do negócio
```

---

### Auditoria: Revisar Histórico de Conversas

Seu histórico de conversas com Claude Code fica salvo em:

```
Windows: %USERPROFILE%\.anthropic\
Mac:     ~/.anthropic/
Linux:   ~/.anthropic/
```

**Antes de fazer login em máquina compartilhada:**

```bash
# Verificar histórico
ls ~/.anthropic/  # Ver quais conversas estão salvas

# Limpar histórico (se necessário)
rm -rf ~/.anthropic/  # Remove tudo
```

**Boas Práticas:**

```markdown
- [ ] Máquina pessoal: pode deixar histórico
- [ ] Máquina compartilhada (lab): limpe histórico ao sair
- [ ] Máquina corporativa: siga política TI
- [ ] Máquina pública: NUNCA faça login
```

---

## AULA 11 — Integração Avançada: MCP e Contexto Expandido

### Model Context Protocol (MCP): Expandindo Poderes do Claude

**Objetivos da Aula:**
- Entender o que é MCP
- Integrar MCP com Claude Code
- Casos de uso para Engenharia

**Habilidades Esperadas:**
- Conhecimento de MCPs disponíveis
- Habilidade de ativar/configurar MCP
- Uso de contexto MCP em prompts

---

### O Que é MCP?

MCP (Model Context Protocol) permite Claude acessar ferramentas e dados externos:

```
Claude Code
    ↓
  MCP
    ↓
┌─────────────────────┐
├─ Git (repository)   ├─ Acessar histórico, branches
├─ GitHub API        ├─ Issues, PRs, commits
├─ Databases        ├─ SQL queries
├─ APIs Custom      ├─ Sua API interna
└─────────────────────┘
```

**Exemplos:**

```markdown
📚 Git MCP: "Quais commits afetaram esse arquivo?"
🐙 GitHub MCP: "Liste issues abertas para mim"
💾 SQL MCP: "Consulte schema da tabela users"
🔌 Custom MCP: "Puxe últimas métricas de performance"
```

---

### Caso de Uso 1: Git MCP — Análise de Histórico

**Setup:** Você tem MCP de Git ativado.

**Arquivo: `legacy_module.py` (muito antigo)**

**Pergunta:**

```
"Analise histórico de @legacy_module.py usando Git MCP.
1. Quem foi último a editar?
2. Quando foi última mudança?
3. Quais 3 últimos commits afetaram isso?
4. Há comments em commits?"
```

Claude consulta Git e retorna:

```
Histórico de legacy_module.py:

Última edição: 2023-10-15 por @alice
Último commit: "Refactor legacy module for perf"

3 últimos commits:
1. e7a3f2d (2023-10-15) Refactor legacy module - Alice
   "Removed deprecated function, updated docstrings"

2. 9c2e1f4 (2023-08-20) Fix bug in calculate_total() - Bob
   "Fixed off-by-one error in loop"

3. 5d1c8a9 (2023-06-10) Initial commit - Charlie
   "Add legacy module from old codebase"
```

**Insight:** Arquivo foi tocado 3 vezes em 4 meses. Pode ser candidato a refatoração/deprecation.

---

### Caso de Uso 2: GitHub MCP — Gerenciar Issues

**Setup:** Você tem MCP de GitHub ativado.

**Pergunta:**

```
"Use GitHub MCP para:
1. Listar issues abertas com label 'bug'
2. Criar issue nova: 'Refactor legacy_module.py for performance'
3. Linkar issue ao PR existente"
```

Claude interage com GitHub:

```
Criada issue #234:
Title: Refactor legacy_module.py for performance
Body: Histórico Git mostra que módulo foi tocado 3 vezes 
      em 4 meses, indicando complexidade...
Labels: enhancement, performance
```

Agora você não precisa sair do VS Code para gerenciar GitHub.

---

### Caso de Uso 3: SQL MCP — Consultas ao Banco

**Setup:** Você tem MCP de banco de dados local (SQLite, PostgreSQL).

**Estrutura de Banco:**

```sql
-- Schema
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT,
  email TEXT,
  created_at TIMESTAMP
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  total DECIMAL,
  created_at TIMESTAMP
);
```

**Pergunta ao Claude Code:**

```
"Use SQL MCP para:
1. Contar quantos usuários foram criados em último mês
2. Encontrar usuários sem pedidos
3. Análise: qual foi ordem média por cliente?"
```

Claude consulta banco e retorna:

```
Análise do banco de dados:

1. Usuários criados (último mês): 42
2. Usuários sem pedidos: 15
3. Ordem média por cliente: $127.50

Sugestão: 15 usuários sem pedidos podem ser oportunidade
de follow-up para re-engagement.
```

Agora você não precisa abrir client SQL separado.

---

### Habilitando MCP em Claude Code

**Arquivo de Configuração:**

Localização:
- Windows: `%APPDATA%\Anthropic\claude_desktop_config.json`
- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

**Exemplo com Git MCP:**

```json
{
  "mcpServers": {
    "git": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-git"]
    },
    "github": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Instalação:**

```bash
npm install @anthropic-ai/mcp-server-git @anthropic-ai/mcp-server-github
```

Depois reinicie VS Code.

---

### Criando MCP Customizado para Seu Projeto

**Cenário:** Seu projeto tem sistema de build customizado.

**Arquivo: `mcp_build_server.py`**

```python
#!/usr/bin/env python3
"""MCP Server para interagir com sistema de build customizado."""

import json
import subprocess
from typing import Any

def get_build_status() -> dict:
    """Retorna status do último build."""
    result = subprocess.run(
        ["python", "build.py", "--status"],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)

def trigger_build(target: str) -> str:
    """Dispara build para target específico."""
    result = subprocess.run(
        ["python", "build.py", "--build", target],
        capture_output=True, text=True
    )
    return result.stdout

def get_build_logs(limit: int = 10) -> list:
    """Retorna últimos N logs de build."""
    result = subprocess.run(
        ["python", "build.py", "--logs", str(limit)],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)

# Registrar recursos MCP
if __name__ == "__main__":
    print(json.dumps({
        "tools": [
            {
                "name": "get_build_status",
                "description": "Obtém status do último build"
            },
            {
                "name": "trigger_build",
                "description": "Dispara novo build",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "target": {"type": "string", "description": "Target (dev/prod)"}
                    }
                }
            },
            {
                "name": "get_build_logs",
                "description": "Retorna logs recentes"
            }
        ]
    }))
```

**Registrar em `claude_desktop_config.json`:**

```json
{
  "mcpServers": {
    "custom-build": {
      "command": "python",
      "args": ["mcp_build_server.py"]
    }
  }
}
```

**Agora no Claude Code:**

```
"Qual é o status do último build?"
```

Claude executa `get_build_status()` e retorna resultado em tempo real.

---

## AULA 12 — Projeto Final: Refatoração Completa com Claude Code

### Capstone Project: Do Zero ao Refatorado

**Objetivos da Aula:**
- Aplicar tudo aprendido em projeto real
- Documentar processo e aprendizados
- Revisar qualidade final

**Habilidades Esperadas:**
- Aplicação integrada de: refatoração, testes, documentação
- Tomada de decisão: quando usar Claude Code
- Avaliação crítica de mudanças

---

### Projeto: Módulo `user_manager.py`

**Estado Inicial (Péssimo):**

```python
# user_manager.py
def um(d):
    a = []
    for u in d:
        x = u['n']
        y = u['a']
        if y > 18:
            a.append({'name': x, 'age': y})
    return a

def ap(n, a, e):
    return {'name': n, 'age': a, 'email': e}

def sv(f, d):
    import json
    with open(f, 'w') as g:
        json.dump(d, g)

def ld(f):
    import json
    with open(f) as g:
        return json.load(g)
```

**Problemas:**

- ❌ Nomes de variáveis ilegíveis (um, d, a, x, y)
- ❌ Sem type hints
- ❌ Sem documentação
- ❌ Sem tratamento de erro
- ❌ Sem testes
- ❌ Imports dentro de função (ineficiente)
- ❌ Lógica não modular

---

### Fase 1: Análise com Claude Code

**Pergunta 1:**

```
"Arquivo @user_manager.py está legível? Liste problemas."
```

Claude identifica:

```
Problemas encontrados:
1. Nomes de variáveis: um, d, a, x, y (não legível)
2. Sem type hints (confuso qual é tipo de input/output)
3. Sem docstrings (função um() faz o quê?)
4. Imports dentro de função (ld e sv)
5. Sem tratamento de FileNotFoundError ou JSONDecodeError
6. Sem validação de entrada
7. Sem testes
```

---

### Fase 2: Refatoração Passo a Passo

**Pergunta 2:**

```
"Renomeie variáveis para nomes legíveis. Não aplique mudança,
mostre novo código."
```

Claude sugere:

```python
def filter_adult_users(users):
    """Filtra usuários maiores de 18."""
    adult_users = []
    for user in users:
        name = user['name']
        age = user['age']
        if age > 18:
            adult_users.append({'name': name, 'age': age})
    return adult_users

def create_user(name, age, email):
    """Cria dicionário de usuário."""
    return {'name': name, 'age': age, 'email': email}

def save_users(filepath, users):
    """Salva usuários em JSON."""
    with open(filepath, 'w') as file:
        json.dump(users, file)

def load_users(filepath):
    """Carrega usuários de JSON."""
    with open(filepath) as file:
        return json.load(file)
```

**Pergunta 3:**

```
"Adicione type hints e docstrings em estilo Google."
```

Claude refatora:

```python
from typing import List, Dict, Any
import json

def filter_adult_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filtra usuários maiores de 18 anos.
    
    Args:
        users: Lista de dicionários com chaves 'name', 'age'.
    
    Returns:
        Lista de usuários com age > 18.
    """
    return [u for u in users if u['age'] > 18]

def create_user(name: str, age: int, email: str) -> Dict[str, Any]:
    """Cria dicionário de usuário.
    
    Args:
        name: Nome completo.
        age: Idade em anos.
        email: Endereço de email.
    
    Returns:
        Dicionário com usuário.
    """
    return {'name': name, 'age': age, 'email': email}

def save_users(filepath: str, users: List[Dict]) -> None:
    """Salva usuários em arquivo JSON.
    
    Args:
        filepath: Caminho do arquivo.
        users: Lista de usuários.
    
    Raises:
        IOError: Se falhar escrita em disco.
    """
    try:
        with open(filepath, 'w') as file:
            json.dump(users, file, indent=2)
    except IOError as e:
        print(f"Erro ao salvar: {e}")
        raise

def load_users(filepath: str) -> List[Dict]:
    """Carrega usuários de arquivo JSON.
    
    Args:
        filepath: Caminho do arquivo.
    
    Returns:
        Lista de usuários.
    
    Raises:
        FileNotFoundError: Se arquivo não existe.
        json.JSONDecodeError: Se JSON inválido.
    """
    try:
        with open(filepath) as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {filepath} não encontrado")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON inválido: {e}")
        return []
```

**Pergunta 4:**

```
"Gere testes unitários com pytest cobrindo:
- filter_adult_users com casos normais e edge
- create_user com dados válidos
- save/load round-trip
- Erro ao carregar arquivo inexistente"
```

Claude gera:

```python
import pytest
import json
import os
from user_manager import filter_adult_users, create_user, save_users, load_users

@pytest.fixture
def sample_users():
    return [
        {'name': 'Alice', 'age': 25, 'email': 'alice@test.com'},
        {'name': 'Bob', 'age': 17, 'email': 'bob@test.com'},
        {'name': 'Charlie', 'age': 30, 'email': 'charlie@test.com'},
    ]

def test_filter_adult_users(sample_users):
    result = filter_adult_users(sample_users)
    assert len(result) == 2
    assert all(u['age'] > 18 for u in result)

def test_filter_no_adults():
    users = [{'name': 'Baby', 'age': 2, 'email': 'baby@test.com'}]
    result = filter_adult_users(users)
    assert result == []

def test_create_user():
    user = create_user('Alice', 25, 'alice@test.com')
    assert user['name'] == 'Alice'
    assert user['age'] == 25
    assert user['email'] == 'alice@test.com'

def test_save_load_roundtrip(sample_users, tmp_path):
    filepath = tmp_path / "users.json"
    
    save_users(str(filepath), sample_users)
    loaded = load_users(str(filepath))
    
    assert loaded == sample_users

def test_load_nonexistent_file():
    result = load_users('/nonexistent/file.json')
    assert result == []
```

**Fase 3: Documentação**

**Pergunta 5:**

```
"Gere README.md documentando módulo user_manager com:
- Descrição
- Exemplos de uso
- API reference"
```

Claude gera:

```markdown
# User Manager

Módulo para gerenciar usuários com operações básicas: filtro, criação, persistência.

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

```python
from user_manager import create_user, filter_adult_users, save_users, load_users

# Criar usuários
users = [
    create_user('Alice', 25, 'alice@test.com'),
    create_user('Bob', 17, 'bob@test.com'),
]

# Filtrar maiores de 18
adults = filter_adult_users(users)
# [{'name': 'Alice', 'age': 25, 'email': 'alice@test.com'}]

# Salvar em arquivo
save_users('users.json', users)

# Carregar de arquivo
loaded = load_users('users.json')
```

## API Reference

### filter_adult_users(users)
Filtra usuários com age > 18.

### create_user(name, age, email)
Cria novo usuário.

### save_users(filepath, users)
Persiste usuários em JSON.

### load_users(filepath)
Carrega usuários de JSON.
```

---

### Fase 4: Validação e Testes

**Execute testes:**

```bash
pytest test_user_manager.py -v --cov=user_manager

# Resultado:
# test_filter_adult_users PASSED
# test_filter_no_adults PASSED
# test_create_user PASSED
# test_save_load_roundtrip PASSED
# test_load_nonexistent_file PASSED
# 
# ========== 5 passed in 0.15s ==========
# Name            Stmts   Miss  Cover
# user_manager.py    35      0   100%
```

✅ **100% de cobertura!**

---

### Resumo da Transformação

| Métrica | Antes | Depois |
|---------|-------|--------|
| Linhas de código | 25 | 65 (mais documentação) |
| Type hints | ❌ | ✅ |
| Docstrings | ❌ | ✅ (Google style) |
| Testes | ❌ | ✅ (5 testes, 100% cobertura) |
| Tratamento de erro | ❌ | ✅ |
| README | ❌ | ✅ |
| Legibilidade | ⭐ | ⭐⭐⭐⭐⭐ |

---

## AULA 13 — Troubleshooting e Próximos Passos

### Problemas Comuns e Soluções

**Problema 1: "Claude Code não aparece após instalação"**

```
Solução 1: Recarregar janela
- Ctrl + Shift + P → "Developer: Reload Window"

Solução 2: Desinstalar e reinstalar
- Extensions → Claude Code → Uninstall
- Reiniciar VS Code
- Reinstalar

Solução 3: Verificar versão VS Code
- Help → About
- Se < 1.95, atualize VS Code
```

---

**Problema 2: "Erro de autenticação (API key inválida)"**

```
Solução 1: Verificar chave
- Abra https://console.anthropic.com
- Vá em API Keys
- Gere nova chave (a antiga pode ter expirado)

Solução 2: Re-inserir chave
- VS Code: Ctrl + Shift + P
- "Claude Code: Sign Out"
- "Claude Code: Sign In"
- Cole nova chave

Solução 3: Limpar cache
- Windows: delete %USERPROFILE%\.anthropic
- Mac: rm -rf ~/.anthropic
- Fazer login novamente
```

---

**Problema 3: "Firewall corporativo bloqueia Anthropic"**

```
Solução 1: Verificar whitelist
- Contate seu admin TI
- Peça para whitelisted api.anthropic.com

Solução 2: Usar proxy
- VS Code → File → Preferences → Settings
- Search "proxy"
- Configure proxy corporativo

Solução 3: Usar alternativa
- Use Claude Web (claude.ai) em navegador corporativo
- Ou Claude CLI se tiver autorização
```

---

**Problema 4: "Claude sugeriu mudança ruim, aceitei por engano"**

```
Solução: Git pode resolver
- git diff (ver mudanças)
- git checkout user_manager.py (revert arquivo)
- Aprenda do erro
```

---

### Recursos para Continuar Aprendendo

**📚 Documentação Oficial:**
- https://docs.anthropic.com — API docs e guias
- https://github.com/anthropics/anthropic-sdk — SDKs em várias linguagens

**🎓 Comunidade:**
- Discord Anthropic (https://discord.gg/anthropic)
- GitHub Discussions
- Stack Overflow (tag: claude-ai)

**🚀 Próximos Passos Recomendados:**

1. **Integração CI/CD:** Configure GitHub Actions para rodar testes automaticamente
2. **MCP Avançado:** Explore MCPs para seu domínio específico (Engenharia Civil, ML, etc.)
3. **Automação Local:** Use `claude` CLI para scripts sem VS Code
4. **Colaboração:** Compartilhe prompts úteis com time

---

## CONCLUSÃO

Você agora pode:

✅ Instalar e configurar Claude Code no VS Code  
✅ Usar contexto de arquivo para prompts efetivos  
✅ Refatorar código com segurança (ask → plan → review → accept)  
✅ Gerar testes unitários com cobertura completa  
✅ Documentar código automaticamente  
✅ Debugar erros com stack trace e contexto  
✅ Automatar tarefas com scripts  
✅ Entender limitações e segurança de dados  
✅ Integrar MCP para contexto expandido  
✅ Executar projeto real do zero ao refatorado  

**Próximo passo:** Pegue um projeto real, aplique o padrão 5-step (Ask → Explain → Plan → Diff → Accept) e observe como sua produtividade aumenta.

---

**Happy Coding! 🚀**
