import csv

with open("sample.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        if row[0] != "Name":
            if int(row[1]) > 1986:
                print(row)