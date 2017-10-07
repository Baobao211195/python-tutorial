import csv
f = open('stock.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
for row in f_csv:
	print row