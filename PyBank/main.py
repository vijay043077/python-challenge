# import os module & csv reader
import os
import csv 
# import the system module
import sys

# set file path
csv_path = os.path.join("..", "PyBank", "budget_data.csv")

# read CSV file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # read header row 
    header_row = next(csv_reader, None)

    # set variables for first row
    total_months_count = 1
    first_row = next(csv_reader)
    net_total = 0
    net_total = net_total + int(first_row[1])
    previous_row = int(first_row[1])
    change_in_profit = 0
    net_change = []
    max_increase = {"date": first_row[0]},"value": 0}

    # read each row after header row
for row in csv_reader:
    total_months_count = total_months_count + 1
    net_total = net_total + int(row[1])
    change_in_profit = int(row[1]) -1








