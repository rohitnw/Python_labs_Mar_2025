#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: simulate high street bank pin

import sys
import getpass

master_pin= "0123"
pin = None
attempt = 1

while pin != master_pin and attempt in range (4):
    pin = getpass.getpass("Enter pin: ")
    attempt+=1
    if pin == master_pin:
        print("valid pin")
        break
    else:
            print("Invalid pin")
else:
    print("too many attempts")

print("Done")

sys.exit(0)

#sys.exit("goodbye")
