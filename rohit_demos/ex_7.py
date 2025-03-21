#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: file unused ports in /etc/services

import re
import sys

file = r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/rohit_demos/mac_services"


all_ports = set(range(1,201))

used_ports = set()

with open(file, mode='rt') as fh_in:
    for line in fh_in:
        m=re.search(r"\d+)/(tcp|udp)", line)
        if m:
            print(m.group(1))
            if port <=200:
                unused_ports.add(port)

print(f"Allports = {all_ports}")
