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
