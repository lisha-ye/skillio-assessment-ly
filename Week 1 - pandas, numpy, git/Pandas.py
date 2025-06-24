import pandas as pd

#Creating a DataFrame manually
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': ['12', '55', '89', '15', '23'],
    'score': ['50', '60', '70', '80', '90'],
})

df = df.set_index('name')
print(df)