import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#creating random dataset
np.random.seed(1)
df = pd.DataFrame(np.random.randint(1,201,(100,30)))

#1.1 replacing value bw 10 and 60 with NA
df = df.mask((df >= 10) & (df <= 60))
print("NA count in each row:\n", df.isna().sum(axis=1))
print("NA count in each column:\n", df.isna().sum())

#1.2 replacing NA with mean values
df = df.fillna(df.mean(numeric_only=True))

# 1.3 heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr())
plt.show()\


# 1.4
corr = df.corr()

mask = (corr <= 0.7) & (corr != 1)

count = 0
for col in mask.columns:
    if mask[col].any():
        count += 1

print("Number of columns with correlation <= 0.7:", count)


# 1.5
df_norm = (df - df.min())/(df.max() - df.min())*10





# 1.6 replace values <=5 with 0 else 1
df_bin = df_norm.applymap(lambda x: 0 if x<=5 else 1)

# distribution plot practice
sns.histplot(df[0], kde=True)
plt.show()

