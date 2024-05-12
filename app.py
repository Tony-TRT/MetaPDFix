"""
Main application file.
"""

import pdfrw
from PySide6 import QtWidgets

from packages.ui.aesthetic import AestheticWindow
from packages.logic import toolkit


class MainWindow(AestheticWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("MetaPDFix")
        self.setFixedSize(500, 550)

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
        self.lbl_filename = None
        self.lbl_title = None
        self.lbl_author = None
        self.lbl_creation_date = None
        self.lbl_subject = None
        self.lbl_modification_date = None
        self.lbl_creator = None
        self.lbl_producer = None
        self.le_filename = None
        self.le_title = None
        self.le_author = None
        self.le_creation_date = None
        self.le_subject = None
        self.le_modification_date = None
        self.le_creator = None
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

        self.setWindowIcon(self.icons.get("logo"))
        self.btn_open.setIcon(self.icons.get("open"))
        self.btn_clear.setIcon(self.icons.get("clear"))
        self.btn_save.setIcon(self.icons.get("save"))

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

        self.btn_open = QtWidgets.QPushButton("Open")
        self.btn_clear = QtWidgets.QPushButton("Clear")
        self.btn_save = QtWidgets.QPushButton("Save")
        self.lbl_filename = QtWidgets.QLabel("Filename")
        self.lbl_title = QtWidgets.QLabel("Title")
        self.lbl_author = QtWidgets.QLabel("Author")
        self.lbl_creation_date = QtWidgets.QLabel("Creation date")
        self.lbl_subject = QtWidgets.QLabel("Subject")
        self.lbl_modification_date = QtWidgets.QLabel("Modification date")
        self.lbl_creator = QtWidgets.QLabel("Creator")
        self.lbl_producer = QtWidgets.QLabel("Producer")
        self.le_filename = QtWidgets.QLineEdit()
        self.le_title = QtWidgets.QLineEdit()
        self.le_author = QtWidgets.QLineEdit()
        self.le_creation_date = QtWidgets.QLineEdit()
        self.le_subject = QtWidgets.QLineEdit()
        self.le_modification_date = QtWidgets.QLineEdit()
        self.le_creator = QtWidgets.QLineEdit()
        self.le_producer = QtWidgets.QLineEdit()

        self.btn_layout.addWidget(self.btn_open)
        self.btn_layout.addWidget(self.btn_clear)
        self.btn_layout.addWidget(self.btn_save)
        self.left_tg_layout.addWidget(self.lbl_filename)
        self.left_tg_layout.addWidget(self.le_filename)
        self.left_tg_layout.addWidget(self.lbl_author)
        self.left_tg_layout.addWidget(self.le_author)
        self.left_tg_layout.addWidget(self.lbl_subject)
        self.left_tg_layout.addWidget(self.le_subject)
        self.left_tg_layout.addWidget(self.lbl_creator)
        self.left_tg_layout.addWidget(self.le_creator)
        self.right_tg_layout.addWidget(self.lbl_title)
        self.right_tg_layout.addWidget(self.le_title)
        self.right_tg_layout.addWidget(self.lbl_creation_date)
        self.right_tg_layout.addWidget(self.le_creation_date)
        self.right_tg_layout.addWidget(self.lbl_modification_date)
        self.right_tg_layout.addWidget(self.le_modification_date)
        self.right_tg_layout.addWidget(self.lbl_producer)
        self.right_tg_layout.addWidget(self.le_producer)

    def logic_clear_tags(self):

        ...

    def logic_connect_widgets(self) -> None:
        """Connections are managed here."""

        self.btn_open.clicked.connect(self.logic_open_file)
        self.btn_clear.clicked.connect(self.logic_clear_tags)
        self.btn_save.clicked.connect(self.logic_save_file)

    def logic_open_file(self) -> None:
        """Opens a file dialog to select a PDF file and updates the UI with the selected file's tags."""

        caption: str = "Select PDF File"
        file_filter: str = "PDF Files (*.pdf)"
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption=caption, dir="", filter=file_filter)

        if toolkit.check_file(file=file):
            validated_file: pdfrw.PdfReader = pdfrw.PdfReader(file)
            self.ui_update_tags(file=validated_file)

    def logic_save_file(self):

        ...


if __name__ == '__main__':
    root = QtWidgets.QApplication()
    application = MainWindow()
    application.show()
    root.exec()
