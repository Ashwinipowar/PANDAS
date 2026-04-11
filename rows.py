# rows ko kese dekh sakte hai aap pandas ke madat se
# ye check kar sakte ho data correctly load kiya gaya hai ya nahi gaya
# data organize kese hai

# for this we have two methods 
 # head() , tail() only shows 5 rows


import pandas as pd
df= pd.read_json("sample_Data.json")


print("display pehle")
print(df.head(10))


print("display last ke ")
print(df.tail(10))
