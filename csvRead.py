import sys

class CsvRead:
    def __init__(self, fileName):
        self._fileName = fileName
        self._file = None
        self._linesFromFile = []
        self._timeStamp_Column = -1
        self._open_Column = -1
        self._high_Column = -1
        self._low_Column = -1
        self._close_Column = -1
        self._adjustedClose_Column = -1
        self._volume_Column = -1
        self._dividendAmount_Column = -1
        self._splitCoefficient_Column = -1

        self._file = open(self._fileName, "r")

        #self._line = False

    def __str__(self):
        return self._timeStamp_Column self._open_Column
        print self._timeStamp_Column
        print self._open_Column
        print self._high_Column
        print self._low_Column
        print self._close_Column
        print self._adjustedClose_Column
        print self._volume_Column
        print self._dividendAmount_Column
        print self._splitCoefficient_Column

    def setColumns(self, line):
        columns = line.split(',')
        i = 0
        print columns
        for var in columns:
            if var == "timestamp":
                self._timeStamp_Column = i
            elif var == "open":
                self._open_Column = i
            elif var == "high":
                self._high_Column = i
            elif var == "low":
                self._low_Column = i
            elif var == "close":
                self._close_Column
            elif var == "adjusted_close":
                self._adjustedClose_Column
            elif var == "volume":
                self._volume_Column = i
            elif var == "dividend_amount":
                self._dividendAmount_Column = i
            elif var == "split_coefficient":
                self._splitCoefficient_Column = i

            i += 1

    def parseFileToLines(self):
        firstLine = self._file.readline()
        self.setColumns(firstLine)

if __name__ == "__main__":
    inputFile = sys.argv[1]
    myRead = CsvRead(inputFile)
    myRead.parseFileToLines()
    print myRead