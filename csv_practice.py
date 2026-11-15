# 1. Python can automate an ETL pipeline by reading, cleaning, and organizing
# large amounts of data quickly. Excel is easier for manually editing data,
# creating charts, and looking at information visually. Python is better for
# repeating tasks and processing large files automatically.
# 2. A business could use an append-mode log file to track customer orders.
# Each new order could be added to the file with its date, time, and details.
# Append mode is useful because it saves new orders without deleting old ones,
# keeping a record of all past transactions.

import csv
from datetime import datetime

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        total_revenue += revenue

print(f"Total revenue: ${total_revenue:.2f}")

# Append the date, time, and total revenue to the log file
with open("data/run_log.txt", "a", newline="") as log_file:
    timestamp = datetime.now()
    log_file.write(f"{timestamp}: Total revenue = ${total_revenue:.2f}\n")

print("Run saved to data/run_log.txt")

