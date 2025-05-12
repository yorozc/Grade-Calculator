from fileProcessor import fileprocessor

class Main:

    def main():
        gradeFile = input("Please insert grade file: ")
        gradeResult = fileprocessor(gradeFile) #passes string
        gradeResult.processFile()

    if __name__ == "__main__":
        main()