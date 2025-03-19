#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: ch3 - ex 2 - to display range of numbers - step 2


var = 0
num = 0

var = input ("Please enter an integer:")
if var.isdecimal():
    var = int(var)
    print("entered number is:", var)
    for num in range(var,0,-2):
        print(num)
else:
    print("not a number")
    