import pandas as pd

data = {
    "name":['ram','sham','pinu'],
    "Age":[10,30,57],
    "city":['pune','mumbai','delhi']
}

df=pd.DataFrame(data)
print(df)


# to save in the excel file
df.to_csv("output.csv",index=False)

df.to_excel("outputt.xlsx", index=False) # ye index false sirf isliye hai qki hame file main jo index aa raha hai vo nahi chahiye

df.to_json("outputt_json.json", index=False)
