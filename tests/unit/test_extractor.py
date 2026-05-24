"""Tests for lesson extractor."""

import json
from pathlib import Path

import pytest

from _src.scorm.extractor import LessonExtractor


class TestLessonExtractor:
    """Test LessonExtractor class."""

    def test_sanitize_filename_removes_invalid_chars(self):
        """Test filename sanitization."""
        test_cases = [
            ('Lesson: Test*2024.txt', 'Lesson_Test2024.txt'),
            ('File/Path\\Name', 'FilePathName'),
            ('Multiple   Spaces', 'Multiple_Spaces'),
        ]

        for input_text, expected in test_cases:
            result = LessonExtractor.sanitize_filename(input_text)
            assert expected in result or result.startswith(expected.split('_')[0])

    def test_sanitize_filename_limits_length(self):
        """Test filename length limit."""
        long_name = 'a' * 200
        result = LessonExtractor.sanitize_filename(long_name)
        assert len(result) <= 80

    def test_extract_from_data_creates_lessons(self, sample_course_data):
        """Test extracting lessons from course data."""
        paths = None  # Not needed for from_data
        extractor = LessonExtractor(paths)

        lessons = extractor.extract_from_data(sample_course_data, "test_course")

        assert len(lessons) == 2
        assert lessons[0].numero == 1
        assert lessons[0].title == "Lesson 1"
        assert lessons[1].numero == 2
        assert lessons[1].title == "Lesson 2"

    def test_extract_from_data_sorts_by_position(self):
        """Test lessons are sorted by position."""
        course_data = {
            "course": {
                "lessons": [
                    {"position": 3, "title": "Third"},
                    {"position": 1, "title": "First"},
                    {"position": 2, "title": "Second"},
                ],
            }
        }

        extractor = LessonExtractor(None)
        lessons = extractor.extract_from_data(course_data, "test")

        assert lessons[0].title == "First"
        assert lessons[1].title == "Second"
        assert lessons[2].title == "Third"

    def test_save_to_files_creates_lesson_files(self, scorm_paths, sample_course_data):
        """Test saving lessons to files."""
        extractor = LessonExtractor(scorm_paths)
        lessons = extractor.extract_from_data(sample_course_data, "test_course")

        output_dir = extractor.save_to_files(lessons, "test_course")

        # Check directory structure
        assert output_dir.exists()
        lesson_files = list(output_dir.glob("licao_*.json"))
        assert len(lesson_files) == 2

        # Check index file
        index_file = output_dir / "indice_licoes.json"
        assert index_file.exists()

        with open(index_file, "r") as f:
            index = json.load(f)
        assert len(index) == 2
