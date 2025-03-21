#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: match and substitute patterh with string using re.sub() or re.subn() functions


#sample using /etc/passwd on linux for root user account
import re

line = "root:x:0:0:The Super User:/root:/bin/ksh"

line = re.sub(r"[sS]uper [uU]Ser", r"Administrator", line)

print(f"Modifies string = {line}")