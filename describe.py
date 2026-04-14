import pandas as pd

data={
    "Nmae": ['ram','shyam','siya','diya','priya','minu'],
    "age":[22,33,44,32,43,21,],
    "salary":[2000,300000,6000,70000,87777,89999],
    "performance":[35,57,85,58,93,73]


}

df=pd.DataFrame(data)
print("sample Dataframe")
print(df)
print("desscriptive statistics")
print(df.describe())



# desscriptive statistics
#              age         salary  performance
# count   6.000000       6.000000     6.000000
# mean   32.500000   92629.333333    66.833333
# std     9.853933  108870.070605    21.169947
# min    21.000000    2000.000000    35.000000
# 25%    24.500000   22000.000000    57.250000
# 50%    32.500000   78888.500000    65.500000
# 75%    40.500000   89443.500000    82.000000
# max    44.000000  300000.000000    93.000000

#this kind of hame o/p milega

#mean hame ik avg value deta hai pure values ka
# std hota hai small and large matlb jo avg kr close hai matlab value avg se kafi dur haiu
# matlb ke std deiation large hai
# std main jitni variation utna values std is klarge


