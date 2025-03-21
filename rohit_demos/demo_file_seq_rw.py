#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: safer way to open files - block scope demo


movies = { 'p1': ['a','b','c'],
           'p2': ['d','e','f'],
           'p3': ['g','h','i'],
           'is': ['j','k','l'],
           'gr': ['m','n','o']}

file = r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/rohit_demos/movies.txt"

with open(file, mode = "wt") as fh_out:
    #iterate through movies dict and write key + values to file
    for name in movies.keys():
        print(name, movies[name])
        #fh_out.write(name + str(movies[name]))
        fh_out.write(f"{name}: {movies[name]}\n")

fh_out.close() #flushed buffers and closes file


print("-" * 60)
#open fle  for reading
with open(file, mode = "rt") as fh_in:
    text = fh_in.readlines() #reads entire rile into a list object 
    print(text)
fh_in.close()
