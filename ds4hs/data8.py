#! /usr/bin/env python3

from datascience import *
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import datetime
import sys


if len(sys.argv) != 2:
  print ("No csv file  supplied.")
  exit(1)

csvdata=sys.argv[1]

rawdata=Table.read_table(csvdata)

#print(rawdata.shape)
print("\n")
print("Shape of the csv imported data to the Python object name: rawdata")
print("Number of columns:", rawdata.num_columns)
print("Number of rows:", rawdata.num_rows)
x=rawdata.labels
print("\n")

for i in x:
  print(i,rawdata.column(i).dtype)
print("\n")
#print("rawdata.select('offense','precinct').pivot('precinct','offense')")
print("Start analyzing your data with the SQL-like commands 'select', 'where' and 'group'.")
print("Have fun! Build some pivot tables and draw graphs to visualize your data")
print("\n")
print(rawdata)

