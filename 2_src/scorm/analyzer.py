"""Analyze SCORM course structure and content."""

from pathlib import Path
from typing import Dict, Any, Counter
from collections import Counter as CounterClass

from ..config.constants import (
    DEFAULT_ENCODING,
    CONTENT_TYPE_FIELD,
    TITLE_FIELD,
    POSITION_FIELD,
)
from ..utils.file_utils import write_json


class ContentTypeAnalyzer:
    """Analyze content types and structure in SCORM courses."""

    def __init__(self):
        """Initialize analyzer."""
        self.types = CounterClass()

    @staticmethod
    def traverse_and_count_types(obj: Any, types: CounterClass) -> None:
        """Recursively traverse object and count 'type' fields."""
        if isinstance(obj, dict):
            if CONTENT_TYPE_FIELD in obj:
                types[obj[CONTENT_TYPE_FIELD]] += 1
            for value in obj.values():
                ContentTypeAnalyzer.traverse_and_count_types(value, types)
        elif isinstance(obj, list):
            for item in obj:
                ContentTypeAnalyzer.traverse_and_count_types(item, types)

    def analyze_course(self, course_data: Dict[str, Any]) -> Dict[str, int]:
        """Analyze content types in course."""
        self.types = CounterClass()
        self.traverse_and_count_types(course_data, self.types)
        return dict(self.types.most_common())

    def get_type_distribution(self) -> Dict[str, int]:
        """Get current type distribution."""
        return dict(self.types.most_common())

    def save_analysis(self, analysis: Dict[str, int], output_path: Path) -> None:
        """Save analysis results to JSON file."""
        write_json(analysis, output_path)


class CourseMapGenerator:
    """Generate detailed course structure maps."""

    @staticmethod
    def truncate_text(text: str, limit: int = 120) -> str:
        """Truncate text to limit with ellipsis."""
        if not isinstance(text, str):
            return ""
        text = " ".join(text.split())
        if len(text) > limit:
            return text[:limit] + "..."
        return text

    @staticmethod
    def format_separator() -> str:
        """Generate visual separator."""
        return "=" * 80

    def generate_course_map(self, course_data: Dict[str, Any]) -> str:
        """Generate detailed course structure map."""
        lines = []
        lines.append(self.format_separator())
        lines.append("CURSO - MAPA DETALHADO")
        lines.append(self.format_separator())
        lines.append("")

        course_info = course_data.get("course", {})
        lessons = course_info.get("lessons", [])

        for lesson_num, lesson in enumerate(lessons, start=1):
            lines.append(self.format_separator())
            lines.append(
                f"Lição {lesson_num}: {lesson.get(TITLE_FIELD, 'Sem título')}"
            )
            lines.append(self.format_separator())

            self._traverse_and_format(
                lesson,
                lines,
                lesson_num,
                lesson.get(TITLE_FIELD, f"Licao {lesson_num}")
            )
            lines.append("")

        return "\n".join(lines)

    def _traverse_and_format(
        self,
        obj: Any,
        lines: list,
        lesson_num: int,
        lesson_title: str,
        depth: int = 0
    ) -> None:
        """Recursively traverse and format course structure."""
        if isinstance(obj, dict):
            content_type = obj.get(CONTENT_TYPE_FIELD, None)

            if CONTENT_TYPE_FIELD in obj:
                indent = "  " * depth
                lines.append(
                    f"{indent}→ {content_type}: "
                    f"{self.truncate_text(str(obj.get('value', '')))}"
                )

            for key, value in obj.items():
                if key not in [CONTENT_TYPE_FIELD]:
                    self._traverse_and_format(
                        value,
                        lines,
                        lesson_num,
                        lesson_title,
                        depth + 1
                    )

        elif isinstance(obj, list):
            for item in obj:
                self._traverse_and_format(
                    item,
                    lines,
                    lesson_num,
                    lesson_title,
                    depth
                )

    def save_course_map(
        self,
        course_data: Dict[str, Any],
        output_path: Path
    ) -> None:
        """Generate and save course map to text file."""
        map_text = self.generate_course_map(course_data)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(map_text, encoding=DEFAULT_ENCODING)
