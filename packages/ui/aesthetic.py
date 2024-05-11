"""
This module provides utility functions for managing the appearance of the user interface.
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from packages.constants import constants


class AestheticWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.icons: dict = {icon_name: QIcon(icon_path) for icon_name, icon_path in constants.ICONS.items()}

        if constants.STYLE.exists():
            self.ui_apply_style()

    def ui_apply_style(self) -> None:
        """Loads application style."""

        with open(constants.STYLE, "r", encoding="UTF-8") as style:
            self.setStyleSheet(style.read())
