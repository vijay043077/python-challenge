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
    profit_increase = {"Date": first_row[0], "Profit_Increase": 0}
    profit_decrease = {"Date": first_row[0], "Profit_Decrease": 0}

    # read each row after header row
    # count total number of months 
    # net total amount of "Profit/Losses"
    for row in csv_reader:
        total_months_count = total_months_count + 1
        net_total = net_total + int(row[1])
        change_in_profit = int(row[1]) -previous_row
        previous_row = int(row[1])

        # change in profit "if" statement
        if len(net_change)> 0 and change_in_profit> max(net_change):
            profit_increase["Date"] = row[0]
            profit_increase["Profit_Increase"] = change_in_profit
            print(profit_increase)
            
        elif len(net_change) and change_in_profit< min(net_change):
            profit_decrease["Date"] = row[0]
            profit_decrease["Profit_Decrease"] = change_in_profit
        
        net_change.append(change_in_profit)

    # average of net change formula
    average_net_change = sum(net_change)/len(net_change) 

    # print out financial summary
    print(f"Total Months: {total_months_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_net_change: .2f}")
    print("Greatest Increase in Profits:", profit_increase["Date"], "$", profit_increase["Profit_Increase"])
    print("Greatest Decrease in Profits:", profit_decrease["Date"], "$", profit_decrease["Profit_Decrease"])

    # set a variable to print to txt file
    text_file= os.path.join("budget_results.txt")
    output_text = ""
     # print budget results to txt file\n"
    output_text +=f"Total Months: {total_months_count}\n"
    output_text +=f"Total: ${net_total}\n"
    output_text +=f"Average Change: ${average_net_change: .2f}\n"
    output_text +=str({'Greatest Increase in Profits:', profit_increase['Date'], '$', profit_increase['Profit_Increase']})
    output_text +=str({'Greatest Decrease in Profits:', profit_decrease['Date'], '$', profit_decrease['Profit_Decrease']})
    with open("output.txt","w") as out_text:
        out_text.write(output_text)
    



