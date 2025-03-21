#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: open, close, read, write text file using built-in open function

movies = { 'p1': ['a','b','c'],
           'p2': ['d','e','f'],
           'p3': ['g','h','i'],
           'is': ['j','k','l'],
           'gr': ['m','n','o']}

file = r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/rohit_demos/movies.txt"
fh_out = open(file, mode = "wt")

#iterate through movies dict and write key + values to file
for name in movies.keys():
    print(name, movies[name])
    #fh_out.write(name + str(movies[name]))
    fh_out.write(f"{name}: {movies[name]}\n")

fh_out.flush() #manually flush buffers
fh_out.close() #flushed buffers and closes file


print("-" * 60)
#open fle  for reading
fh_in = open(file, mode = "rt")
#text = fh_in.read() #reads entire file into str object. could havae issues with large files
#text = fh_in.read(30)
#text = fh_in.readline() #reads 1 line (till first newline parameter)
#text = fh_in.readlines() #reads entire rile into a list object 
#print(text)

#text = fh_in.readlines() #reads entire rile into a list object 
#print(text[2])


#interate through file 1 line at a time - for loop + filehandle (iteragor object iter()/ next())

for line in fh_in:
    print(line, end="")


fh_in.close()
