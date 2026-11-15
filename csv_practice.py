
import csv

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")


