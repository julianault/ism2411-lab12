
import csv

sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity

        if product in sales_summary:
            sales_summary[product] += revenue
        else:
            sales_summary[product] = revenue

print("Sales Summary by Product:")

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

