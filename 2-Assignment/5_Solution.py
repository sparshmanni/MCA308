import pandas as pd

df = pd.read_csv("data.csv")

print(df)


print("\n Rows 3 to 7:")
print(df.iloc[3:8])


print("\n Rows 4 to 8, Columns 2 to 4:")
print(df.iloc[4:9, 2:5])


print("\n Columns index 1 to 3:")
print(df.iloc[:, 1:4])