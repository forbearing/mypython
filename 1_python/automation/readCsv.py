#!/usr/bin/env python3

import csv

def readCsv(path):
    infoList = []
    with open(path, 'r') as f:
        csvInfo = csv.reader(f)
        for row in csvInfo:
            infoList.append(row)
    return infoList

infoList = readCsv("iris.csv")
for row in infoList:
    print(row)
