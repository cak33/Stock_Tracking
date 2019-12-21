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
        self.breakthrough_Column = -1

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
        i = 0
        for var in line:
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
            elif var == "SMA_Price":
                self.smaPrice_Column = i
            elif var == "upper_bound":
                self.aboveRail_Column = i
            elif var == "lower_bound":
                self.belowRail_Column = i
            elif var == "breakthrough":
                self.breakthrough_Column = i
            i += 1

    def parseFileToLines(self):
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
                newLine.append("breakthrough")
                self.firstLine = newLine
                self.setColumns(self.firstLine)
            else:
                # Add 4 blank items for the additional columns we are adding
                newLine.append(0)
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

    def getBreakthroughs(self, simpleMovingAvg, safety):
        i = 0
        for entry in self.entries:
            if i < len(self.entries) - simpleMovingAvg:
                # calculate upper and lower safety
                upperPlusSafety = float(entry[self.adjustedClose_Column]) * (1 + safety)
                lowerPlusSafety = float(entry[self.adjustedClose_Column]) * (1 - safety)
                if entry[self.smaPrice_Column] > upperPlusSafety:
                    entry[self.breakthrough_Column] = "UPPER"
                elif entry[self.smaPrice_Column] < lowerPlusSafety:
                    entry[self.breakthrough_Column] = "LOWER"
            i += 1

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
        print fileName
        f = open(fileName, "w")
        f.write(self.entryToString(self.firstLine))
        for entry in self.entries:
            f.write(self.entryToString(entry))
        f.close()


if __name__ == "__main__":
    simpleMovingAvg = 10
    railCalcPercentage = .10
    marginOfSafety = .05
    inputFile = ""
    outputFileName = "output"

    i = 0
    # parse the args
    for arg in sys.argv:
        if arg == "-help" or len(sys.argv) == 1:
            print "-file: The input file name (include the .csv)"
            print "-margin: The margin of safety in .XX format"
            print "-rail: The \"rail\" percentage in .XX format"
            print "-avg: The amount of days for the moving average"
            print "-o: The output file name (do no include the extension"
            print "Default Values:"
            print "Moving Average = " + str(simpleMovingAvg)
            print "Rail percentage = " + str(railCalcPercentage)
            print "Margin of Safety = " + str(marginOfSafety)
            print "Output File = " + outputFileName + ".csv"
        elif arg == "-file":
            inputFile = sys.argv[i+1]
        elif arg == "-margin":
            marginOfSafety = float(sys.argv[i+1])
        elif arg == "-rail":
            railCalcPercentage = float(sys.argv[i+1])
        elif arg == "-avg":
            simpleMovingAvg = int(sys.argv[i+1])
        elif arg == "-o":
            outputFileName = str(sys.argv[i+1])
        i += 1

    if inputFile != "":
        # Open the file and get the lies parsed for processing
        myRead = CsvRead(inputFile)
        myRead.parseFileToLines()
        myRead.calculateRails(simpleMovingAvg, railCalcPercentage)
        myRead.getBreakthroughs(simpleMovingAvg, marginOfSafety)
        myRead.writeEntriesToCSV(outputFileName + ".csv")

        myRead.closeFile()
