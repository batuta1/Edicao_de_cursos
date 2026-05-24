"""Pytest configuration and fixtures."""

import json
import tempfile
from pathlib import Path

import pytest

from _src.config.paths import ScormPaths
from _src.config.settings import Settings


@pytest.fixture
def temp_repo(tmp_path):
    """Create a temporary repository structure."""
    raw_packages = tmp_path / "3_scorm" / "raw_packages"
    processed = tmp_path / "3_scorm" / "processed"
    raw_packages.mkdir(parents=True)
    processed.mkdir(parents=True)
    return tmp_path


@pytest.fixture
def scorm_paths(temp_repo):
    """Provide ScormPaths with temporary directories."""
    class TempSettings:
        SCORM_RAW_PACKAGES = str(temp_repo / "3_scorm" / "raw_packages")
        SCORM_PROCESSED = str(temp_repo / "3_scorm" / "processed")
        TEMP_DIR = str(temp_repo / ".tmp")

    return ScormPaths(settings_override=TempSettings())


@pytest.fixture
def sample_course_data():
    """Sample course data for testing."""
    return {
        "course": {
            "name": "Test Course",
            "lessons": [
                {
                    "position": 1,
                    "title": "Lesson 1",
                    "type": "content",
                    "value": "Test content 1",
                },
                {
                    "position": 2,
                    "title": "Lesson 2",
                    "type": "activity",
                    "value": "Test activity 2",
                },
            ],
        }
    }


@pytest.fixture
def sample_lesson_file(tmp_path):
    """Create a sample lesson JSON file."""
    lesson_data = {
        "numero_da_licao": 1,
        "position_original": 1,
        "title": "Test Lesson",
        "lesson": {
            "type": "content",
            "value": "Test content",
        },
    }

    lesson_file = tmp_path / "licao_01_Test_Lesson.json"
    with open(lesson_file, "w", encoding="utf-8") as f:
        json.dump(lesson_data, f)

    return lesson_file
