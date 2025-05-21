from fileProcessor import fileprocessor
from mainWindow import MainWindow
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

class Main:
    def main():
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec()

if __name__ == "__main__":
    Main.main()