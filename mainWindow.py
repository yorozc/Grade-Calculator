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
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        mainLayout = QVBoxLayout()

        self.categoryLayout = QVBoxLayout()
        resultLayout = QHBoxLayout()

        #Labels (Grades and results)
        hwGrade = QLabel("HW", self)
        hwGrade.setObjectName("HW")
        hwGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        
        quizGrade = QLabel("Quiz", self)
        quizGrade.setObjectName("QUIZ")
        quizGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        
        examGrade = QLabel("Exam", self)
        examGrade.setObjectName("EXAM")
        examGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        
        projectGrade = QLabel("Project", self)
        projectGrade.setObjectName("PROJECT")
        projectGrade.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        
        result = QLabel("Result", self)
        result.setStyleSheet("color: black;" \
                            "border: 1px solid red;")
        result.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        # adding widgets to layouts
        mainLayout.addWidget(self.inputFileButton, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        self.categoryLayout.addWidget(hwGrade)
        self.categoryLayout.addWidget(quizGrade)
        self.categoryLayout.addWidget(examGrade)
        self.categoryLayout.addWidget(projectGrade)

        resultLayout.addWidget(result)

        mainLayout.addLayout(self.categoryLayout)
        mainLayout.addLayout(resultLayout)

        self.centralWidget.setLayout(mainLayout)
        
    def inputFileButtonPressed(self):
        selectedfile = self.selectGradeFile()
        print("selected file: " + selectedfile)
    
    def displayGrades(self, grades):
        i = 0
        for k,v in grades.items():
            print(v)
            item = self.categoryLayout.itemAt(i)
            if item.widget():
                widget = item.widget()
                if widget.objectName() == k and len(v) !=0:
                    widget.setText(f"{k}: {" ".join(v)}")
                else:
                    widget.setText(f"{k}: Empty Category")
            i+=1
                    

        
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
                self.displayGrades(grades)

            except Exception as e:
                print(f"An error has occured: {e}")

        return filePath