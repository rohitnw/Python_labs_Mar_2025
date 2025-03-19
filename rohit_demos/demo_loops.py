#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: demo a block of commands a specific number of times using a counter loop


"""
Docstring:
"""
count = 0 #init counter
while count < 10: # test counter
    print(count)
    count+=1 #increment counter


#Alternate - for loop + built-in range()

for num in range(0,10,1):
    print(num)

#Alternate - assumes start is 0
for num2 in range(10,1):
    print(num2)

#Alternate - assumes step is 1, start is 0
for num3 in range(10):
    print(num3)
