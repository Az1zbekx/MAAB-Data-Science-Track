import pandas as pd

# 1. Load the CSV file
movie = pd.read_csv('movie.csv')

# 2. Create two smaller DataFrames
df1 = movie[['director_name', 'color']]
df2 = movie[['director_name', 'num_critic_for_reviews']]

# 3. Left Join
left_join = pd.merge(df1, df2, on='director_name', how='left')

# 4. Full Outer Join
outer_join = pd.merge(df1, df2, on='director_name', how='outer')

# 5. Count the number of rows
print("Left Join rows:", len(left_join))
print("Full Outer Join rows:", len(outer_join))
