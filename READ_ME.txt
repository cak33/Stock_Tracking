SAMPLE COMMANDS:

	python csvRead.py -file csvRead.py daily_adjusted_WWW.csv - This command runs it with default values

	python csvRead.py -file daily_adjusted_WWW.csv -margin .1 -rail .50 -avg 30 - This command changes all values


Run Options:
	-file: The input file name (include the .csv)"
	-margin: The margin of safety in .XX format"
	-rail: The \"rail\" percentage in .XX format"
	-avg: The amount of days for the moving average"