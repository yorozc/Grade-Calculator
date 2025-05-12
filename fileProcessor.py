class fileprocessor:

    def __init__(self, file):
        self.file = file

    def processFile(self): #parses file
        try:
            with open(self.file) as file:
                print(file.read())
        except FileNotFoundError:
            print("FILE NOT FOUND")

    def createsResult(self): #creates result.txt
        pass

    def processAndResults(self):
        self.processFile()
        self.createsResult()
