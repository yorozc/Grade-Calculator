class fileprocessor:

    def __init__(self, file):
        self.file = file

    def processFile(self):
        with open(self.file) as file:
            print(file.read())

    def createsResult(self):
        pass

    def operations(self):
        pass
