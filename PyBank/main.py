import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')
months = -1
total = 0
#Creates a new list to determine the total profit
total_pl = []

print("Financial Analysis")
print("-------------------------")
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
    last = len(total_pl)-1
    avg_change = (int(total_pl[last]) - int(total_pl[0]))/months
print("Total Months:", months)   
print(f"Total: ${total}")
#print(total_pl)
#print"%8.2f" %(avg_change))
#print("Hi.")

print(f"Average Change: ${avg_change:.2f}")
#print("Greatest Increase in Profits: ")
#print("Greatest Decrease in Profits: ")