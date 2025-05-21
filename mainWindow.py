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
        self.inputFileButton = QPushButton("Select File", self)
        self.grades = {}
        self.initUI()

    def initUI(self):
        #buttons
        self.setStyleSheet("QLabel{" \
                        "font-size: 32px;"
                        "}"
                        "QMainWindow{" \
                        "background-color: white;" \
                        "}") 
        
        self.inputFileButton.setGeometry(0, 0, 150, 50)
        self.inputFileButton.setStyleSheet("background-color: #55a7fa;" \
                                        "color: black;" \
                                        "font-size: 24px;" \
                                        "font-weight: bold;" \
                                        "border-radius: 8px;"
                                        "padding: 12px;"
                                        "margin-top: 75px")

        self.inputFileButton.clicked.connect(self.inputFileButtonPressed)

        #layout
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        mainLayout = QVBoxLayout()

        categoryLayout = QVBoxLayout()
        resultLayout = QHBoxLayout()

        #Labels (Grades and results)
        self.hwGrade = QLabel("HW: ", self)

        self.hwGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        self.quizGrade = QLabel("Quiz: ", self)
        self.quizGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        self.examGrade = QLabel("Exam: ", self)
        self.examGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        self.projectGrade = QLabel("Project: ", self)
        self.projectGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        
        self.result = QLabel("Result", self)
        self.result.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        self.result.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        # adding widgets to layouts
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
    
    def setGrades(self, grades):
        self.grades = grades

    def printGrades(self):
        for k,v in self.grades.items():
            print(k, v)
        
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
                grades = gradeResult.getGrades()
                self.setGrades(grades)
                self.printGrades()

            except:
                print("Invalid file. Text files only.")

        return filePath