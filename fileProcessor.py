class fileprocessor:

    def __init__(self, file):
        self.file = file

    def processFile(self): #parses file
        with open(self.file) as file:
            print(file.read())

    def createsResult(self): #creates result.txt
        pass

    def processAndResults(self):
        self.processFile()
        self.createsResult()
