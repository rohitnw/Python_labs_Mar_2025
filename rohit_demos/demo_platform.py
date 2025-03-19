#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: How to check which platform your script is running on

import sys

if sys.platform == "win32":
    print ("windows platform")
else:
    if sys.platform == "darwin":
        print("Running on macos")
    else:
        print("running on linux")

print (sys.platform)



import sys
import os
import glob

if sys.platform == "win32":
    print ("windows platform")
    home = os.environ["HOMEPATH"]
    pattern = home + r"\*"
else:
    if sys.platform == "darwin":
        print("Running on macos")
        home = os.environ["HOME"]
        pattern = home + r"/*"
    
    """else:
        print("running on linux")
        home = os.environ["HOME"]
        pattern = home + r"/*"
    """

print(sys.platform)
print("Home directory is:", home)
files = glob.glob(pattern) #return list of files + dir

print(files)

for file in files:
    if os.path.isfile(file):
        size = os.path.getsize(file)
        print(file,size)