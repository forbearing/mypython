#!/usr/bin/env python3

import csv

def writeCsv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

infoList = [[1,2,3],[4,5,6],[7,8,9]]
writeCsv("test.csv", infoList)
