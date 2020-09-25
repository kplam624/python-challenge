import os
import csv

count = 0
votecount1 = 0

candidate = []
votecount = [0,0,0,0]
cand_dic = {}
cand_vote = {}

csvpath = os.path.join('..','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for rows in csvreader:
        count += 1
        if rows[2] not in candidate:
            candidate.append(rows[2])
        
        for i in range(len(candidate)):
            if rows[2] == candidate[i]:
                votecount[i] += 1

for i in range(len(candidate)):
    cand_dic[f"Candidate Name {i+1}"] = candidate[i]
    cand_vote[f"Candidate Name {i+1}"] = votecount[i]
    

for i in range(len(candidate)):
    print(cand_dic[f"Candidate Name {i+1}"])
    print(cand_vote[f"Candidate Name {i+1}"])

## for i in range(len(votecount)):
print(votecount)
#print(count)