#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: ultrarealistic calclator app

"""
calc app with basic and adv functions
"""

import basic

"""to import specific functions/ objects

from basic import add
from basic import mul
from basic import div
"""


import adv
import sys

def main():

    while True:

        menu = """
            Calc options
            ------------
            1. Basic calc options
            2. Adv calc options    
            q = quit
        """

        print(menu)

        option = input (r"Enter option 1 - 2, quit:")
        print (option)

        if option == "1":
            print(f"50+40+30 = {basic.add(50,40,30)}") 
            print(f"50*40 = {basic.mul(50,40)}") 
            print(f"50/40 = {basic.div(50,40)}") 
        elif option == "2":
            print (f"50 % 40 = {adv.mod(50,40)}")
            print (f"50 ** 40 = {adv.power(50,40)}")
            print (f" \N{square root} 50 = {adv.sqrt(50)}")
        elif option =="q":
            break
        else:
            print("Invalid option")
    return None

if __name__ == "__main__":
    #only exec if ran directly as a script, ignore if imported as a module
    main()
    sys.exit(0)