# Análise e Plano de Reorganização do Repositório

**Data:** 2026-05-20  
**Status:** Proposta de Estruturação  
**Origem de dados:** 3_scorm

---

## 1. Diagnóstico Atual

### Estrutura Existente
```
projeto/
├── 2_src/
│   └── config/
│       ├── constants.py (vazio - 0 linhas)
│       └── path.py (vazio - 0 linhas)
│
├── 3_scorm/ (ORIGEM DE DADOS)
│   ├── claudeEXCEL_curto_versao1/ (SCORM package v1)
│   │   ├── imsmanifest.xml
│   │   ├── *.xsd, *.dtd (schemas)
│   │   └── scormcontent/
│   │
│   ├── claudeEXCEL_versao1/ (SCORM package v1 - alternativa)
│   │   └── [estrutura similar]
│   │
│   └── cursos_desserializados/ (CÓDIGO PYTHON - 467 linhas total)
│       ├── desserialize.py (18 linhas) - extrai dados base64
│       ├── IDlesson.py (24 linhas) - estrutura lição
│       ├── lessonExtracter.py (64 linhas) - separa lições
│       ├── lessonExtracterTester.py (118 linhas) - testa extração
│       ├── mapCourse.py (19 linhas) - mapeia tipos de conteúdo
│       ├── mapCourseDetailed.py (66 linhas) - mapeamento detalhado
│       ├── serializeCourse.py (131 linhas) - reconstrói curso
│       ├── testMessage.py (26 linhas) - procura texto
│       └── [arquivos de dados: *.json, arquivos SCORM originais]
└── .git/
```

### Problemas Identificados

| Problema | Impacto | Severidade |
|----------|---------|-----------|
| **Paths hardcoded** | Scripts usam `Path(__file__).parent / "arquivo.json"` sem centralização | Média |
| **Config vazia** | 2_src/config não implementado | Alta |
| **Sem estrutura clara** | Código, dados e testes misturados | Alta |
| **Sem entry points** | Nenhum script tem `if __name__ == "__main__"` | Média |
| **Sem configuração env** | Sem suporte a diferentes ambientes | Média |
| **Sem documentação de APIs** | Scripts não documentam interfaces | Média |
| **Acoplamento forte** | Nenhuma reutilização entre módulos | Baixa |

---

## 2. Plano de Reorganização

### 2.1 Estrutura Proposta

```
projeto/
├── .github/
│   └── workflows/ (CI/CD no futuro)
│
├── 1_docs/
│   ├── ARCHITECTURE.md (decisões de design)
│   ├── API.md (interfácies do código)
│   └── SCORM_SPEC.md (referência dos pacotes SCORM)
│
├── 2_src/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py (configuração centralizada)
│   │   ├── constants.py (valores fixos)
│   │   └── paths.py (gestão de paths com validação)
│   │
│   ├── scorm/
│   │   ├── __init__.py
│   │   ├── deserializer.py (base64 → JSON)
│   │   ├── extractor.py (lições → arquivos separados)
│   │   ├── mapper.py (análise de tipos de conteúdo)
│   │   ├── serializer.py (JSON → base64)
│   │   └── models.py (Lesson, Course, etc)
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_utils.py (sanitização de nomes, I/O)
│   │   └── validators.py (verificações de integridade)
│   │
│   └── cli.py (entry point principal)
│
├── 3_scorm/ (FONTE DE DADOS)
│   ├── raw_packages/
│   │   ├── claudeEXCEL_curto_versao1/ (SCORM original v1)
│   │   └── claudeEXCEL_versao1/ (SCORM original v1 alt)
│   │
│   └── processed/ (GERADO AUTOMATICAMENTE)
│       ├── cursoVSCODE/
│       │   ├── curso.json (desserializado)
│       │   └── licoes/ (lições extraídas)
│       │
│       └── cursoVSCODE_test/
│           ├── curso.json
│           └── licoes/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py (fixtures pytest)
│   ├── unit/
│   │   ├── test_deserializer.py
│   │   ├── test_extractor.py
│   │   ├── test_mapper.py
│   │   └── test_validators.py
│   │
│   └── integration/
│       └── test_full_pipeline.py (end-to-end)
│
├── requirements.txt
├── pytest.ini
├── .env.example
├── README.md
├── REPOSITORY_STRUCTURE.md (este arquivo)
└── .gitignore (exclui dados processados)
```

---

## 3. Detalhes da Reorganização

### 3.1 Módulo `config`

**Antes:**
```python
# Cada script hardcoda seus paths
pasta_base = Path(__file__).parent
arquivo = pasta_base / "cursoVSCODE.json"
```

**Depois:**
```python
# 2_src/config/paths.py
from pathlib import Path
from .settings import REPO_ROOT

class ScormPaths:
    RAW_PACKAGES = REPO_ROOT / "3_scorm" / "raw_packages"
    PROCESSED = REPO_ROOT / "3_scorm" / "processed"
    TEMP = REPO_ROOT / ".tmp"
    
    @staticmethod
    def get_course_path(course_name: str):
        return ScormPaths.PROCESSED / course_name / "curso.json"
    
    @staticmethod
    def get_lessons_dir(course_name: str):
        return ScormPaths.PROCESSED / course_name / "licoes"
```

**Benefícios:**
- Um lugar para mudar todos os paths
- Suporte para diferentes ambientes (dev/prod)
- Validação de diretórios existentes
- Camada de abstração para I/O

### 3.2 Módulo `scorm`

**Antes:**
```python
# lessonExtracter.py - 64 linhas, sem classe
for numero, licao in enumerate(licoes_ordenadas, start=1):
    # lógica inline
```

**Depois:**
```python
# 2_src/scorm/models.py
@dataclass
class Lesson:
    numero: int
    position: int
    title: str
    content: dict

# 2_src/scorm/extractor.py
class LessonExtractor:
    def __init__(self, paths: ScormPaths):
        self.paths = paths
    
    def extract(self, course_data: dict) -> List[Lesson]:
        """Extrai lições ordenadas de dados do curso."""
        pass
    
    def save_to_files(self, lessons: List[Lesson], output_dir: Path):
        """Salva lições em arquivos separados."""
        pass
```

**Benefícios:**
- Classes reutilizáveis
- Testes isolados
- Documentação via docstrings
- Sem side-effects globais

### 3.3 Organização de Dados

**3_scorm antes:**
```
3_scorm/
├── claudeEXCEL_curto_versao1/
├── claudeEXCEL_versao1/
├── cursos_desserializados/ (MISTURA CÓDIGO E DADOS)
│   ├── *.py (scripts)
│   ├── *.json (dados de entrada)
│   ├── licoes_extraidas/ (dados de saída)
│   └── ...arquivos SCORM
```

**3_scorm depois:**
```
3_scorm/
├── raw_packages/ (ORIGEM IMUTÁVEL)
│   ├── claudeEXCEL_curto_versao1/
│   │   ├── imsmanifest.xml
│   │   ├── *.xsd
│   │   ├── scormcontent/
│   │   └── scormdriver/
│   │
│   └── claudeEXCEL_versao1/
│       └── [estrutura similar]
│
└── processed/ (GERADO - NÃO COMMITAR)
    ├── cursoVSCODE/
    │   ├── curso.json (desserializado)
    │   └── licoes/
    │       ├── licao_01_*.json
    │       ├── licao_02_*.json
    │       └── indice_licoes.json
    │
    └── cursoVSCODE_test/
        └── [estrutura similar]
```

**Benefícios:**
- Separação clara: código vs. dados
- Dados processados no .gitignore
- Reprodutibilidade (regenerar do raw sempre)

### 3.4 Scripts de Entrada (CLI)

**2_src/cli.py:**
```python
#!/usr/bin/env python3
import argparse
from scorm.deserializer import CourseDeserializer
from scorm.extractor import LessonExtractor
from config.paths import ScormPaths

def main():
    parser = argparse.ArgumentParser(
        description="Processa cursos SCORM"
    )
    parser.add_argument(
        "action",
        choices=["deserialize", "extract", "serialize", "map"],
        help="Ação a executar"
    )
    parser.add_argument(
        "--course", required=True,
        help="Nome do curso (ex: claudeEXCEL_curto_versao1)"
    )
    
    args = parser.parse_args()
    
    if args.action == "extract":
        extractor = LessonExtractor(ScormPaths())
        # ... lógica
    # ... outros comandos

if __name__ == "__main__":
    main()
```

**Uso:**
```bash
python 2_src/cli.py deserialize --course claudeEXCEL_curto_versao1
python 2_src/cli.py extract --course claudeEXCEL_curto_versao1
```

---

## 4. Cronograma de Implementação

| Fase | Tarefa | Prioridade | Esforço |
|------|--------|-----------|--------|
| **1** | Criar estrutura `2_src/config/` com `settings.py` e `paths.py` | Alta | 1h |
| **2** | Criar `2_src/scorm/models.py` com dataclasses | Alta | 2h |
| **3** | Refatorar `lessonExtracter.py` → `2_src/scorm/extractor.py` | Alta | 2h |
| **4** | Refatorar `serializeCourse.py` → `2_src/scorm/serializer.py` | Alta | 2h |
| **5** | Refatorar `mapCourseDetailed.py` → `2_src/scorm/mapper.py` | Média | 1.5h |
| **6** | Criar `2_src/utils/file_utils.py` | Média | 1h |
| **7** | Criar `tests/` com testes unitários | Média | 3h |
| **8** | Implementar `2_src/cli.py` | Média | 2h |
| **9** | Reorganizar 3_scorm/ em raw_packages/ e processed/ | Alta | 1h |
| **10** | Atualizar `.gitignore` | Baixa | 0.5h |
| **Total** | - | - | **16h** |

---

## 5. Configuração de Ambiente

### 5.1 `.env.example`
```env
# Diretórios
REPO_ROOT=
SCORM_RAW_PACKAGES=3_scorm/raw_packages
SCORM_PROCESSED=3_scorm/processed
TEMP_DIR=.tmp

# Logging
LOG_LEVEL=INFO
```

### 5.2 `requirements.txt`
```
pytest==7.4.0
pytest-cov==4.1.0
python-dotenv==1.0.0
```

---

## 6. Mudanças em `3_scorm`

### Antes
```
3_scorm/
├── claudeEXCEL_curto_versao1/ ← SCORM original misturado com outputs
├── cursos_desserializados/ ← Código + dados + saídas
└── claudeEXCEL_versao1/
```

### Depois
```
3_scorm/
├── raw_packages/ ← SCORM originais, IMUTÁVEL
│   ├── claudeEXCEL_curto_versao1/
│   └── claudeEXCEL_versao1/
│
└── processed/ ← Gerado automaticamente (NO .gitignore)
    ├── cursoVSCODE/
    └── cursoVSCODE_test/
```

### Ações Específicas

1. **Mover SCORM originais:**
   ```bash
   mkdir -p 3_scorm/raw_packages
   mv 3_scorm/claudeEXCEL_curto_versao1 3_scorm/raw_packages/
   mv 3_scorm/claudeEXCEL_versao1 3_scorm/raw_packages/
   ```

2. **Criar estrutura processed:**
   ```bash
   mkdir -p 3_scorm/processed
   # Dados processados serão gerados aqui pela CLI
   ```

3. **Atualizar .gitignore:**
   ```gitignore
   3_scorm/processed/
   .tmp/
   *.pyc
   __pycache__/
   .env
   ```

---

## 7. Impacto nos Scripts Existentes

| Script | Ação | Novo Local |
|--------|------|-----------|
| `lessonExtracter.py` | Refatorar em classe | `2_src/scorm/extractor.py` |
| `lessonExtracterTester.py` | Integrar como teste | `tests/integration/test_extraction.py` |
| `serializeCourse.py` | Refatorar em classe | `2_src/scorm/serializer.py` |
| `mapCourse.py` | Refatorar em classe | `2_src/scorm/mapper.py` |
| `mapCourseDetailed.py` | Refatorar em classe | `2_src/scorm/mapper.py` (detalhe) |
| `IDlesson.py` | Converter em dataclass | `2_src/scorm/models.py` |
| `desserialize.py` | Refatorar em classe | `2_src/scorm/deserializer.py` |
| `testMessage.py` | Integrar em utils | `2_src/utils/validators.py` |

---

## 8. Configuração de Tests

### `pytest.ini`
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

### `tests/conftest.py`
```python
import pytest
from pathlib import Path
from 2_src.config.paths import ScormPaths

@pytest.fixture
def scorm_paths(tmp_path):
    """Fornece paths temporários para testes."""
    return ScormPaths(root=tmp_path)

@pytest.fixture
def sample_course_data():
    """Carrega dados de teste padrão."""
    # retorna dict com estrutura de curso
    pass
```

---

## 9. Benefícios da Reorganização

✅ **Manutenibilidade:** Código organizado por funcionalidade, não por tipo  
✅ **Testabilidade:** Classes isoladas, fixtures reutilizáveis  
✅ **Escalabilidade:** Fácil adicionar novos processors (XML, CSV, etc)  
✅ **Reusabilidade:** Módulos podem ser importados como biblioteca  
✅ **Portabilidade:** Paths centralizados, suporta diferentes ambientes  
✅ **Documentação:** Estrutura clara reduz cognitive load  
✅ **CI/CD Ready:** Estrutura permite testes e builds automatizados  

---

## 10. Próximos Passos

1. **Discussão:** Validar proposta com stakeholders
2. **Implementação Fase 1:** Criar estrutura base (config + models)
3. **Refatoração:** Migrar código existente (fases 3-6)
4. **Testes:** Implementar suite de testes (fase 7)
5. **Validação:** Rodar pipeline completo (phase 8-10)
6. **Documentação:** Adicionar READMEs em cada módulo

---

## Apêndice A: Mapas de Importação

### Antes
```
lessonExtracter.py
├─ json
├─ re
└─ pathlib

mapCourse.py
├─ json
├─ collections
└─ pathlib

serializeCourse.py
├─ json
├─ base64
└─ pathlib
```

### Depois (Exemplo)
```
cli.py
├─ config.settings (APP_ROOT, LOG_LEVEL)
├─ config.paths (ScormPaths)
├─ scorm.extractor (LessonExtractor)
├─ scorm.serializer (CourseSerializer)
└─ scorm.models (Lesson, Course)

tests/unit/test_extractor.py
├─ scorm.extractor
├─ scorm.models
├─ config.paths
└─ pytest fixtures
```

---

## Apêndice B: Análise Detalhada dos Arquivos Existentes

Descrição de cada arquivo em `3_scorm/cursos_desserializados/`, sua funcionalidade, e local na nova estrutura.

### 1. `desserialize.py` (18 linhas)

**O que faz:**
- Decodifica base64 extraído de SCORM (imsmanifest.xml ou similar)
- Converte para JSON usando `base64.b64decode()`
- Adiciona padding base64 conforme necessário
- Salva resultado em arquivo JSON local

**Entrada:** String base64 hardcoded no script  
**Saída:** Arquivo `cursoVSCODEtest.json`

**Novo local:** `2_src/scorm/deserializer.py`  
**Refatoração:** Converter em classe reutilizável
```python
class CourseDeserializer:
    def deserialize_base64(self, base64_str: str) -> dict:
        """Decodifica base64 → JSON."""
        pass
    
    def save_to_file(self, data: dict, filepath: Path):
        """Salva dados em arquivo JSON."""
        pass
```

---

### 2. `IDlesson.py` (24 linhas)

**O que faz:**
- Semelhante a `desserialize.py` (decodifica base64)
- Foco em extrair estrutura de uma lição individual
- Analisa tipos de conteúdo dentro da lição
- Salva análise em `estrutura_licoes.json`

**Entrada:** String base64 de uma lição  
**Saída:** Arquivo `estrutura_licoes.json` com análise

**Novo local:** `2_src/scorm/deserializer.py` (merge com desserialize)  
**Refatoração:** Integrar como método em `CourseDeserializer`
```python
class CourseDeserializer:
    def analyze_lesson_structure(self, lesson_data: dict) -> dict:
        """Analisa tipos de conteúdo em lição."""
        pass
```

**Nota:** Código pode ser consolidado com `desserialize.py` - ambos fazem decode de base64.

---

### 3. `lessonExtracter.py` (64 linhas) ⭐ **CRÍTICO**

**O que faz:**
- **Função principal:** Extrai lições individuais de um JSON de curso
- Lê JSON completo com estrutura `curso.lessons[]`
- Ordena lições por posição original
- Cria pasta `licoes_extraidas/`
- Salva cada lição em arquivo separado: `licao_01_titulo.json`, `licao_02_titulo.json`, etc
- Gera índice: `indice_licoes.json`
- Limpa nomes de arquivo (remove caracteres inválidos)

**Entrada:** `cursoVSCODEtest.json`  
**Saída:** 
- `licoes_extraidas/licao_01_*.json`
- `licoes_extraidas/licao_02_*.json`
- `licoes_extraidas/indice_licoes.json`

**Novo local:** `2_src/scorm/extractor.py`  
**Refatoração:** Converter em classe
```python
class LessonExtractor:
    def __init__(self, paths: ScormPaths):
        self.paths = paths
    
    def extract_all(self, course_data: dict) -> List[Lesson]:
        """Extrai todas as lições."""
        lessons = []
        for i, lesson in enumerate(self._sort_lessons(course_data["lessons"])):
            lessons.append(self._create_lesson_object(lesson, i))
        return lessons
    
    def save_to_files(self, lessons: List[Lesson], output_dir: Path):
        """Salva lições em arquivos separados."""
        for lesson in lessons:
            self._write_lesson_file(lesson, output_dir)
        self._write_index(lessons, output_dir)
    
    @staticmethod
    def _sanitize_filename(text: str) -> str:
        """Remove caracteres inválidos para nomes de arquivo."""
        # Move para utils/file_utils.py
        pass
```

---

### 4. `lessonExtracterTester.py` (118 linhas) ⭐ **TESTE**

**O que faz:**
- **Propósito:** Testa pipeline de edição de lições
- Carrega lições extraídas da pasta `licoes_extraidas/`
- Simula edição (adiciona texto de teste "OI EU EDITEI")
- Reconstrói JSON do curso a partir das lições editadas
- Valida se dados fazem round-trip corretamente
- Gera saída base64 para validação manual

**Entrada:** 
- `cursoVSCODEtest.json` (molde original)
- `licoes_extraidas/licao_*.json` (lições extraídas)

**Saída:**
- `cursoVSCODEtest_editado.json` (curso reconstitído)
- `cursoVSCODEtest_editado_base64.txt` (para validação)

**Novo local:** `tests/integration/test_lesson_roundtrip.py`  
**Refatoração:** Converter em teste pytest
```python
class TestLessonRoundTrip:
    def test_extract_and_serialize(self, sample_course):
        """Extrai lições e reconstrói curso."""
        # Arrange
        extractor = LessonExtractor(self.paths)
        serializer = CourseSerializer(self.paths)
        
        # Act
        lessons = extractor.extract_all(sample_course)
        reconstructed = serializer.serialize_from_lessons(lessons)
        
        # Assert
        assert reconstructed["course"]["lessons"] == sample_course["course"]["lessons"]
```

---

### 5. `mapCourse.py` (19 linhas)

**O que faz:**
- **Análise de metadados:** Conta tipos de conteúdo em um curso
- Percorre estrutura JSON recursivamente
- Busca campos `type` em cada objeto
- Usa `Counter` para contabilizar
- Imprime relatório: `"type_name": quantidade`

**Entrada:** `cursoVSCODEtest.json`  
**Saída:** Relatório em stdout

**Novo local:** `2_src/scorm/analyzer.py`  
**Refatoração:** Criar classe `ContentTypeAnalyzer`
```python
class ContentTypeAnalyzer:
    def count_types(self, course_data: dict) -> Counter:
        """Conta tipos de conteúdo em curso."""
        pass
    
    def get_type_distribution(self) -> Dict[str, int]:
        """Retorna distribuição de tipos."""
        pass
```

---

### 6. `mapCourseDetailed.py` (66 linhas)

**O que faz:**
- **Análise detalhada e visual:** Cria mapa completo do curso
- Lê JSON de curso
- Percorre cada lição e elemento interno
- Formata saída em arquivo `.txt` legível
- Agrupa por lição, elemento tipo
- Trunca textos longos para legibilidade
- Cria hierarquia visual com "=" (80 colunas)

**Entrada:** `cursoVSCODEtest.json`  
**Saída:** `mapa_detalhado_curso_VSCODE_test.txt` (arquivo formatado para leitura)

**Novo local:** `2_src/scorm/analyzer.py` (junto com `mapCourse.py`)  
**Refatoração:** Estender `ContentTypeAnalyzer`
```python
class ContentTypeAnalyzer:
    def generate_detailed_map(self, course_data: dict) -> str:
        """Gera mapa visual do curso."""
        lines = []
        # ... lógica de formatação
        return "\n".join(lines)
    
    def save_map_to_file(self, course_data: dict, output_path: Path):
        """Salva mapa em arquivo .txt."""
        map_text = self.generate_detailed_map(course_data)
        output_path.write_text(map_text, encoding="utf-8")
```

---

### 7. `serializeCourse.py` (131 linhas) ⭐ **CRÍTICO**

**O que faz:**
- **Função principal:** Reconstrói curso original a partir de lições editadas
- Carrega JSON original como molde
- Itera lições da pasta `licoes_extraidas/`
- Reinsere lições editadas na estrutura original
- Reconstrói JSON completo
- Encoda resultado em base64
- Localiza posição correta no arquivo HTML/imsmanifest original
- Oferece instruções para reinserção manual

**Entrada:**
- `cursoVSCODE.json` (molde - para preservar metadata)
- `licoes_extraidas/licao_*.json` (lições editadas)
- `index.html` ou `imsmanifest.xml` (estrutura SCORM)

**Saída:**
- `cursoVSCODE_editado.json` (curso reconstitído)
- `cursoVSCODE_editado_base64.txt` (pronto para reinserção)

**Novo local:** `2_src/scorm/serializer.py`  
**Refatoração:** Converter em classe
```python
class CourseSerializer:
    def __init__(self, paths: ScormPaths):
        self.paths = paths
    
    def serialize_from_lessons(
        self, 
        lessons: List[Lesson], 
        original_course: dict
    ) -> dict:
        """Reconstrói curso a partir de lições."""
        course_copy = copy.deepcopy(original_course)
        course_copy["course"]["lessons"] = [
            lesson.to_dict() for lesson in lessons
        ]
        return course_copy
    
    def encode_to_base64(self, course_data: dict) -> str:
        """Codifica para base64."""
        json_str = json.dumps(course_data, ensure_ascii=False)
        return base64.b64encode(json_str.encode()).decode()
    
    def find_base64_in_manifest(self, manifest_path: Path) -> str:
        """Localiza base64 no arquivo imsmanifest."""
        pass
```

---

### 8. `testMessage.py` (26 linhas)

**O que faz:**
- **Teste de busca:** Procura por mensagem específica em lições
- Define frase de teste: "OI EU EDITEI AQUI"
- Itera arquivos de lições extraídas
- Busca recursivamente em estrutura JSON
- Identifica se texto está dentro ou fora de campo `lesson`
- Importante: Valida se edições foram incorporadas corretamente

**Entrada:**
- `licoes_extraidas/licao_*.json`
- Frase teste hardcoded: "OI EU EDITEI AQUI"

**Saída:** Relatório em stdout indicando onde texto foi encontrado

**Novo local:** `2_src/utils/validators.py`  
**Refatoração:** Integrar em classe `LessonValidator`
```python
class LessonValidator:
    def search_text(self, lessons_dir: Path, search_text: str) -> Dict[str, bool]:
        """Procura texto em lições."""
        results = {}
        for lesson_file in lessons_dir.glob("licao_*.json"):
            data = json.load(lesson_file.open())
            found_in_content = self._search_recursive(data, search_text)
            found_in_lesson = self._search_recursive(
                data.get("lesson", {}), search_text
            )
            results[lesson_file.name] = {
                "found_anywhere": found_in_content,
                "found_in_lesson": found_in_lesson,
            }
        return results
    
    @staticmethod
    def _search_recursive(obj, text: str) -> bool:
        """Busca recursiva em estrutura."""
        if isinstance(obj, dict):
            return any(
                LessonValidator._search_recursive(v, text) 
                for v in obj.values()
            )
        elif isinstance(obj, list):
            return any(
                LessonValidator._search_recursive(item, text) 
                for item in obj
            )
        elif isinstance(obj, str):
            return text in obj
        return False
```

---

## Mapa de Migração: Arquivos Atuais → Nova Estrutura

| Arquivo Atual | Linhas | Tipo | Novo Local | Refatoração |
|---------------|--------|------|-----------|-------------|
| `desserialize.py` | 18 | Core | `2_src/scorm/deserializer.py` | Classe `CourseDeserializer` |
| `IDlesson.py` | 24 | Core | `2_src/scorm/deserializer.py` | Merge com desserialize |
| `lessonExtracter.py` | 64 | Core ⭐ | `2_src/scorm/extractor.py` | Classe `LessonExtractor` |
| `lessonExtracterTester.py` | 118 | Test | `tests/integration/test_lesson_roundtrip.py` | Pytest class |
| `mapCourse.py` | 19 | Analysis | `2_src/scorm/analyzer.py` | Classe `ContentTypeAnalyzer` |
| `mapCourseDetailed.py` | 66 | Analysis | `2_src/scorm/analyzer.py` | Método `generate_detailed_map()` |
| `serializeCourse.py` | 131 | Core ⭐ | `2_src/scorm/serializer.py` | Classe `CourseSerializer` |
| `testMessage.py` | 26 | Test | `2_src/utils/validators.py` | Classe `LessonValidator` |

**Totais:**
- **Core modules** (devem ser refatorados em classes): 4 arquivos → 3 módulos
- **Analysis** (combinar em um módulo): 2 arquivos → 1 módulo
- **Tests** (converter para pytest): 2 arquivos → 2 arquivos de teste
- **Utilities** (funções helper): Funções distribuídas → centralizar em utils/

---

## Dependências Entre Módulos (Fluxo de Dados)

```
raw SCORM packages (3_scorm/raw_packages/)
    ↓
CourseDeserializer (extrai base64 → JSON)
    ↓
course.json (desserializado)
    ↓
LessonExtractor (separa lições)
    ↓
licoes/ (arquivos individuais)
    ↓
[Edição Manual ou Teste]
    ↓
CourseSerializer (reconstrói de lições)
    ↓
course_editado.json (reconstitído)
    ↓
base64.txt (para reinserção em SCORM)
    ↓
imsmanifest.xml (manual update)
```

---

**Versão:** 1.1  
**Autor:** Análise de Claude  
**Última atualização:** 2026-05-20
