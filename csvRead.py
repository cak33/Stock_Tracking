import sys

class CsvRead:
    def __init__(self, fileName):
        self.fileName = fileName
        self.file = None
        self.linesFromFile = []
        self.entries = []
        self.firstLine = ""

        self.timeStamp_Column = -1
        self.open_Column = -1
        self.high_Column = -1
        self.low_Column = -1
        self.close_Column = -1
        self.adjustedClose_Column = -1
        self.volume_Column = -1
        self.dividendAmount_Column = -1
        self.splitCoefficient_Column = -1

        self.smaPrice_Column = -1
        self.aboveRail_Column = -1
        self.belowRail_Column = -1

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

        self.smaPrice_Column = i
        self.aboveRail_Column = i + 1
        self.belowRail_Column = i + 2

    def parseFileToLines(self):
        self.setColumns(self.firstLine)
        i = 0
        for line in self.file:
            currLine = line.split(',')                       # create an instance of Line
            newLine = []
            for item in currLine:
                newLine.append(item.rstrip())
            if i == 0:
                newLine.append("SMA_Price")
                newLine.append("upper_bound")
                newLine.append("lower_bound")
                self.firstLine = newLine
            else:
                # Add 3 blank items for the additional columns we are adding
                newLine.append(0)
                newLine.append(0)
                newLine.append(0)
                self.entries.append(newLine)               # Append the current line for processing
            i += 1

    def closeFile(self):
        self.file.close()

    def getRails(self, entry, price, railPercentage):
        entry[self.aboveRail_Column] = (price * (1 + railPercentage))
        entry[self.belowRail_Column] = (price * (1 - railPercentage))

    def calculateRails(self, simpleMovingAvg, railCalcPercentage):
        SMA_price = 0.0
        sum = 0.0
        i = 0
        correctDirectionIndex = len(self.entries) - 1
        valToSubtract = 0
        for entry in self.entries[::-1]:                       # [::-1] parses the list in reverse order
            # first need to get to where we can start the moving avg
            if (i < simpleMovingAvg):
                sum += float(entry[self.adjustedClose_Column])
                # now start the moving average calculation since we have enough
                if i == simpleMovingAvg-1:
                    SMA_price = sum / simpleMovingAvg               # calculate the simple moving avg price
                    entry[self.smaPrice_Column] = SMA_price         # add the price to the entry
                    self.getRails(entry, SMA_price, railCalcPercentage)
            # handle the rest of the cases were we need to have the sliding window
            else:
                valToSubtract = float(self.entries[correctDirectionIndex+simpleMovingAvg][self.adjustedClose_Column])
                sum -= valToSubtract                                            # subtract off the oldest in our window
                sum += float(entry[self.adjustedClose_Column])                  # add our current price in
                SMA_price = sum / simpleMovingAvg                               # calculate the SMA price
                entry[self.smaPrice_Column] = SMA_price                         # add the price to the current entry
                self.getRails(entry, SMA_price, railCalcPercentage)             # calculate the rails and add to entry
            i += 1
            correctDirectionIndex -= 1

    #def getBreakthroughs(self, safety):


    def entryToString(self, entry):
        writeString = ""
        i = 0
        for currItem in entry:
            if i == len(entry)-1:
                writeString += str(currItem) + '\n'
            else:
                writeString += str(currItem) + ","
            i += 1
        return writeString

    def writeEntriesToCSV(self, fileName):
        f = open(fileName, "w")
        f.write(self.entryToString(self.firstLine))
        for entry in self.entries:
            f.write(self.entryToString(entry))
        f.close()

if __name__ == "__main__":
    inputFile = sys.argv[1]

    # Open the file and get the lies parsed for processing
    myRead = CsvRead(inputFile)
    myRead.parseFileToLines()

    # TODO: Add functionality for setting up parameters
    simpleMovingAvg = 10        # TODO:remove this, should be received via the command line
    railCalcPercentage = .1     # TODO:remove this, should be received via the command line
    marginOfSafety = .05

    myRead.calculateRails(simpleMovingAvg, railCalcPercentage)

    # TODO: Get the breakthroughs
    #myRead.getBreakthroughs(marginOfSafety)

    # TODO: Write the breakthroughs back to the csv
    myRead.writeEntriesToCSV("output.csv")

    #print("Number of lines: " + str(len(myRead.linesFromFile)))
    #print(myRead.linesFromFile[0])

    myRead.closeFile()
