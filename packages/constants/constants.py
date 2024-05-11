"""
This module contains all the constants used in the application.
These constants can be imported and used throughout the project to maintain
consistency and ease of updates.
"""

from typing import final
from pathlib import Path


BASE_FOLDER: final(Path) = Path(__file__).resolve().parent.parent.parent
RESOURCES_FOLDER: final(Path) = Path.joinpath(BASE_FOLDER, "resources")
ICONS_FOLDER: final(Path) = Path.joinpath(RESOURCES_FOLDER, "icons")
ICONS: final(dict) = {icon_path.stem: str(icon_path) for icon_path in ICONS_FOLDER.iterdir()}
STYLE_FOLDER: final(Path) = Path.joinpath(RESOURCES_FOLDER, "style")
STYLE: final(Path) = Path.joinpath(STYLE_FOLDER, "style.qss")
