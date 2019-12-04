import sys

class CsvRead:
    def __init__(self, fileName):
        self.fileName = fileName
        self.file = None
        self.linesFromFile = []

        self.timeStamp_Column = -1
        self.open_Column = -1
        self.high_Column = -1
        self.low_Column = -1
        self.close_Column = -1
        self.adjustedClose_Column = -1
        self.volume_Column = -1
        self.dividendAmount_Column = -1
        self.splitCoefficient_Column = -1

        self.file = open(self.fileName, "r")

    def __str__(self):
        myString = ""
        myString += "timestamp:" + str(self.timeStamp_Column) + '\n'
        myString += "open:" + str(self.open_Column) + '\n'
        myString += "high:" + str(self.high_Column) + '\n'
        myString += "low:" + str(self.low_Column) + '\n'
        myString += "close:" + str(self.close_Column) + '\n'
        myString += "adjusted_close:" + str(self.adjustedClose_Column) + '\n'
        myString += "volume:" + str(self.volume_Column) + '\n'
        myString += "dividend_amount:" + str(self.dividendAmount_Column) + '\n'
        myString += "split_coefficient:" + str(self.splitCoefficient_Column) + '\n'

        return myString


    def setColumns(self, line):
        columns = line.split(',')
        i = 0
        for var in columns:
            # remove the newline char for the last column and any other whitespace
            var = var.rstrip()
            if var == "timestamp":
                self.timeStamp_Column = i
            elif var == "open":
                self.open_Column = i
            elif var == "high":
                self.high_Column = i
            elif var == "low":
                self.low_Column = i
            elif var == "close":
                self.close_Column = i
            elif var == "adjusted_close":
                self.adjustedClose_Column = i
            elif var == "volume":
                self.volume_Column = i
            elif var == "dividend_amount":
                self.dividendAmount_Column = i
            elif var == "split_coefficient":
                self.splitCoefficient_Column = i
            i += 1

    def parseFileToLines(self):
        firstLine = self.file.readline()
        self.setColumns(firstLine)

    def getLines(self):
        i = 0
        for row in self.file:
            self.linesFromFile.append(row)

    def closeFile(self):
        self.file.close()


if __name__ == "__main__":
    inputFile = sys.argv[1]
    myRead = CsvRead(inputFile)
    myRead.parseFileToLines()
    myRead.getLines()
    print("Number of lines: " + str(len(myRead.linesFromFile)))
    print(myRead.linesFromFile[0])
    myRead.closeFile()
