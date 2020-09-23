import os
import csv

count = 0


csvpath = os.path.join('..','Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for rows in csvreader:
        count += 1







##print(count)