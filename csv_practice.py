
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

