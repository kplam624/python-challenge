#Import dependancies
import os
import csv

#Set variables to initial values
months = 0
total = 0
big = 0
small = 0

#Creates lists to store values
total_pl = []
big_l = []
prof_mon = []

#Calls for the csv file
csvpath = os.path.join('..','Resources','budget_data.csv')

#Open CSV and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Counts the months in the csv
    for rows in csvreader:
        months += 1     

#Appends the profit/loss values to the new list
        total_pl.append(rows[1])

#Also appends the month to the new list
        prof_mon.append(rows[0])

#Find the total amount of profit and losses
    for change in total_pl:
        total += int(change)

#Finds the last value of the list    
    last = len(total_pl)-1

#Average change Calculation
#Difference of the last month value and first month value divided by the changes(month - 1)
    avg_change = (int(total_pl[last]) - int(total_pl[0]))/(months-1)

#Find the changes and appends them into the new list
    big_l.append(total_pl[0])
    big = 0    
    for i in range(len(total_pl)-1):
        big_l.append(int(total_pl[i+1]) - int(total_pl[i]))

#Does a comparison to find the greatest increase and greatest decrease    
    for i in range(len(total_pl)):
        num = big_l[i]
        if int(num) > big:
            big = int(num)
            inc = i
        elif int(num) < small:
            small = int(num)
            dec = i
        else:
            continue

#Creates a .txt file
mainfile = open("main.txt","w")

mainfile.write("Financial Analysis\n")
mainfile.write("-------------------------\n")
mainfile.write(f"Total Months: {months}\n")
mainfile.write(f"Total: ${total}\n")
mainfile.write(f"Average Change: ${avg_change:.2f}\n")
mainfile.write(f"Greatest Increase in Profits: {prof_mon[inc]} (${big})\n")
mainfile.write(f"Greatest Decrease in Profits:  {prof_mon[dec]} (${small})\n")
mainfile.close()

#Output, Financial Analysis
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {months}")   
print(f"Total: ${total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {prof_mon[inc]} (${big})")
print(f"Greatest Decrease in Profits:  {prof_mon[dec]} (${small})")
