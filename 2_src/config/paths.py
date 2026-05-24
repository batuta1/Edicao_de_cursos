"""Path management for SCORM data and processing."""

from pathlib import Path
from typing import Optional
from .settings import settings


class ScormPaths:
    """Centralized path management for SCORM processing."""

    def __init__(self, settings_override: Optional[object] = None):
        """Initialize with settings."""
        self.settings = settings_override or settings
        self._ensure_directories()

    def _ensure_directories(self) -> None:
        """Create required directories if they don't exist."""
        self.get_raw_packages_dir().mkdir(parents=True, exist_ok=True)
        self.get_processed_dir().mkdir(parents=True, exist_ok=True)
        self.get_temp_dir().mkdir(parents=True, exist_ok=True)

    # Root directories
    def get_raw_packages_dir(self) -> Path:
        """Get path to raw SCORM packages (immutable source)."""
        return Path(self.settings.SCORM_RAW_PACKAGES)

    def get_processed_dir(self) -> Path:
        """Get path to processed data (generated, not in git)."""
        return Path(self.settings.SCORM_PROCESSED)

    def get_temp_dir(self) -> Path:
        """Get path to temporary files."""
        return Path(self.settings.TEMP_DIR)

    # Raw package paths
    def get_raw_package_dir(self, package_name: str) -> Path:
        """Get path to specific raw SCORM package."""
        package_path = self.get_raw_packages_dir() / package_name
        if not package_path.exists():
            raise FileNotFoundError(
                f"Raw package not found: {package_path}"
            )
        return package_path

    def get_manifest_path(self, package_name: str) -> Path:
        """Get path to imsmanifest.xml in raw package."""
        return self.get_raw_package_dir(package_name) / "imsmanifest.xml"

    # Processed course paths
    def get_course_dir(self, course_name: str) -> Path:
        """Get path to processed course directory."""
        course_dir = self.get_processed_dir() / course_name
        course_dir.mkdir(parents=True, exist_ok=True)
        return course_dir

    def get_course_json_path(self, course_name: str) -> Path:
        """Get path to deserialized course JSON."""
        return self.get_course_dir(course_name) / "curso.json"

    def get_lessons_dir(self, course_name: str) -> Path:
        """Get path to extracted lessons directory."""
        lessons_dir = self.get_course_dir(course_name) / "licoes"
        lessons_dir.mkdir(parents=True, exist_ok=True)
        return lessons_dir

    def get_lessons_index_path(self, course_name: str) -> Path:
        """Get path to lessons index file."""
        return self.get_lessons_dir(course_name) / "indice_licoes.json"

    # Lesson file paths
    def get_lesson_file_path(
        self,
        course_name: str,
        lesson_number: int,
        lesson_title: str
    ) -> Path:
        """Get path for a specific lesson file."""
        # Format: licao_01_titulo.json
        # Sanitization handled by caller
        filename = f"licao_{lesson_number:02d}_{lesson_title}.json"
        return self.get_lessons_dir(course_name) / filename

    # Export/output paths
    def get_edited_course_json_path(self, course_name: str) -> Path:
        """Get path to edited/reconstructed course JSON."""
        return self.get_course_dir(course_name) / "curso_editado.json"

    def get_base64_export_path(self, course_name: str) -> Path:
        """Get path to base64-encoded course export."""
        return self.get_course_dir(course_name) / "curso_editado_base64.txt"

    # Analysis/report paths
    def get_course_map_path(self, course_name: str) -> Path:
        """Get path to course structure map (text)."""
        return self.get_course_dir(course_name) / "mapa_curso.txt"

    def get_type_analysis_path(self, course_name: str) -> Path:
        """Get path to content type analysis report."""
        return self.get_course_dir(course_name) / "analise_tipos.json"

    # Validation methods
    def validate_course_exists(self, course_name: str) -> bool:
        """Check if course has been deserialized."""
        return self.get_course_json_path(course_name).exists()

    def validate_lessons_exist(self, course_name: str) -> bool:
        """Check if lessons have been extracted."""
        lessons_dir = self.get_lessons_dir(course_name)
        return (
            lessons_dir.exists() and
            list(lessons_dir.glob("licao_*.json"))
        )
