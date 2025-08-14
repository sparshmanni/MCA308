import pandas as pd

nominal = ['Alice', 'Bob', 'Charlie', 'David']

binary = ['Male', 'Female', 'Male', 'Female']

ordinal = ['Low', 'Medium', 'High', 'Medium'] 

continuous = [5.6, 7.2, 6.5, 8.1] 
discrete = [1, 3, 2, 4]  

df_attributes = pd.DataFrame({
    'Name': nominal,
    'Gender': binary,
    'Performance Level': ordinal,
    'Height': continuous,
    'Score': discrete
})

print("Q4 - Attribute Types:")
print(df_attributes)
