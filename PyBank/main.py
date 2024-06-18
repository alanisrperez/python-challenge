#PyBank budget_data | Alanis Perez Mod 3 Challenge
import os
import csv
csvpath = os.path.join("Resources","budget_data.csv")

print("Financial Analysis")
print("--------------------------------------------------------------")

# initialize variables
# months = set() # total number of months
months = 0
total_sum = 0 # net total of "Profit/Losses"
changes = [] # changes & avg of changes in "Profits/Losses"
dates = []
prev_value = None

with open(csvpath, 'r') as budget_file:
    csv_reader = csv.reader(budget_file, delimiter=",")
    months += 1
    next(csv_reader) # skip header
    for row in csv_reader: #month is in the first column (index 0)
        month = row[0]
        # months.add(month)
        months += 1
        # total_months = len(months)
        date = row[0]
        value = int(row[1])
        total_sum += value
        dates.append(date)

        if prev_value is not None:
            change = value - prev_value
            changes.append(change)
        prev_value = value

print(f"Total Months: {months}")
print(f"Total: {total_sum}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
if len(changes) == 0:
    average_change = 0
else:
    average_change = sum(changes) / len(changes)

if len(changes) > 0:
    greatest_increase_index = changes.index(max(changes))+1
    greatest_decrease_index = changes.index(min(changes))+1
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    date_of_greatest_increase = dates[greatest_increase_index]
    date_of_greatest_decrease = dates[greatest_decrease_index]
else:
    greatest_increase = 0
    greatest_decrease = 0
    date_of_greatest_increase = None
    date_of_greatest_decrease = None
    
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: ${greatest_increase} on {date_of_greatest_increase}")
print(f"Greatest Decrease in Profits: ${greatest_decrease} on {date_of_greatest_decrease}")

# Export results to a text file
output_file = os.path.join("analysis", "budget_data_output.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("--------------------------------------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${total_sum}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: ${greatest_increase} on {date_of_greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits: ${greatest_decrease} on {date_of_greatest_decrease}\n")