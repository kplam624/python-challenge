import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')
months = -1
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for rows in csvreader:
        print(rows)
        months += 1
print("Hi.")
print("Financial Analysis")
print("-------------------------")
print("Total Months: ",months)
print("Total: ")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")