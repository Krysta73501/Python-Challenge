import os
import csv

BANK_CSV_PATH = os.path.join("Resources", "budget_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(BANK_CSV_PATH) as bank_csv_file:
    reader = csv.reader(bank_csv_file)
    for row in reader: 
        print(row)
