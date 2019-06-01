import os
import csv

budgetdata_csv = os.path.join('..', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

# Functions

# Read in CSV file
with open(budgetdata_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Number of Months and Total from budget_data
    
    count = 0
    total = 0
    g_increase = 0.0
    g_decrease = 0.0

    for row in csvreader:
        count += 1
        total += int(row[1])

    print(count)
    print(total)