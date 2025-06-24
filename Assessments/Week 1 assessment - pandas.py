import pandas as pd

#Adding a low quality column
df = pd.read_csv('assessment.csv')

df['lowquality'] = df['Rating (out of 5)'] <= 2

table = pd.DataFrame(df)

print("Data set:", table)

#Calculate and display the average price for lowquality products and for non-lowquality products,
#and are they lower or higher than the total average price of all products
sorted_quality = df.sort_values(by=['lowquality'])
grouped_quality = sorted_quality.groupby(by=['lowquality'])
grouped_quality = grouped_quality['Price']
average_price_quality = grouped_quality.mean()

print("Average price for quality vs. low quality products:", average_price_quality)

#Average price, sorted by category & material
sorted_category = df.sort_values(by=['Category', 'Material'])
group = sorted_category.groupby(['Category', 'Material'])
grouped_price = group['Price']
average_price = grouped_price.mean()
average_price = average_price.reset_index()

print("Table based on Category and Material, with average price for each:", average_price)
 
 
#Create a new dataframe for average price based on quality, compared to the total average    
total_average = df['Price'].mean()
df['Price vs Total average'] = df['Price'] > total_average

compare = average_price_quality + total_average

average_price_comparison = pd.Dataframe(compare)

print("Average price for quality vs. low quality vs. all products:", average_price_comparison)

#dont know how to move on, code above does not work unfortunately

#change1