#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description:

"""
Docstring:
"""


num = 42
txt ="3"

"""
if txt < num:
    print("less than")
else:
    print("greater than")
"""

#fix1 - conver str to int
if int(txt) < num:
    print("less than")
else:
    print("greater than")


#fix2 - check what type of data they are
if isinstance(txt,int):
    if int(txt) < num:
        print("less than")
    else:
        print("greater than")

else:
    print("cannot compare str with int")

#fix4 - catch exception
try: 
    if txt < num:
        print("less than")
    else:
        print("greater than")
except TypeError:
    print("incompatible data types for comparison")