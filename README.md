# python-challenge
The goal is to analyze two different csv files using python. Create a summary from the analysis and write the summary onto a .txt file.

# Resources

Within the resources file, contains the csvs that need to be analyzed.

# Submission

Within the file pybank and pypoll will hold the scripts to complete the above goal. Pybank will analyze budget_data.csv and pypoll will analyze election_data.csv.

## Pybank

Pybank will analyze budget_data.csv. 

* The script will read the csv file and will show the following:
  * Total Months
  * Total
  * The Average Change
  * Greatest Increase
  * Greatest Decrease

The total months will analyze the total months that is contained in the csv.

The total will find the sum of the profit and loss for the entire period.

The average change will look to find the change over the whole period. This will first find the difference of the first entry and the last entry. With the difference, the script will then divide it by the amount of changes over the whole period.

The greatest increase will compare each value in the profit/loss category and take the largest value from it.

The greatest decrease in analogous to the greatest increase. However, will store the smallest value from it.

With all of the information the script will create a financial report showing the results. Not only that it will create and write the results onto a .txt file.

## Pypoll

Pypoll will analyze election_data.csv.


