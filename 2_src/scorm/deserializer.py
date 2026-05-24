"""Deserialize base64-encoded SCORM courses to JSON."""

import base64
import json
from pathlib import Path
from typing import Dict, Any

from ..config.constants import (
    DEFAULT_ENCODING,
    BASE64_PADDING_CHAR,
    JSON_INDENT,
    ENSURE_ASCII,
)
from ..utils.file_utils import write_json


class CourseDeserializer:
    """Deserialize base64-encoded courses to JSON."""

    @staticmethod
    def fix_base64_padding(text: str) -> str:
        """Add proper base64 padding."""
        text = text.strip()
        text += BASE64_PADDING_CHAR * (-len(text) % 4)
        return text

    @staticmethod
    def decode_base64_to_json(base64_text: str) -> Dict[str, Any]:
        """Decode base64 string to JSON object."""
        corrected = CourseDeserializer.fix_base64_padding(base64_text)
        json_text = base64.b64decode(corrected).decode(DEFAULT_ENCODING)
        return json.loads(json_text)

    @staticmethod
    def deserialize_from_string(base64_text: str) -> Dict[str, Any]:
        """Deserialize base64 course data to dictionary."""
        return CourseDeserializer.decode_base64_to_json(base64_text)

    @staticmethod
    def deserialize_from_file(filepath: Path) -> Dict[str, Any]:
        """Read base64 from file and deserialize to dictionary."""
        base64_text = filepath.read_text(encoding=DEFAULT_ENCODING)
        return CourseDeserializer.deserialize_from_string(base64_text)

    @staticmethod
    def save_to_json_file(
        course_data: Dict[str, Any],
        output_path: Path
    ) -> None:
        """Save deserialized course to JSON file."""
        write_json(course_data, output_path)
