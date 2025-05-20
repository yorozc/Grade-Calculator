from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget,
                               )

from PySide6.QtGui import QIcon, QFont, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 150, 750, 750)
        self.setWindowTitle("CS3750 Grade Calculator")
        self.setWindowIcon(QIcon("pictures/cartoon-notebook-icon-png.png"))