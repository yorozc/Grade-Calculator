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
                        "color: black;"
                        "border: none;"
                        "border-bottom: 0.5px solid grey;"
                        "}"
                        "QMainWindow{" \
                        "background-color: white;" \
                        "}"
                        "QLabel#resultNumber, QLabel#resultText{" \
                        "color: black;" \
                        "border: none;" \
                        "font-size: 32px;" \
                        "}" \
                        "QLabel#resultNumber{" \
                        "font-size: 48px" \
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

        self.categoryLayout = QVBoxLayout()
        self.resultLayout = QVBoxLayout()

        #Labels (Grades and results)
        hwGrade = QLabel("HW", self)
        hwGrade.setObjectName("HW")
        
        quizGrade = QLabel("Quiz", self)
        quizGrade.setObjectName("QUIZ")
        
        examGrade = QLabel("Exam", self)
        examGrade.setObjectName("EXAM")
        
        projectGrade = QLabel("Project", self)
        projectGrade.setObjectName("PROJECT")
        
        resultText = QLabel("Result", self)
        resultText.setObjectName("resultText")
        resultText.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        resultNumber = QLabel("", self)
        resultNumber.setObjectName("resultNumber")
        resultNumber.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        
        # adding widgets to layouts
        mainLayout.addWidget(self.inputFileButton, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        self.categoryLayout.addWidget(hwGrade)
        self.categoryLayout.addWidget(quizGrade)
        self.categoryLayout.addWidget(examGrade)
        self.categoryLayout.addWidget(projectGrade)

        self.resultLayout.addWidget(resultText)
        self.resultLayout.addWidget(resultNumber)

        mainLayout.addLayout(self.categoryLayout)
        mainLayout.addLayout(self.resultLayout)

        centralWidget.setLayout(mainLayout)
        
    def inputFileButtonPressed(self):
        selectedfile = self.selectGradeFile()
        print("selected file: " + selectedfile)
    
    def displayGrades(self, grades):
        i = 0
        for k,v in grades.items():
            item = self.categoryLayout.itemAt(i)
            if item.widget():
                widget = item.widget()
                if widget.objectName() == k and len(v) !=0:
                    widget.setText(f"{k}: {" ".join(v)}")
                else:
                    widget.setText(f"{k}: Empty Category")
            i+=1

    def displayResult(self, result):
        count = self.resultLayout.count()

        for i in range(count):
            item = self.resultLayout.itemAt(i)
            if item.widget:
                widget = item.widget()
                if widget.objectName() == "resultNumber":
                    widget.setText(f"{result}") 
                
                    
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
                result = gradeResult.createsResult()
                self.displayGrades(grades)
                self.displayResult(result)
                

            except Exception as e:
                print(f"An error has occured: {e}")

        return filePath