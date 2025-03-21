#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: range function using floating point


def frange(start, stop, step=0.25):
    curr = start
    if step==0 or start>stop:
        print("incompatible values")
    else:
        curr = float(start)
        while curr < stop:
            yield curr
            curr+=step


print(list(frange(-1,-0.5,1)))
      

