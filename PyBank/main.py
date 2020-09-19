import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')
months = -1
total = 0
#Creates a new list to determine the total profit
total_pl = []

#Open CSV and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Counts the months in the csv
    for rows in csvreader:
## To see the set        print(rows[1])
        months += 1
        
#Appends the profit/loss values to the new list
        total_pl.append(rows[1])

#Find the total amount of profit and losses
#Removes the header and adds up the changes
    total_pl.pop(0)
    for change in total_pl:
        total += int(change)


print("Hi.")
print(total_pl)
print(total)
print("Financial Analysis")
print("-------------------------")
print("Total Months:", months)
print(f"Total: ${total}")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")