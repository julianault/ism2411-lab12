
import csv

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")

# csv.reader is useful for simple files when you want to access columns by index.
# csv.DictReader is easier to read when you want to access columns by their names.
