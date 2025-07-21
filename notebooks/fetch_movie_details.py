import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

def search_movie(title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": API_KEY, "query": title}
    response = requests.get(url, params=params)
    return response.json()

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    return response.json()

def discover_movies(page=1, sort_by="popularity.desc"):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "sort_by": sort_by,        # Can be vote_average.desc, release_date.desc, etc.
        "page": page,
        "vote_count.gte": 100,     # Avoid low-data movies
        "language": "en-US"
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])

def get_genre_mapping():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    genres = response.json()["genres"]
    return {genre["id"]: genre["name"] for genre in genres}

if __name__ == "__main__":
    movie = input("Enter movie name: ")
    result = search_movie(movie)
    #result = search_movie("Inception")
    #print(result)

    movie_id = result['results'][0]['id']
    details = get_movie_details(movie_id)
    print(details['overview'])