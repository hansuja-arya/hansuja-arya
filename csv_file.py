import pandas as pd
df=pd.read_csv(r'C:\Users\Student\Desktop\pyt.csv')
print(df.isnull())
print(df.dropna())
print(df.fillna(0))
df.drop("StartDate",axis=1,inplace=True)
print(df)
for index, row in df.iterrows():
    print(row["FirstName"], row["LastName"])
print(df["salary"].sum())
print(df["salary"].mean())
print(df["salary"].max())
print(df["salary"].min())
print(df["salary"].count())