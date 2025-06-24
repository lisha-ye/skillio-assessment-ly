import numpy as np
import datetime
from faker import Faker
import pandas as pd

product_ID = np.random.randint(1000, 9999, size=5)
product_price = np.random.randint(50, 5000, size=5)

product_name = ['TV', 'Barbie', 'Laundry Basket', 'Hose', 'Skirt']
product_category = ['Electronics', 'Toys', 'Home', 'Garden', 'Clothing']

# Simulate transaction data that includes transaction ID, user ID, product ID, quantity, and transaction date.
# Ensure the transaction dates and quantities are randomly generated to simulate real purchase behaviour.

trans_id = np.random.randint(10000, 99999, size=5)
user_id = np.random.randint(3000, 3999, size=5)

#transaction date
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2025, 12, 31)

# Total days in range
days_range = (end_date - start_date).days

# Generate random day offsets and convert to dates
trans_date = np.random.randint(0, days_range, size=5)
trans_date = [start_date + datetime.timedelta(days=int(day)) for day in trans_date]
trans_date_str = [d.strftime('%Y-%m-%d') for d in trans_date]

df2 = trans_id, user_id, trans_date_str


#create dataframes
catalogue = {
    'product ID': [3261, 8677, 7118, 3571, 4237],
    'product price': [815, 3999, 4531, 4264, 4072],
    'product name': ['TV', 'Barbie', 'Laundry Basket', 'Hose', 'Skirt'],
    'product_category': ['Electronics', 'Toys', 'Home', 'Garden', 'Clothing']
}

df_catalogue = pd.DataFrame(catalogue)

catalogue2 = {
    'product ID': [3261, 8677, 7118, 3571, 4237],
    'transaction ID': [71667, 84118, 11262, 16900, 92577],
    'user ID': [3249, 3998, 3285, 3258, 3235],
    'purchase date': ['2025-05-08', '2024-03-08', '2023-12-20', '2025-07-26', '2024-11-19'],
    'quantity': [1, 2, 3, 4, 5]
}
    
df_catalogue2 = pd.DataFrame(catalogue2)

full_catalogue = pd.merge(df_catalogue, df_catalogue2)
    
    #print(full_catalogue)

#aggregation
#Calculate the total spending per user.
full_catalogue['total_spent'] = full_catalogue['product price'] * full_catalogue['quantity']
user_spending = full_catalogue.groupby('user ID')['total_spent'].sum()

    #print(user_spending)

#Find the top 3 best-selling products and their average price.

