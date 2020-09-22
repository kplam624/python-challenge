import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')
months = -1
total = 0
big = 0
small = 0
#Creates a new list to determine the total profit
total_pl = []

#Creates a new list for both months and profits
big_l = []

#Header of the Financial Analysis
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
#Also appends the month to the new list
        prof_mon.append(rows)
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

##Attempt to find the greatest changes
    big_l.append(total_pl[0])    
    for i in range(len(total_pl)-1):
        big_l = [total_pl[i+1] - total_pl[i]]


#prints the rest of the stuff
print("Total Months:", months)   
print(f"Total: ${total}")
print(f"Average Change: ${avg_change:.2f}")
#print("Greatest Increase in Profits: ")
#print("Greatest Decrease in Profits: ")

print(big)
##print("Hi.")