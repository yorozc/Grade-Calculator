from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget,
                               QFileDialog)

from PySide6.QtGui import QIcon, QFont, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 150, 750, 750)
        self.setWindowTitle("CS3750 Grade Calculator")
        self.setWindowIcon(QIcon("pictures/cartoon-notebook-icon-png.png"))
        self.setStyleSheet("background-color: white;")
        self.inputFileButton = QPushButton("Select File", self)
        self.initUI()

    def initUI(self):
        #buttons
        self.inputFileButton.setGeometry(0, 0, 150, 50)
        self.inputFileButton.setStyleSheet("background-color: #55a7fa;" \
                                        "color: black;" \
                                        "font-size: 24px;" \
                                        "font-weight: bold;" \
                                        "border-radius: 8px;")
        self.inputFileButton.clicked.connect(self.inputFileButtonPressed)
        
    def inputFileButtonPressed(self):
        selectedfile = self.selectGradeFile()
        print("selected file: " + selectedfile)
        
    def selectGradeFile(self):
        filePath, _ = QFileDialog.getOpenFileName(
            None,
            "Select Grade File",
            "",
            "Text Files (*.txt)"
        )
        return filePath