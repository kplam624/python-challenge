import os
import csv

count = 0
votecount1 = 0

candidate = []
cand_dic = {}
csvpath = os.path.join('..','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for rows in csvreader:
        count += 1
        if rows[2] not in candidate:
            candidate.append(rows[2])
        # else:
        #     continue

        if rows[2] == candidate[0]:
            votecount1 +=1


for i in range(len(candidate)):
    cand_dic[f"Candidate Name {i+1}"] = candidate[i]


print(count)
print(cand_dic)
print(votecount1)