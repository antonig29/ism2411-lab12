with open("data/sales.csv") as f:
    print(f.readline())


import csv

# Exercise 2: read and print raw rows
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# Exercise 3: skip the header
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)


# Exercise 4: compute totals
total_revenue = 0
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        total_revenue = total_revenue + total
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5: filter and write
original_count = 0
written_count = 0
with open("data/sales.csv") as infile:
    with open("data/cleaned.csv", "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        next(reader)
        writer.writerow(["Product", "Price", "Qty", "Total"])
        for row in reader:
            original_count = original_count + 1
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity
            if total > 100:
                writer.writerow([row[0], price, quantity, total])
                written_count = written_count + 1
print(f"Rows written: {written_count}, rows in original: {original_count}")

# exercise 6:csv.DictReader
dict_total = 0
with open("data/sales.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total = dict_total + total
        print(f"{row['product']}: {quantity} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")

#csv.reader uses column positions which is short but it can get mixed up
#the dict reader uses column names which is more reliable and less likely to make a mistake


# Exercise 7: Sales summary by product
import csv
from datetime import datetime

summary = {}
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        total = float(row[1]) * int(row[2])
        if product in summary:
            summary[product] = summary[product] + total
        else:
            summary[product] = total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


#exercise 8: Append mode log
log_total = 0
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        log_total = log_total + float(row[1]) * int(row[2])

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{datetime.now()} - Total revenue: ${log_total:.2f}\n")
