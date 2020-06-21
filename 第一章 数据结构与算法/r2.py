import csv

with open('./data/stocks.csv') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        print(i)
