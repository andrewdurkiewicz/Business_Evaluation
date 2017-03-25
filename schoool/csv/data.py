#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import csv


def readdata(f):
    data = []
    for line in csv.reader(f):
        for i, point in enumerate(line):
            try:
                data[i].append(float(point))
            except:
                data.append([])
    return np.array(data)


with open('0-output.csv', 'r') as f:
    data0 = readdata(f)
with open('1-output.csv', 'r') as f:
    data1 = readdata(f)
with open('2-output.csv', 'r') as f:
    data2 = readdata(f)
with open('3-output.csv', 'r') as f:
    data3 = readdata(f)
with open('4-output.csv', 'r') as f:
    data4 = readdata(f)
with open('5-output.csv', 'r') as f:
    data5 = readdata(f)
    
# Time,Temp,Pressure,KE,U