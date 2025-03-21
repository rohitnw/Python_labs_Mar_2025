#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: regex string testing and pattern matching


#open file handle for reading in text mode
fh_in = open(r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/labs/words", mode="rt")

#iterate through file handle one line at a time

"""
for line in fh_in:
    #example of str testing
    #if line.startswith("Y") and line.endswith("n\n"): #\n - as all lines end with a newline \n
    #if line.startswith("Y") and line.rstrip("\n").endswith("n"):
    if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
        print(line, end = "") #end="" disables implicit newline in print statement

fh_in.close() #close file handle
"""

import re

for line in fh_in:
    #m = re.search("the", line)
    #m = re.search("^the", line)
    #m = re.search("ing$", line)
    #m = re.search("^ring$", line)
    #m = re.search("^.ing$", line)
    #m = re.search("^[adrp]ing$", line)
    #m = re.search("^[A-Z]", line)
    #m = re.search("^...................$", line)
    #m = re.search("[aeiou][aeiou][aeiou]", line)
    #m = re.search("[.]", line) #\. gives a warning
    #m = re.search("^[A-Z].*[A-Z]$", line) #start and end with capital letters

    #m = re.search("^.{19}$", line)
    #m = re.search("[aeiou]{3}", line)
    #m = re.search("[aeiou]{5,}", line)
    #m = re.search("^[A-Z].{4}[A-Z]$", line) #start and end with capital letters
    #m = re.search("^(.)(.).\\2\\1$", line) #palindrone  - to escape \, but r recommended - next ex
    #m = re.search(r"^(.)(.).\2\1$", line) #palindrone - sting to be passed as raw string
    #m = re.search(r"^([A-Z]).*\1$", line) #start and end with same capital letter
    
    #if m:
    #    print(line) #matching lines with 'the'
    
    m = re.search(r"^([A-Z]).*\1}$", line) #
    if m:
        print(f"matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")

fh_in.close() #close file handle
