#PyBank budget_data | Alanis Perez Mod 3 Challenge
import os
import csv
csvpath = os.path.join("Resources","budget_data.csv")

print("Financial Analysis")
print("--------------------------------------------------------------")

# The total number of months and net total of "Profit/Losses"
months = set()
total_sum = 0
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # skip header
    for row in csv_reader: #month is in the first column (index 0)
        month = row[0]
        months.add(month)
        total_months = len(months)
        value_to_sum = int(row[1]) #int bc values are numeric
        total_sum += value_to_sum
        # changes = []
        # prev_value = None
print(f"Total Months: {total_months}")
print(f"Total: {total_sum}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = []
dates = []
prev_value = None
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) #skip header
    for row in csv_reader:
        date = row[0]
        value = int(row[1])
        dates.append(date)

        if prev_value is not None:
            change = value - prev_value
            changes.append(change)
        prev_value = value

if len(changes) == 0:
    average_change = 0
else:
    average_change = sum(changes) / len(changes)

if len(changes) > 0:
    greatest_increase_index = changes.index(max(changes))
    greatest_decrease_index = changes.index(min(changes))
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
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_sum}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: ${greatest_increase} on {date_of_greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits: ${greatest_decrease} on {date_of_greatest_decrease}\n")