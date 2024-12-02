import numpy as np
import pandas as pd

inputdata = pd.read_csv("input.txt", sep=" ", header=None)

list1 = np.zeros(len(inputdata))
list2 = np.zeros(len(inputdata))

for i in range(0,len(inputdata),1):
    list1[i] = inputdata.iloc[i,0]
    list2[i] = inputdata.iloc[i,3]

sorted1 = np.sort(list1, axis=None)
sorted2 = np.sort(list2, axis=None)
result = np.zeros(len(inputdata))

for i in range(0,len(list1),1):
    result[i] = np.abs(sorted1[i] - sorted2[i])
sum = np.cumulative_sum(result)
print(sum[len(sum)-1])

