import csv

with open('./data/stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)
print(f"row[0] is {row[0]}")
print(f"row[4] is {row[4]}")
