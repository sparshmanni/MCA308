import pandas as pd

df = pd.read_csv("data.csv")
print("Full DataFrame:")
print(df)

selected_rows = df.iloc[[0, 4, 7, 8]]
print("\nSelected Rows:")
print(selected_rows)
