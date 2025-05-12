class fileprocessor:

    def __init__(self, file):
        self.file = file
        self.weights = {
            "HW": 0.25,
            "QUIZ": 0.25,
            "EXAM": 0.35,
            "PROJECT": 0.15
        }

    def processFile(self): #parses file
        try:
            with open(self.file, 'r') as file:
                for line in file:
                    #print(line, end="")
                    gradeList = line.split() #makes string an array
                    category = gradeList[0].upper()
                    grades = gradeList[1:]
                    print(grades)
                    if category in self.weights:
                        print(self.weights[category])
                #separate first characters up until first white space
            

        except FileNotFoundError:
            print("FILE NOT FOUND")

    def createsResult(self): #creates result.txt
        pass

    def calculateWeights(self):
        pass

    def processAndResults(self):
        self.processFile()
        self.createsResult()
