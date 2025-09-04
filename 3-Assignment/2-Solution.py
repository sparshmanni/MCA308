import pandas as pd
from scipy import stats


df1 = pd.read_csv("archive/AWCustomers.csv")
df2 = pd.read_csv("archive/AWSales.csv")

data = pd.merge(df1, df2, on="CustomerID")

buyers = data[data["BikeBuyer"]==1]["YearlyIncome"]
non_buyers = data[data["BikeBuyer"]==0]["YearlyIncome"]


t_stat, p_val = stats.ttest_ind(buyers, non_buyers, equal_var=False)

print("Buyers Avg Income:", buyers.mean())
print("Non-Buyers Avg Income:", non_buyers.mean())
print("t-statistic:", t_stat, "p-value:", p_val)
