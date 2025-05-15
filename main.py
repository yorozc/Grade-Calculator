from fileProcessor import fileprocessor

class Main:
    def main():
        gradeFile = input("Please insert grade file: ")
        gradeResult = fileprocessor(gradeFile) #passes string of text file
        gradeResult.rescaleAndCreate()

if __name__ == "__main__":
    Main.main()