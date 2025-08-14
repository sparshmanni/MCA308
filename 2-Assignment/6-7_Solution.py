import pandas as pd

iris_df = pd.read_csv("iris.csv")

print("\nQ6 - First 5 Rows of Iris Dataset:")
print(iris_df.head())




iris_modified = iris_df.drop(index=4, axis=0)         
iris_modified = iris_modified.drop(iris_df.columns[3], axis=1) 

print("\n After Deleting Row 4 and Column 3:")
print(iris_modified.head())