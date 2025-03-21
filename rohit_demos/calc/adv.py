#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: this module defines several adv calculator functions


"""
Adv calc functions - modulus, power, square root
"""

import sys

def mod(x,z):
    # *args - multiple args in tuple
    #returns modulus of x/z
    return (x%z)

def power(x,z):
    # *args - multiple args in tuple
    #returns x to power z
    return (x**z)


def sqrt(x):
    #return quotient of x/z
    return x**0.5

def main():
    print("-----adv calculator------")   
    print (f"100 % 30 = {mod(100,30)}")
    print (f"12 ** 2 = {power(12,2)}")
    print (f" \N{square root} = {sqrt(25)}")
    return None

if __name__ == "__main__":
    #only exec if ran directly as a script, ignore if imported as a module
    main()
    sys.exit(0)
