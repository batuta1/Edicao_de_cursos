"""Tests for data models."""

import json

import pytest

from _src.scorm.models import Lesson, Course


class TestLesson:
    """Test Lesson model."""

    def test_lesson_creation(self):
        """Test creating a lesson."""
        lesson = Lesson(
            numero=1,
            position=1,
            title="Test",
            content={"type": "content"}
        )

        assert lesson.numero == 1
        assert lesson.title == "Test"

    def test_lesson_to_dict(self):
        """Test converting lesson to dictionary."""
        lesson = Lesson(
            numero=1,
            position=1,
            title="Test",
            content={"type": "content", "value": "test"}
        )

        result = lesson.to_dict()

        assert result["numero_da_licao"] == 1
        assert result["title"] == "Test"
        assert result["lesson"] == {"type": "content", "value": "test"}

    def test_lesson_from_dict(self):
        """Test creating lesson from dictionary."""
        data = {
            "numero_da_licao": 2,
            "position_original": 2,
            "title": "Lesson Two",
            "lesson": {"type": "activity"},
        }

        lesson = Lesson.from_dict(data)

        assert lesson.numero == 2
        assert lesson.title == "Lesson Two"


class TestCourse:
    """Test Course model."""

    def test_course_creation(self):
        """Test creating a course."""
        course = Course(name="Test Course")
        assert course.name == "Test Course"
        assert course.get_lesson_count() == 0

    def test_add_lesson(self):
        """Test adding lessons to course."""
        course = Course(name="Test")
        lesson = Lesson(1, 1, "L1", {})

        course.add_lesson(lesson)

        assert course.get_lesson_count() == 1

    def test_sort_lessons_by_position(self):
        """Test sorting lessons by position."""
        course = Course(name="Test")
        course.add_lesson(Lesson(1, 3, "L1", {}))
        course.add_lesson(Lesson(2, 1, "L2", {}))
        course.add_lesson(Lesson(3, 2, "L3", {}))

        course.sort_lessons_by_position()

        assert course.lessons[0].position == 1
        assert course.lessons[1].position == 2
        assert course.lessons[2].position == 3
