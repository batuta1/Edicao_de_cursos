"""Validation utilities for SCORM processing."""

import json
from pathlib import Path
from typing import Dict, Any, List

from ..config.constants import DEFAULT_ENCODING


class LessonValidator:
    """Validates lesson content and structure."""

    @staticmethod
    def search_text(text: str, obj: Any) -> bool:
        """Recursively search for text in data structure."""
        if isinstance(obj, dict):
            return any(
                LessonValidator.search_text(text, v)
                for v in obj.values()
            )
        elif isinstance(obj, list):
            return any(
                LessonValidator.search_text(text, item)
                for item in obj
            )
        elif isinstance(obj, str):
            return text in obj
        return False

    def find_text_in_lessons(
        self,
        lessons_dir: Path,
        search_text: str
    ) -> Dict[str, Dict[str, bool]]:
        """
        Search for text in lesson files.

        Returns:
            Dict mapping lesson filename to search results (found_in_content, found_in_lesson).
        """
        results = {}

        for lesson_file in sorted(lessons_dir.glob("licao_*.json")):
            with open(lesson_file, "r", encoding=DEFAULT_ENCODING) as f:
                lesson_data = json.load(f)

            # Check if text exists anywhere in lesson
            found_anywhere = self.search_text(search_text, lesson_data)

            # Check if text exists in lesson content specifically
            found_in_lesson = self.search_text(
                search_text,
                lesson_data.get("lesson", {})
            )

            results[lesson_file.name] = {
                "found_anywhere": found_anywhere,
                "found_in_lesson": found_in_lesson,
            }

        return results

    @staticmethod
    def validate_lesson_structure(lesson_data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """
        Validate that lesson has required fields.

        Returns:
            Tuple of (is_valid, error_messages).
        """
        errors = []

        if "numero_da_licao" not in lesson_data:
            errors.append("Missing 'numero_da_licao'")
        if "title" not in lesson_data:
            errors.append("Missing 'title'")
        if "lesson" not in lesson_data:
            errors.append("Missing 'lesson' content")

        return len(errors) == 0, errors
