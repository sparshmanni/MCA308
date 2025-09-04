import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/AWSales.csv")

result = df.groupby("Marital Status")["Bike Buyer"].mean() * 100

print("Proportion of Bike Buyers by Marital Status (%):")
print(result)

result.plot(kind="bar", color="skyblue", edgecolor="black")
plt.ylabel("Percentage of Bike Buyers")
plt.title("Proportion of Bike Buyers by Marital Status")
plt.show()
