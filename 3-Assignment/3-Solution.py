import pandas as pd

df = pd.read_csv("bike_buyers.csv")

result = df.groupby("Commute Distance")["Bike Buyer"].mean() * 100

print("Percentage of customers who purchased a bike in each commute distance category:")
print(result)
