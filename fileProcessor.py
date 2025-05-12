class fileprocessor:

    def __init__(self, file):
        self.file = file
        self.weights = { #grade weights
            "HW": 0.25,
            "QUIZ": 0.25,
            "EXAM": 0.35,
            "PROJECT": 0.15
        }

    def processFile(self): #parses file
        try:
            weightedGrades = []
            with open(self.file, 'r') as file:
                for line in file:
                    #print(line, end="")
                    gradeList = line.split() #makes string an array
                    category = gradeList[0].upper() #dict key
                    grades = gradeList[1:] #list of grades
                    weight = self.calculateWeights(category, grades)
                    weightedGrades.append(weight)

            return weightedGrades
            
        except FileNotFoundError:
            print("FILE NOT FOUND")

    def createsResult(self): #creates result.txt
        weightedGrades = self.processFile() #list of weights
        result = 0
        for i in range(len(weightedGrades)):
            result += weightedGrades[i]
        return result

    def calculateWeights(self, category, grades):
        #calculate total grade and return it
        totalCategoryWeight = 0 
        average = 0
        weightedGrade = 0
        for i in range(len(grades)): 
            totalCategoryWeight += int(grades[i])
        
        if (len(grades) != 0):
            average = totalCategoryWeight / len(grades) 
            weightedGrade = average * self.weights[category]

        return weightedGrade
            
    def weightRescale(self):
        pass

    def processAndResults(self):
        self.processFile()
        print(self.createsResult())
