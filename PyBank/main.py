import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')
months = -1
total = 0
big = 0
small = 0

#Creating a few lists
total_pl = []
big_l = []
prof_mon = []

#Open CSV and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
#Counts the months in the csv
    for rows in csvreader:
        months += 1     
#Appends the profit/loss values to the new list
        total_pl.append(rows[1])
#Also appends the month to the new list
        prof_mon.append(rows[0])
#Find the total amount of profit and losses
#Removes the header and adds up the changes
    total_pl.pop(0)
    for change in total_pl:
        total += int(change)
#Finds the last value of the list    
    last = len(total_pl)-1

#Average change Calculation
#Difference of the last month value and first month value divided by the total months
    avg_change = (int(total_pl[last]) - int(total_pl[0]))/months

#Find the changes and inserts them into a new list
    big_l.append(total_pl[0])
    big = 0    
    for i in range(len(total_pl)-1):
        big_l.append(int(total_pl[i+1]) - int(total_pl[i]))
    
    for i in range(len(total_pl)):
        num = big_l[i]
        if int(num) > big:
            big = int(num)
            inc = i+1
        elif int(num) < small:
            small = int(num)
            dec = i+1
        else:
            continue

#Header of the Financial Analysis
print("Financial Analysis")
print("-------------------------")

#prints the rest of the stuff
print("Total Months:", months)   
print(f"Total: ${total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {prof_mon[inc]} (${big})")
print(f"Greatest Decrease in Profits:  {prof_mon[dec]} (${small})")
