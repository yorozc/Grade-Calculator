class fileprocessor:

    def __init__(self, file):
        self.file = file
        self.weights = { #category, weights
            "HW": 0.25,
            "QUIZ": 0.25,
            "EXAM": 0.35,
            "PROJECT": 0.15
        }
        self.weightTotal = 100

    def processFile(self): #parses file
        try:
            weightedGrades = []
            with open(self.file, 'r') as file:
                for line in file:
                    #print(line, end="")
                    gradeList = line.split() #makes string an array
                    category = gradeList[0].upper() #dict key
                    grades = gradeList[1:] #list of grades
                    self.weightRescale(category, grades)
                    weight = self.calculateWeights(category, grades)
                    weightedGrades.append(weight)
                    self.printWeights()
            return weightedGrades
            
        except FileNotFoundError:
            print("FILE NOT FOUND")

    def createsResult(self): #creates result.txt
        weightedGrades = self.processFile() #list of weights
        result = 0
        for i in range(len(weightedGrades)): #totals up weighted grades
            result += weightedGrades[i]
        
        with open("result.txt", "w") as file:
            finalScore = "Final Score: " + str(round(result,2))
            file.write(finalScore)
            print("result.txt has been created or overwritten!")

    def calculateWeights(self, category, grades): #calculate individual weighted grade
        totalGrades = 0 
        average = 0
        weightedGrade = 0
        for i in range(len(grades)): #total grades 
            totalGrades += int(grades[i])
        
        if (len(grades) != 0):
            average = totalGrades / len(grades) 
            weightedGrade = average * self.weights[category]

        return weightedGrade

    def weightRescale(self, category, grades):
        if len(grades) == 0:
            if category in self.weights:
                self.weights[category] = 0.0

    def printWeights(self):
        print(self.weights)
