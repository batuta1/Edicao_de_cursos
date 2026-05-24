"""Data models for SCORM courses and lessons."""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, List, Optional
from pathlib import Path
import json

from ..config.constants import DEFAULT_ENCODING


@dataclass
class Lesson:
    """Represents a single lesson in a course."""

    numero: int
    position: int
    title: str
    content: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        """Convert lesson to dictionary."""
        return {
            "numero_da_licao": self.numero,
            "position_original": self.position,
            "title": self.title,
            "lesson": self.content,
        }

    def to_json(self) -> str:
        """Convert lesson to JSON string."""
        return json.dumps(
            self.to_dict(),
            ensure_ascii=False,
            indent=2
        )

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Lesson":
        """Create lesson from dictionary."""
        return Lesson(
            numero=data.get("numero_da_licao"),
            position=data.get("position_original"),
            title=data.get("title"),
            content=data.get("lesson", {}),
        )

    @staticmethod
    def from_file(filepath: Path) -> "Lesson":
        """Load lesson from JSON file."""
        with open(filepath, "r", encoding=DEFAULT_ENCODING) as f:
            data = json.load(f)
        return Lesson.from_dict(data)


@dataclass
class Course:
    """Represents a complete SCORM course."""

    name: str
    lessons: List[Lesson] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_lesson(self, lesson: Lesson) -> None:
        """Add lesson to course."""
        self.lessons.append(lesson)

    def sort_lessons_by_position(self) -> None:
        """Sort lessons by their original position."""
        self.lessons.sort(key=lambda l: l.position)

    def get_lesson_count(self) -> int:
        """Get number of lessons in course."""
        return len(self.lessons)

    def to_dict(self) -> Dict[str, Any]:
        """Convert course to dictionary."""
        return {
            "course": {
                "name": self.name,
                "lessons": [l.content for l in self.lessons],
                **self.metadata,
            }
        }

    def to_json(self) -> str:
        """Convert course to JSON string."""
        return json.dumps(
            self.to_dict(),
            ensure_ascii=False,
            indent=2
        )

    @staticmethod
    def from_dict(name: str, data: Dict[str, Any]) -> "Course":
        """Create course from dictionary."""
        course_data = data.get("course", {})
        lessons_data = course_data.get("lessons", [])

        course = Course(name=name)

        # Extract lessons
        for idx, lesson_data in enumerate(lessons_data, start=1):
            lesson = Lesson(
                numero=idx,
                position=lesson_data.get("position", idx),
                title=lesson_data.get("title", f"Lesson {idx}"),
                content=lesson_data,
            )
            course.add_lesson(lesson)

        # Store remaining metadata
        course.metadata = {
            k: v for k, v in course_data.items()
            if k not in ["lessons", "name"]
        }

        return course

    @staticmethod
    def from_file(name: str, filepath: Path) -> "Course":
        """Load course from JSON file."""
        with open(filepath, "r", encoding=DEFAULT_ENCODING) as f:
            data = json.load(f)
        return Course.from_dict(name, data)
