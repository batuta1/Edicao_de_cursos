"""Application constants and fixed values."""

# File encoding
DEFAULT_ENCODING = "utf-8"

# Filename patterns
LESSON_FILE_PATTERN = "licao_*.json"
INDEX_FILE_NAME = "indice_licoes.json"

# Base64 padding
BASE64_PADDING_CHAR = "="

# File constraints
MAX_FILENAME_LENGTH = 80

# Regex patterns for filename sanitization
INVALID_FILENAME_CHARS = r'[\\/*?:"<>|]'
WHITESPACE_COLLAPSE = r"\s+"

# JSON export
JSON_INDENT = 2
ENSURE_ASCII = False

# Content type field names
CONTENT_TYPE_FIELD = "type"
LESSON_FIELD = "lesson"
LESSONS_ARRAY = "lessons"
COURSE_FIELD = "course"
POSITION_FIELD = "position"
TITLE_FIELD = "title"
