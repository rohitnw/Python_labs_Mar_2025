#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: how to copy source collection to dest opt filtering

"""
Docstring:
"""

students = ['jack','john','meredith','reacher','jennifer','john']
wee_names=[]

"""

#copy source collection to destination and filter out long names

#1. using in iterator loop + source collection and optional condition (filtering), expression



#for name in students:
if len(name) <= 5:
    wee_names.append(name)



#2. using user function


def filter_names(name):
    
    if len(name) <= 5:
        return True
    else:
        return False

for name in students:
    if filter_names(name):
         wee_names.append(name)




#.3 using built in filter + source, user function - filtering

wee_names = list(filter(filter_names, students))

print(f"3.Short names  = {wee_names}")

"""""

#4. lambda functions

wee_names = list(filter(lambda name:len(name) <=5, students))
print(f"4. Short names = {wee_names}")


#5. using list comprehension

wee_names = [name for name in students if len(name) <=5]
print(f"5. Short names = {wee_names}")


#5.1
wee_names = [(name.upper(), len(name)) for name in students if len(name) <=5]
print(f"5.1 Short names = {wee_names}")

#5.2 dict comprehension - keys must be unique, so duplicates deleted
wee_names = {name.upper(): len(name) for name in students if len(name) <=5}
print(f"5.1 Short names = {wee_names}")

#5.3 set comprehension - deletes duplicates
wee_names = {name.upper() for name in students if len(name) <=5}
print(f"5.1 Short names = {wee_names}")
