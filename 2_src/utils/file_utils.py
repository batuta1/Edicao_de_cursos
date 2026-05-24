"""File I/O utilities for SCORM processing."""

import json
import re
from pathlib import Path
from typing import Dict, Any

from ..config.constants import (
    DEFAULT_ENCODING,
    INVALID_FILENAME_CHARS,
    WHITESPACE_COLLAPSE,
    MAX_FILENAME_LENGTH,
    JSON_INDENT,
    ENSURE_ASCII,
)


def sanitize_filename(text: str) -> str:
    """Remove invalid characters from filename."""
    text = text.strip()
    text = re.sub(INVALID_FILENAME_CHARS, "", text)
    text = re.sub(WHITESPACE_COLLAPSE, "_", text)
    return text[:MAX_FILENAME_LENGTH]


def read_json(filepath: Path) -> Dict[str, Any]:
    """Read and parse JSON file."""
    with open(filepath, "r", encoding=DEFAULT_ENCODING) as f:
        return json.load(f)


def write_json(
    data: Dict[str, Any],
    filepath: Path,
    indent: int = JSON_INDENT,
    ensure_ascii: bool = ENSURE_ASCII,
) -> None:
    """Write data to JSON file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding=DEFAULT_ENCODING) as f:
        json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)


def read_base64_file(filepath: Path) -> str:
    """Read base64 string from text file."""
    with open(filepath, "r", encoding=DEFAULT_ENCODING) as f:
        return f.read().strip()


def write_base64_file(content: str, filepath: Path) -> None:
    """Write base64 string to text file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding=DEFAULT_ENCODING) as f:
        f.write(content)
