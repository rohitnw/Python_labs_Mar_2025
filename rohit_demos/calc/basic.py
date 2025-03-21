#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: this module defines several basic calculator functions


"""
Basic calc functions - add, multiply, divide
"""

import sys

def add(*args):
    # *args - multiple args in tuple
    sum = 0
    for num in args:
        sum+=num

    return sum

def mul(*args):
    # *args - multiple args in tuple
    product = 1
    for num in args:
        product*=num

    return product


def div(x,z):
    #return quotient of x/z
    return round(x/z, 3)

def main():
    print("-----basic calculator------")   
    print (f"4+3+2+1 = {add(4,3,2,1)}")
    print (f"4*3*2*1 = {mul(4,3,2,1)}")
    print (f"4/3 = {div(4,3)}")
    return None

if __name__ == "__main__":
    #only exec if ran directly as a script, ignore if imported as a module
    main()
    sys.exit(0)
