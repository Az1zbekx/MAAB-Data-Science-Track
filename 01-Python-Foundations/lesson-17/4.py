import pandas as pd

# 1. Load movie data
movie = pd.read_csv('movie.csv')

# 2. Group by color and director_name
grouped_movies = movie.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews': 'sum',
    'duration': 'mean'
}).reset_index()

print(grouped_movies.head())
