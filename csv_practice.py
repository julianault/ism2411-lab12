
import csv

total_rows = 0
cleaned_rows = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)

    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                cleaned_rows += 1

print(f"Rows in original file: {total_rows}")
print(f"Rows written to cleaned.csv: {cleaned_rows}")

