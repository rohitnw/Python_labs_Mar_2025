#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: leap year - ex 3-3


year = int(input('Please enter a year: '))
if year%400 == 0 :
    print("leap year", year)
elif year%100!=0 and year%4==0:
    print("not leap year", year)
elif year%4==0:
    print("leap year", year)
else:
    print("not leap year")
