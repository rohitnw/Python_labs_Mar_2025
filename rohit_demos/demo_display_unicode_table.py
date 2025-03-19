#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: display unicode char set
# using interator for loop + range

for pos in range(0,65536):
    try:
        print(pos, chr(pos), end=" ")
        if pos%6==0:
            print()
    except UnicodeEncodeError:
        continue
        #print(" ")
