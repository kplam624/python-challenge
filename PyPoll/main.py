#Imports dependacies
import os
import csv

#Count the total amount of votes
count = 0

#Stores candidate name data
candidate = []

#Stores how many votes each candidates recieve
votecount = [0,0,0,0]

#Creates dictionaries for easy storage and recall
cand_dic = {}
cand_vote = {}
cand_percent = {}

#Calls for the csv file
csvpath = os.path.join('..','Resources','election_data.csv')

#Reads the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Stores the csv header
    csv_header = next(csvreader)

    for rows in csvreader:

#Counts the total votes in the election
        count += 1

#Appends all candidates to a list
        if rows[2] not in candidate:
            candidate.append(rows[2])

#Counts the amount of votes for each candidate        
        for i in range(len(candidate)):
            if rows[2] == candidate[i]:
                votecount[i] += 1

#Adds each value from the lists to the corresponding dictionaries
for i in range(len(candidate)):
    cand_dic[f"Candidate Name {i}"] = candidate[i]
    cand_vote[f"Candidate Name {i}"] = votecount[i]
#Adds the percents to its own dictionary
    cand_percent[f"Candidate Name {i}"] = (cand_vote[f"Candidate Name {i}"] / count) * 100

#Method to identify the winner
winner = "Candidate Name 0"

#Compares the votes each candidate has, and sets the variable to the key of the dictionary
for i in range(len(candidate)-1):
   if cand_vote[f"Candidate Name {i+1}"] > cand_vote[f"Candidate Name {i}"]:
       winner = f"Candidate Name {i+1}"


#Output, Summary of the result
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {count}")
print("----------------------------------")
for i in range(len(candidate)):
    print(f"{cand_dic[f'Candidate Name {i}']}: {cand_percent[f'Candidate Name {i}']:.3f}% ({cand_vote[f'Candidate Name {i}']})")
print("----------------------------------")
print(f"Winner: {cand_dic[winner]}")
print("----------------------------------")

#Creates a .txt file and writes the result in the file.
mainfile = open("main.txt","w")

mainfile.write("Election Results \n")
mainfile.write("---------------------------------- \n")
mainfile.write(f"Total Votes: {count} \n")
mainfile.write("---------------------------------- \n")
for i in range(len(candidate)):
    mainfile.write(f"{cand_dic[f'Candidate Name {i}']}: {cand_percent[f'Candidate Name {i}']:.3f}% ({cand_vote[f'Candidate Name {i}']}) \n")
mainfile.write("----------------------------------\n")
mainfile.write(f"Winner: {cand_dic[winner]} \n")
mainfile.write("---------------------------------- \n")

mainfile.close()