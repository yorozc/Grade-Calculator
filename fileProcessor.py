class fileprocessor:

    def __init__(self, file):
        self.file = file
        self.weights = { #category, weights
            "HW": 25,
            "QUIZ": 25,
            "EXAM": 35,
            "PROJECT": 15
        }

    def processFile(self): #parses file
        try:
            gradesDict = {}
            with open(self.file, 'r') as file:
                for line in file: 
                    gradeList = line.split() 
                    category = gradeList[0].upper() 
                    grades = gradeList[1:] 
                    gradesDict[category] = grades

            return gradesDict
            
        except FileNotFoundError:
            print("FILE NOT FOUND")

    def createsResult(self): #creates result.txt
        weightedGrades = self.calculateGrade() #list of weighted grades
        result = sum([grade for grade in weightedGrades])
        
        with open("result.txt", "w") as file:
            finalScore = "Final Score: " + str(round(result,2))
            file.write(finalScore)
            print("result.txt has been created or overwritten!")

    def calculateGrade(self): #calculate individual weighted grade
        gradesDict = self.processFile() #might be removed
        totalGrades = 0 
        average = 0
        weightedGrade = 0
        
        for i in range(len(grades)): #total grades 
            totalGrades += int(grades[i])
        
        if (len(grades) != 0):
            average = totalGrades / len(grades) # average of all grades for that category
            weightedGrade = average * self.weights[category]

        return weightedGrade

    def weightRescale(self):
        gradesDict = self.processFile()
        newSum = 0
        for key, val in gradesDict.items():
            if len(val) == 0: #checks which category doesnt have a list
                newSum = 100 - self.weights[key]
                self.weights[key] = 0.0

        for key, val in self.weights.items(): #changes weights in constructor
            self.weights[key] =  round((val / newSum) * 100, 2)

    def printWeights(self):
        print(self.weights)

    def wrapper(self):
        self.printWeights()
        self.weightRescale()
        self.printWeights()
        self.createsResult()