import csv
import os

# Get the absolute path to the CSV file
file_path = os.path.abspath('Pybank/Resources/budget_data.csv')

# Read the budget data from the CSV file
with open(file_path) as file:
    reader = csv.reader(file)
    next(reader)    

    months = []
    profit = []
    changes = []

    previous_profit_loss = None

    for row in reader:
        months.append(row[0])
        profit.append(int(row[1]))

    for i in range(1, len(profit)):
        profit_change = profit[i] - profit[i - 1]
        changes.append(profit_change)

# Calculate average change
avg_change = sum(changes) / len(changes)

# Find greatest profit increase/decrease
greatest_increase_amt = max(changes)
greatest_increase_date = months[changes.index(greatest_increase_amt) + 1]
greatest_decrease_amt = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease_amt) + 1]

# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amt})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amt})")
