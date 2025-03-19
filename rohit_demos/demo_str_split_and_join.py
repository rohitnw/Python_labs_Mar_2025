#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: split() and join(). 

line = "root:x:0:0:The Super User:/root:/bin/ksh"

#since strings are immutable

fields = line.split(":") #returns list which is mutable
print(fields)

fields[4] = "The Administator"
fields[6] = "/bin/bash"

print(fields)

line = ":".join(fields) #return new str
print("Modified line = : ", line)