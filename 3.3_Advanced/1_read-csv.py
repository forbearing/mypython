#!/usr/bin/env python3
import csv

res = open('test.csv')
reader = csv.reader(res, delimiter=',')
print(reader.__next__)
