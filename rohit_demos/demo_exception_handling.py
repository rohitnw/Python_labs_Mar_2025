
#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: exception handling using try/ except blocks

import re
import sys


def search_pattern(pattern=r"^.{19}$", file=r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/labs/words"):
    lines = 0
    # Open file handle for READING in TEXT mode.
    fh_in = open(file, mode="rt"):
        reobj = re.compile(pattern)
        for line in fh_in:
           #m = re.search(pattern, line)  # MATCH lines start/end SAME CAPITAL
           m = re.obj.search(line)
           if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    fh_in.close()
    return lines

def __main__():
    lines_matched = 0
    lines_matched += search_pattern()
    lines_matched += search_pattern(r"^([A-Z]).*\1$",
                                    file=r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/labs/words")
    print(f"Lines matched = {lines_matched}")
    return None

if __name__ == __main__:
    main()
    sys.exit(0)