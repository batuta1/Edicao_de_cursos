"""Application settings and environment configuration."""

import os
from pathlib import Path
from enum import Enum
from typing import Optional


class LogLevel(Enum):
    """Logging levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Settings:
    """Centralized settings for the application."""

    def __init__(self):
        """Initialize settings from environment or defaults."""
        # Repo structure
        self.REPO_ROOT = Path(__file__).parent.parent.parent
        self.SRC_DIR = self.REPO_ROOT / "2_src"
        self.DATA_DIR = self.REPO_ROOT / "3_scorm"

        # Logging
        self.LOG_LEVEL = LogLevel[
            os.getenv("LOG_LEVEL", "INFO")
        ]

        # Paths
        self.SCORM_RAW_PACKAGES = os.getenv(
            "SCORM_RAW_PACKAGES",
            str(self.DATA_DIR / "raw_packages")
        )
        self.SCORM_PROCESSED = os.getenv(
            "SCORM_PROCESSED",
            str(self.DATA_DIR / "processed")
        )
        self.TEMP_DIR = os.getenv(
            "TEMP_DIR",
            str(self.REPO_ROOT / ".tmp")
        )

    def get_repo_root(self) -> Path:
        """Get absolute repository root path."""
        return self.REPO_ROOT

    def get_data_dir(self) -> Path:
        """Get absolute data directory path."""
        return self.DATA_DIR

    def validate_env(self) -> bool:
        """Validate that required directories exist or can be created."""
        try:
            Path(self.SCORM_RAW_PACKAGES).mkdir(parents=True, exist_ok=True)
            Path(self.SCORM_PROCESSED).mkdir(parents=True, exist_ok=True)
            Path(self.TEMP_DIR).mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            print(f"Failed to validate environment: {e}")
            return False


# Global settings instance
settings = Settings()
