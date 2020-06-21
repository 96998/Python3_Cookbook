from collections import namedtuple
import csv

with open('./data/stocks.csv') as f:
    f_csv = csv.reader(f)
    # print(f_csv)
    headers = next(f_csv)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        print(Row(*r))
    # print(*r)
    # print(r)
