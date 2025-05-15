class fileprocessor:

    def __init__(self, file):
        self.file = file
        self.weights = { #category, weights
            "HW": 0.25,
            "QUIZ": 0.25,
            "EXAM": 0.35,
            "PROJECT": 0.15
        }
        self.grades = {}

    def processFile(self): #parses file
        try:
            with open(self.file, 'r') as file:
                for line in file: 
                    gradeList = line.split() 
                    category = gradeList[0].upper() 
                    grades = gradeList[1:] 
                    self.grades[category] = grades #adds to self.grades

                    #weight = self.calculateGrade(category, grades)
                    #weightedGrades.append(weight)

            self.printWeights()
            print(self.grades)
            
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
        pass
    # figure out way to rescale weights right at the beginning

    def printWeights(self):
        print(self.weights)

    def wrapper(self):
        self.weightRescale()
        self.createsResult()