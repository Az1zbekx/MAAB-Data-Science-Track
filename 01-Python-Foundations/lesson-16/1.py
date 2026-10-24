import pandas as pd
import sqlite3

# === Part 1: Reading Files ===

# 1. chinook.db - customers jadvalini o'qish
conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("\n--- Customers (first 10 rows) ---")
print(customers_df.head(10))

# 2. iris.json
iris_df = pd.read_json('iris.json')
print("\n--- Iris Dataset Info ---")
print("Shape:", iris_df.shape)
print("Columns:", iris_df.columns.tolist())

# 3. titanic.xlsx
titanic_df = pd.read_excel('titanic.xlsx')
print("\n--- Titanic (first 5 rows) ---")
print(titanic_df.head())

# 4. flights.parquet
flights_df = pd.read_parquet('flights.parquet')
print("\n--- Flights Info ---")
flights_df.info()

# 5. movie.csv
movie_df = pd.read_csv('movie.csv')
print("\n--- Random 10 Movies ---")
print(movie_df.sample(10))


# === Part 2: Exploring DataFrames ===

# 1. Iris Data: lowercase column names & selecting two columns
iris_df.columns = iris_df.columns.str.lower()
print("\n--- Sepal Length and Width ---")
print(iris_df[['sepal_length', 'sepal_width']])

# 2. Titanic Data: age > 30 and gender count
print("\n--- Titanic: Age > 30 ---")
print(titanic_df[titanic_df['Age'] > 30])

print("\n--- Gender Counts ---")
print(titanic_df['Sex'].value_counts())

# 3. Flights: origin, dest, carrier & unique destinations
print("\n--- Flights: Origin, Dest, Carrier ---")
print(flights_df[['origin', 'dest', 'carrier']])

print("\n--- Unique Destinations ---")
print(flights_df['dest'].nunique())

# 4. Movie: duration > 120 and sorted by director likes
long_movies = movie_df[movie_df['duration'] > 120]
sorted_long_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print("\n--- Long Movies Sorted by Director Likes ---")
print(sorted_long_movies)


# === Part 3: Challenges and Explorations ===

# 1. Iris statistics
print("\n--- Iris Statistics ---")
print(iris_df.describe().loc[['mean', '50%', 'std']])  # 50% = median

# 2. Titanic age stats
print("\n--- Titanic Age Stats ---")
print("Min:", titanic_df['Age'].min())
print("Max:", titanic_df['Age'].max())
print("Sum:", titanic_df['Age'].sum())

# 3. Movie insights
print("\n--- Director with Highest Total Facebook Likes ---")
director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum()
top_director = director_likes.idxmax()
print(f"{top_director} with {director_likes.max()} likes")

print("\n--- Top 5 Longest Movies ---")
print(movie_df.nlargest(5, 'duration')[['movie_title', 'director_name', 'duration']])

# 4. Flights missing values
print("\n--- Flights Missing Values ---")
print(flights_df.isnull().sum())

# Fill numerical column (example: 'arr_delay') with mean
if 'arr_delay' in flights_df.columns:
    mean_value = flights_df['arr_delay'].mean()
    flights_df['arr_delay'] = flights_df['arr_delay'].fillna(mean_value)
    print(f"\n--- 'arr_delay' column filled with mean ({mean_value:.2f}) ---")
