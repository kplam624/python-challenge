import os
import csv

count = 0

candidate = []
votecount = [0,0,0,0]
cand_dic = {}
cand_vote = {}
cand_percent = {}

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
    cand_dic[f"Candidate Name {i}"] = candidate[i]
    cand_vote[f"Candidate Name {i}"] = votecount[i]
    cand_percent[f"Candidate Name {i}"] = cand_vote[f"Candidate Name {i}"] / count
    
for i in range(len(candidate)):
    print(cand_percent[f"Candidate Name {i}"])

# print("Election Results")
# print("----------------------------------")
# print(f"Total Votes: {count}")
# print("----------------------------------")
# for i in range(len(candidate)):
#     print(f"{cand_dic[f'Candidate Name {i+1}']}: damn {cand_vote[f'Candidate Name {i+1}']}")
# print("----------------------------------")
# print("Winner: ")
# print("----------------------------------")
##print(votecount)
##print(count)