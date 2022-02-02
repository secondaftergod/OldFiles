import csv
whith open("crimes.csv") as f:
	reader=csv.reader(f)
	for row in reader:
		print(row)
