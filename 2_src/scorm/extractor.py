"""Extract lessons from SCORM courses into individual files."""

import json
import re
from pathlib import Path
from typing import List, Dict, Any

from .models import Lesson, Course
from ..config.paths import ScormPaths
from ..config.constants import (
    DEFAULT_ENCODING,
    INVALID_FILENAME_CHARS,
    WHITESPACE_COLLAPSE,
    MAX_FILENAME_LENGTH,
    JSON_INDENT,
    ENSURE_ASCII,
    POSITION_FIELD,
    TITLE_FIELD,
)


class LessonExtractor:
    """Extracts lessons from a course and saves them as individual files."""

    def __init__(self, paths: ScormPaths):
        """Initialize extractor with path configuration."""
        self.paths = paths

    @staticmethod
    def sanitize_filename(text: str) -> str:
        """Remove invalid characters from filename."""
        text = text.strip()
        text = re.sub(INVALID_FILENAME_CHARS, "", text)
        text = re.sub(WHITESPACE_COLLAPSE, "_", text)
        return text[:MAX_FILENAME_LENGTH]

    def extract_from_file(
        self,
        course_json_path: Path,
        course_name: str
    ) -> List[Lesson]:
        """Extract lessons from course JSON file."""
        with open(course_json_path, "r", encoding=DEFAULT_ENCODING) as f:
            data = json.load(f)
        return self.extract_from_data(data, course_name)

    def extract_from_data(
        self,
        course_data: Dict[str, Any],
        course_name: str
    ) -> List[Lesson]:
        """Extract lessons from course data dictionary."""
        lessons_data = course_data.get("course", {}).get("lessons", [])

        # Sort by position
        lessons_sorted = sorted(
            lessons_data,
            key=lambda x: x.get(POSITION_FIELD, 0)
        )

        # Create lesson objects
        lessons = []
        for numero, lesson_data in enumerate(lessons_sorted, start=1):
            lesson = Lesson(
                numero=numero,
                position=lesson_data.get(POSITION_FIELD, numero),
                title=lesson_data.get(TITLE_FIELD, f"licao_{numero}"),
                content=lesson_data,
            )
            lessons.append(lesson)

        return lessons

    def save_to_files(
        self,
        lessons: List[Lesson],
        course_name: str
    ) -> Path:
        """Save lessons to individual JSON files."""
        output_dir = self.paths.get_lessons_dir(course_name)
        output_dir.mkdir(parents=True, exist_ok=True)

        index = []

        for lesson in lessons:
            # Sanitize title for filename
            clean_title = self.sanitize_filename(lesson.title)
            filename = f"licao_{lesson.numero:02d}_{clean_title}.json"
            filepath = output_dir / filename

            # Save individual lesson
            with open(filepath, "w", encoding=DEFAULT_ENCODING) as f:
                json.dump(
                    lesson.to_dict(),
                    f,
                    ensure_ascii=ENSURE_ASCII,
                    indent=JSON_INDENT
                )

            # Add to index
            index.append({
                "numero_da_licao": lesson.numero,
                "position_original": lesson.position,
                "title": lesson.title,
                "arquivo": filename,
            })

        # Save index file
        index_path = self.paths.get_lessons_index_path(course_name)
        with open(index_path, "w", encoding=DEFAULT_ENCODING) as f:
            json.dump(
                index,
                f,
                ensure_ascii=ENSURE_ASCII,
                indent=JSON_INDENT
            )

        return output_dir

    def extract_and_save(
        self,
        course_json_path: Path,
        course_name: str
    ) -> Path:
        """Extract lessons and save to files in one operation."""
        lessons = self.extract_from_file(course_json_path, course_name)
        return self.save_to_files(lessons, course_name)
