#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: ex4 q1 - string handling

#          012345678901234567890123456789012345678901234567890123456789012345678901234567890 
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-" * len(Belgium))
print(Belgium)

#todo

Belgium2 = Belgium.replace(",",":")
print(Belgium2)

Belgium_split=Belgium.split(",")
print(Belgium_split)


pop_sum = int(Belgium_split[1]) + int(Belgium_split[3])
print(pop_sum)

print("-" * len(Belgium_split[1]))
