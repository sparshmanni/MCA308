import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bike_buyers.csv")

buyers = df[df["Bike Buyer"] == 1]["Age"]
non_buyers = df[df["Bike Buyer"] == 0]["Age"]

print("Average Age of Buyers:", buyers.mean())
print("Average Age of Non-Buyers:", non_buyers.mean())

plt.hist(buyers, bins=10, alpha=0.7, label="Bike Buyers")
plt.hist(non_buyers, bins=10, alpha=0.7, label="Non-Buyers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution: Buyers vs Non-Buyers")
plt.legend()
plt.show()
