#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: to demo shelves - save multiple py objects into 1 file 

import shelve
import pprint

movies = { 'p1': ['a','b','c'],
           'p2': ['d','e','f'],
           'p3': ['g','h','i'],
           'is': ['j','k','l'],
           'gr': ['m','n','o']}

tvseries = {
           'p1': ['p','q','r'],
           'p2': ['s','t','u'],
           'p3': ['v','w','x'],
           'is': ['y','z','zz'],
           'gr': ['za','zb','zc']}


books = {  'p1': 'lion, witch and wardrobe',
           'p2': 'dummys guide to python',
           'p3': 'guide to train sets'
           }



with shelve.open(r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/rohit_demos/media") as db:
    db['movies']=movies
    db['tvseries']=tvseries
    db['books']=books
    
    print(f"Rohit's movies {db['movies']['p1']}")
    print(f"Rohit's books {db['books']['p1']}")
