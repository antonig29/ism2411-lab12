with open("data/sales.csv") as f:
    print(f.readline())


import csv

# Exercise 2: read and print raw rows
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
