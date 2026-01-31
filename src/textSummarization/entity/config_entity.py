from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    unzip_data_dir: Path
    all_required_files: list
