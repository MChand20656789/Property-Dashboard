import pandas as pd
df = pd.read_csv("data/realtor-data.csv")
print("Rows:", len(df))
print(df.head())
print(df.info())
print(df.describe(include='all').transpose())
print("Missing values (%):\n", (df.isnull().sum()/len(df)*100))