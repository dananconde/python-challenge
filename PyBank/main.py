# Dependencies

import os
import csv

budgetdata_csv = os.path.join('..', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

# Read in CSV file
with open(budgetdata_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Code
    
    count = 0
    total = 0
    profit_loss = 0.0
    profit_loss_list = []
    price_changes = []

    for row in csvreader:
        count += 1
        total += int(row[1])
        profit_loss_list.append(int(row[1]))
    
    for x in range(len(profit_loss_list)-1):
        profit_loss = (profit_loss_list[x+1] - profit_loss_list[x])
        price_changes.append(profit_loss)
    
    average_change = round(sum(price_changes)/len(price_changes),2)

    g_increase = max(price_changes)
    g_decrease = min(price_changes)

    # f-string and Print Statements

    p = ("Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {count}\n"
        f"Total: ${total}\n"
        f"Average Change: ${average_change}\n"
        f"Greatest Increase in Profits: ${g_increase}\n"
        f"Greatest Decrease in Profits: ${g_decrease}")

    print(p)

    with open("budget_data.txt", "w+") as f:
        f.write(p)