import sys


class CsvRead:
    def __init__(self):
        self.line = False

    def __str__(self):
        return "Using the string method"


if __name__ == "__main__":
    argument1 = sys.argv[1]
    print(argument1)

    line = CSV_Read()
    print(line)
