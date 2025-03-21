#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: to preserve 1 python object inot file using picke module
#incomplete

import sys
import pickle

movies = { 'p1': ['a','b','c'],
           'p2': ['d','e','f'],
           'p3': ['g','h','i'],
           'is': ['j','k','l'],
           'gr': ['m','n','o']}

file = r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/rohit_demos/movies.txt"

with open(file, mode = "wb") as fh_out:
    pickle.dump(movies, fh_out)


print("-" * 60)
#open fle  for reading in test fh_in    
with open(file, mode = "rb") as fh_in:
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() -len(text)} = {text}")

#open file handle for reading in binary mode:

print("-" * 60)
#open fle  for reading in test fh_in    
with open(file, mode = "rb") as fh_in:
    fh_in.seek(-10,2) #read from eof
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() -len(text)} = {text}")


with open(file, mode = "rb") as fh_in:
    fh_in.seek(10,1)
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() -len(text)} = {text}")
