import pandas as pd

 # this is how we read the csv file 
df= pd.read_csv("sales_data_sample.csv" ,encoding="latin1")
print(df)


# this is how we read the xlxs file and the json file
df=pd.read_excel("sales_data_sample.xlsx", engine="openpyxl")
print(df)
    


df=pd.read_json("sample_Data.json")
print(df)




