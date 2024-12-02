import numpy as np
import pandas as pd

#siirretään data csv muotoon
inputdata = pd.read_csv("input.txt", sep=" ", header=None)
inputdata.to_csv("input.csv")

#alustetaan listat muistiin
list1 = np.zeros(len(inputdata))
list2 = np.zeros(len(inputdata))

# siirretään data omiin listoihin
for i in range(0,len(inputdata),1):
    list1[i] = inputdata.iloc[i,0]
    list2[i] = inputdata.iloc[i,3]


# järjetetään data suuruusjärjestykseen
sorted1 = np.sort(list1, axis=None)
sorted2 = np.sort(list2, axis=None)
result = np.zeros(len(sorted1))

# lasketaan arvojen etäisyys ja summa
for i in range(0,len(list1),1):
    result[i] = sorted1[i] - sorted2[i]
    result[i] = np.abs(result[i])

sum = np.cumulative_sum(result)
print(sum[len(sum)-1])

