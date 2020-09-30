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

With the information above, the script will create a financial report showing the results. Not only that it will create and write the results onto a .txt file.

## Pypoll

Pypoll will analyze election_data.csv.

* The script will read the csv file and show the following:
  * Total Votes
  * The Candidates that were on the ballot
  * The Amount of votes that the candidates recieve
  * The percentage of votes that the candidates votes amount to
  * The winner of the election

The total votes will look at how many votes were casted in the entire csv

For the second to fourth objective, the script will use both lists and dictionaries to store the information. The different candidates will be placed into a list and appended to a dictionary. To account for the candidate votes, a rolling count will be used to keep track on which vote goes to which candidate. To correctly assign the candidate to their vote, the same key will be used.

To calculate the percentage, the amount of votes casted for the candidate will be divided by the total votes. This will then be stored into a seperate dictionary.

Finally, the winner is found through a comparison between the amount of votes recieved by each candidate. The person with the most votes win the election.

The script will then present the results of the election and copy the results to a new .txt file.

## Text Files

As said before both of the scripts will create two .txt files. Both of the files will be found in their respective folders. For example, the pypoll script will run and the .txt file will be written in the pypoll folder. This is the same for pybank script.
