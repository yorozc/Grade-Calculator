from fileProcessor import fileprocessor
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget,
                               QFileDialog, QGridLayout, QHBoxLayout)

from PySide6.QtGui import QIcon, QFont, QPixmap
from PySide6.QtCore import Qt

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
                                        "border-radius: 8px;"
                                        "padding: 12px;"
                                        )

        self.inputFileButton.clicked.connect(self.inputFileButtonPressed)

        #layout
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        mainLayout = QVBoxLayout()

        categoryLayout = QVBoxLayout()
        resultLayout = QHBoxLayout()

        #Labels (Grades and results)
        hwGrade = QLabel("HW", self)
        hwGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        quizGrade = QLabel("Quiz", self)
        quizGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        examGrade = QLabel("Exam", self)
        examGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        projectGrade = QLabel("Project", self)
        projectGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        
        result = QLabel("Result", self)
        result.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        
        mainLayout.addWidget(self.inputFileButton, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        categoryLayout.addWidget(hwGrade)
        categoryLayout.addWidget(quizGrade)
        categoryLayout.addWidget(examGrade)
        categoryLayout.addWidget(projectGrade)

        resultLayout.addWidget(result)

        mainLayout.addLayout(categoryLayout)
        mainLayout.addLayout(resultLayout)

        centralWidget.setLayout(mainLayout)
        

        
    def inputFileButtonPressed(self):
        selectedfile = self.selectGradeFile()
        print("selected file: " + selectedfile)

    def getGrades(self):
        gradesDict = fileprocessor.getGrades()
        return gradesDict
        
    def selectGradeFile(self):
        filePath, _ = QFileDialog.getOpenFileName(
            None,
            "Select Grade File",
            "",
            "Text Files (*.txt)"
        )
        if filePath:
            try:
                gradeResult = fileprocessor(filePath) #passes string of text file
                gradeResult.rescaleAndCreate()
            except:
                print("Invalid file. Text files only.")

        return filePath