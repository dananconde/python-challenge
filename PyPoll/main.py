# Dependencies

import os
import csv

electiondata_csv = os.path.join('..', 'Resources', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

# Read in CSV file

with open(electiondata_csv, 'r') as csvfile:
    
    # Split the data on commas

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Reading each row

    count = 0
    candidate_votes = []
    candidate_dict = {}

    # Dictionary Method
  
    for row in csvreader:

        count += 1
        candidate_vote.append(row[1])

    for x in candidate_vote: 

        if x not in candidate_list:

            candidate_list.append(x)


    # Print Statements
    print(count)
    print(candidate_list)