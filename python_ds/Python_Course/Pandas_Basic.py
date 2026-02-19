import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Bengaluru", "Delhi", "Mumbai"]
}
df=pd.DataFrame(data)
print(df)

print(df[['Name','City',"Age"]])
print(df[df['Age']>30])
df['Salary']=[20000,15000,35000]
print(df)
print(df[(df['Age']<=30) & (df['Salary']>=15000)])