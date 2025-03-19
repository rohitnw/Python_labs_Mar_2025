#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: how to iterate through collections (str, tuple, list, dict, sets)
#  using an interator for loop


heroes = ['Spider man','Wonder woman','Batman','Batgirl','Indiana Jones']

for name in heroes:
    print (name, end="\n")

print("unchanges heroes=", heroes)


# using iterator for loop and modify objectx

idx = 0
for name in heroes:
    print (name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx+=1

print("changed heroes=", heroes)


# using built-in enumerate() function


for (idx,name) in enumerate(heroes, start = 0):
    print (name.title(), end="\n")
    heroes[idx] = name.title()
    

print("changed heroes=", heroes)
