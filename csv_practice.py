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

