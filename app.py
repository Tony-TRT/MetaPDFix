"""
Main application file.
"""

from PySide6 import QtWidgets

from packages.ui.aesthetic import AestheticWindow


class MainWindow(AestheticWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("MetaPDFix")
        self.setFixedSize(500, 600)

        ##################################################
        # Layouts.
        ##################################################

        self.main_layout = None
        self.btn_layout = None
        self.main_tg_layout = None
        self.left_tg_layout = None
        self.right_tg_layout = None

        self.ui_manage_layouts()

        ##################################################
        # Widgets.
        ##################################################

        self.btn_open = None
        self.btn_clear = None
        self.btn_save = None
        self.lbl_title = None
        self.lbl_author = None
        self.lbl_subject = None
        self.lbl_creator = None
        self.lbl_creation_date = None
        self.lbl_modification_date = None
        self.lbl_producer = None
        self.le_title = None
        self.le_author = None
        self.le_subject = None
        self.le_creator = None
        self.le_creation_date = None
        self.le_modification_date = None
        self.le_producer = None

        self.ui_manage_widgets()

        ##################################################
        # Icons.
        ##################################################

        self.ui_manage_icons()

        ##################################################
        # Connections.
        ##################################################

        self.logic_connect_widgets()

    def ui_manage_icons(self) -> None:
        """Icons are managed here."""

        ...

    def ui_manage_layouts(self) -> None:
        """Layouts are managed here."""

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.btn_layout = QtWidgets.QHBoxLayout()
        self.main_tg_layout = QtWidgets.QHBoxLayout()
        self.left_tg_layout = QtWidgets.QVBoxLayout()
        self.right_tg_layout = QtWidgets.QVBoxLayout()

        self.main_layout.addLayout(self.btn_layout)
        self.main_layout.addLayout(self.main_tg_layout)
        self.main_tg_layout.addLayout(self.left_tg_layout)
        self.main_tg_layout.addLayout(self.right_tg_layout)

    def ui_manage_widgets(self) -> None:
        """Widgets are managed here."""

        ...

    def logic_connect_widgets(self) -> None:
        """Connections are managed here."""

        ...


if __name__ == '__main__':
    root = QtWidgets.QApplication()
    application = MainWindow()
    application.show()
    root.exec()
