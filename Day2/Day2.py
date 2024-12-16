import numpy as np
import pandas as pd

df = pd.read_csv('C:/Ohjelmointi/AoC2024/Day2/d2input.txt', sep=" ", header=None)

safeReports = 0
row = df.loc[0]


def part1(row):
    inRange = True
    ascending = True
    desc = True
    global safeReports
    #remove NaN from row
    row = row.dropna()

    #check ascending/descending
    for j in range(row.size):
        if j != row.size-1 and ascending == True:
            ascending = row.iloc[j] < row.iloc[j+1]

    for l in range(row.size):
        if l != row.size-1 and desc == True:
            desc = row.iloc[l] > row.iloc[l+1]

    #check for numbers to be in range 1-3
    for i in range(row.size):
        if i != row.size-1 and inRange == True:
            inRange = np.abs(row.iloc[i] - row.iloc[i+1]) in range(1,4)

    #check safety
    if inRange == True and ascending == True:
        safeReports += 1
    if inRange == True and desc == True:
        safeReports += 1
    return 1



for x in range(df.shape[0]):
    part1(df.loc[x])
print("safe reports: ", safeReports)