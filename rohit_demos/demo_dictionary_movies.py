#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: create, grow, shring dictionaries
import pprint

movies = { 'p1': ['a','b','c'],
           'p2': ['d','e','f'],
           'p3': ['g','h','i']}

movies['is']=['j','k','l']
movies['gr']=['m','n','o']

#print(movies)

pprint.pprint(movies)

movies.pop('p2')
pprint.pprint(movies)

movies.popitem()

pprint.pprint(movies)


print(f"Is's favourite movies are 1 {movies['is']}")


print(f"Is's favourite movies are 2 {movies['is'][0]}")


print(f"Is's favourite movies are 3 {movies.get('is')}")


for films in movies.values():
    print(f"Good  films = {films}")


for (name, films) in movies.items():
    print(f"{name} Loves the films {films}")