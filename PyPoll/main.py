# Dependencies

import os
import csv

electiondata_csv = os.path.join('..', 'Resources', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

# Read in CSV file

with open(electiondata_csv, 'r') as csvfile:
    
    # Split the data on commas

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Code

    candidate_votes = []
    candidate_dict = {}

    for row in csvreader:
        candidate_votes.append(row[2])

    total = len(candidate_votes)

    for vote in candidate_votes: 
        if vote in candidate_dict:
            candidate_dict[vote] += 1
        else:
            candidate_dict[vote] = 1

    winning_candidate = max(candidate_dict, key=candidate_dict.get)

    # f- string and Print Statements

    stats = ""

    for candidate in candidate_dict:
        line = (f"{candidate}: {candidate_dict[candidate]} votes ({round((candidate_dict[candidate]/total)*100,2)}%)\n")
        stats += line
        
    intro = ("Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total}\n"
        "-------------------------\n")

    winner = ("-------------------------\n"
        f"Winner: {winning_candidate}\n"
        "-------------------------")

    p = intro + stats + winner

    print(p)

    with open("election_data.txt", "w+") as f:
        f.write(p)