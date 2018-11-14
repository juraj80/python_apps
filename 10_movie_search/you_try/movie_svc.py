import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres')

def find_movies(search_text):

    if not search_text or not search_text.strip():
        raise ValueError   # returns ValueError in program.py in try block, to catch that exception we need to create except ValueError in search_event_loop

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)
    resp.raise_for_status()

    #print(resp.status_code)
    #print(resp.text)

    movie_data = resp.json() # turns json to dict
    movies_list = movie_data.get('hits') # get list of dictionaries with movies

# movies = []
# for md in movies_list: # to create list of namedTuples
#     m = MovieResult(imdb_code = md.get('imdb_code'),
#                     title = md.get('title'),
#                     duration = md.get('duration'),
#                     director = md.get('director'),
#                     year = md.get('year', 0),
#                     rating = md.get('rating', 0),
#                     imdb_score = md.get('imdb_score', 0.0),
#                     keywords = md.get('keywords'),
#                     genres = md.get('genres'))
#     movies.append(m)


# def method(x,y,z, **kwargs): # **kwargs takes additional keyword arguments and turns them to dictionary
#     return kwargs
#
# print(method(7,1,z=2, format=True, age=7)) # these ** can be used in reversed direction to go from dict to keyword arguments

# movies =[]
# for md in movies_list: # to create list of namedTuples
#      m = MovieResult(**md) # ** goes from the dictionary md and returns values
#      movies.append(m)

    movies = [
        MovieResult(**md)  # ** goes from the dictionary md and returns values if keys from dict are same with items from namedTuple
        for md in movies_list
    ]

    movies.sort(key=lambda m: -m.year)

    return movies

