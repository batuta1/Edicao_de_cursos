"""Reconstruct SCORM courses from edited lessons."""

import json
import base64
import re
import copy
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

from .models import Lesson
from ..config.paths import ScormPaths
from ..config.constants import (
    DEFAULT_ENCODING,
    JSON_INDENT,
    ENSURE_ASCII,
    BASE64_PADDING_CHAR,
)
from ..utils.file_utils import read_json, write_json, write_base64_file


class CourseSerializer:
    """Reconstructs a course from edited lessons."""

    def __init__(self, paths: ScormPaths):
        """Initialize serializer with path configuration."""
        self.paths = paths

    def load_edited_lessons(self, course_name: str) -> List[Dict[str, Any]]:
        """Load all edited lesson files from disk."""
        lessons_dir = self.paths.get_lessons_dir(course_name)
        lessons = []

        for lesson_file in sorted(lessons_dir.glob("licao_*.json")):
            # Skip index file
            if lesson_file.name == "indice_licoes.json":
                continue

            lesson_data = read_json(lesson_file)

            # Validate structure
            if "lesson" not in lesson_data:
                raise ValueError(
                    f"File {lesson_file.name} missing 'lesson' field"
                )

            lessons.append({
                "numero_da_licao": lesson_data.get("numero_da_licao"),
                "position_original": lesson_data.get("position_original"),
                "lesson": lesson_data["lesson"],
                "arquivo": lesson_file.name,
            })

        # Sort by lesson number
        lessons.sort(key=lambda x: x.get("numero_da_licao", 9999))

        return lessons

    def serialize_course(
        self,
        original_course_path: Path,
        course_name: str
    ) -> Dict[str, Any]:
        """Reconstruct course from original template and edited lessons."""
        # Load original course as template
        original_data = read_json(original_course_path)

        # Load edited lessons
        edited_lessons = self.load_edited_lessons(course_name)

        # Make a copy to avoid modifying original
        course_data = copy.deepcopy(original_data)

        # Extract lesson content only
        new_lessons = [item["lesson"] for item in edited_lessons]

        # Warn if lesson count changed
        original_count = len(course_data.get("course", {}).get("lessons", []))
        edited_count = len(new_lessons)

        if original_count != edited_count:
            print(f"WARNING: Lesson count changed.")
            print(f"  Original: {original_count}")
            print(f"  Edited: {edited_count}")

        # Replace lessons in course
        course_data["course"]["lessons"] = new_lessons

        return course_data

    def save_course_json(
        self,
        course_data: Dict[str, Any],
        course_name: str
    ) -> Path:
        """Save reconstructed course to JSON file."""
        output_path = self.paths.get_edited_course_json_path(course_name)
        write_json(course_data, output_path)
        return output_path

    @staticmethod
    def fix_base64_padding(text: str) -> str:
        """Add proper base64 padding."""
        return text + BASE64_PADDING_CHAR * (-len(text) % 4)

    @staticmethod
    def is_valid_course_base64(text: str) -> bool:
        """Check if text is valid base64-encoded course data."""
        try:
            corrected = CourseSerializer.fix_base64_padding(text)
            json_text = base64.b64decode(corrected).decode(DEFAULT_ENCODING)
            obj = json.loads(json_text)

            return (
                isinstance(obj, dict)
                and "course" in obj
                and isinstance(obj["course"], dict)
                and "lessons" in obj["course"]
            )
        except Exception:
            return False

    def encode_to_base64(
        self,
        course_data: Dict[str, Any],
        course_name: str
    ) -> Path:
        """Encode course to base64 and save to file."""
        json_compact = json.dumps(
            course_data,
            ensure_ascii=ENSURE_ASCII,
            separators=(",", ":")
        )

        base64_encoded = base64.b64encode(
            json_compact.encode(DEFAULT_ENCODING)
        ).decode(DEFAULT_ENCODING)

        output_path = self.paths.get_base64_export_path(course_name)
        write_base64_file(base64_encoded, output_path)

        return output_path

    def find_base64_in_html(
        self,
        html_path: Path
    ) -> Optional[str]:
        """Find base64-encoded course in HTML file."""
        if not html_path.exists():
            return None

        html = html_path.read_text(encoding=DEFAULT_ENCODING)

        # Find large base64 blocks (courses are >1000 chars)
        candidates = re.findall(r"[A-Za-z0-9+/=]{1000,}", html)

        for candidate in candidates:
            if self.is_valid_course_base64(candidate):
                return candidate

        return None

    def update_html_with_base64(
        self,
        html_path: Path,
        base64_encoded: str,
        output_path: Path
    ) -> bool:
        """Replace base64 in HTML file and save updated version."""
        found_base64 = self.find_base64_in_html(html_path)

        if not found_base64:
            print(f"Could not find course base64 in {html_path}")
            return False

        html = html_path.read_text(encoding=DEFAULT_ENCODING)
        updated_html = html.replace(found_base64, base64_encoded, 1)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(updated_html, encoding=DEFAULT_ENCODING)

        return True

    def full_serialize_and_export(
        self,
        original_course_path: Path,
        course_name: str,
        html_source_path: Optional[Path] = None
    ) -> Dict[str, Path]:
        """
        Complete serialization pipeline:
        1. Reconstruct course from lessons
        2. Save to JSON
        3. Encode to base64
        4. Optionally update HTML

        Returns:
            Dictionary with output file paths.
        """
        outputs = {}

        # Step 1: Reconstruct course
        course_data = self.serialize_course(original_course_path, course_name)

        # Step 2: Save JSON
        json_path = self.save_course_json(course_data, course_name)
        outputs["json"] = json_path

        # Step 3: Encode to base64
        base64_path = self.encode_to_base64(course_data, course_name)
        outputs["base64"] = base64_path

        # Step 4: Update HTML if provided
        if html_source_path and html_source_path.exists():
            base64_content = base64_path.read_text(encoding=DEFAULT_ENCODING)
            html_output = self.paths.get_course_dir(course_name) / "index_editado.html"

            if self.update_html_with_base64(html_source_path, base64_content, html_output):
                outputs["html"] = html_output

        return outputs
