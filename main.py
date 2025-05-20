from fileProcessor import fileprocessor
from mainWindow import MainWindow
import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication

class Main:
    def main():
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec()

if __name__ == "__main__":
    Main.main()