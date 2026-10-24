import requests
import random

Api_key = "69fd13f6d0ece99d21db4d6f2984a570"

url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Api_key}&language=en-US"

response = requests.get(url).json()
genres = {g["name"].lower(): g["id"] for g in response["genres"]}

user = input("Movie genre: ").lower()

if user not in genres:
    print("No such genre found!")
else:
    Id = genres[user]
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={Api_key}&with_genres={Id}"
    data = requests.get(url).json()["results"]
    movie = random.choice(data)
    if not movie:
        print("No movies found in this genre!")
    print(f"Recommended movie: {movie['title']}")
