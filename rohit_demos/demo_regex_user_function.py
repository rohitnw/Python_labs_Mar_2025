#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: regex string testing and pattern matching



import re

"""
def search_pattern():

    with open(r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/labs/words",mode = "rt") as fh_in:
        for line in fh_in:
            m  = re.search(r"^([A-Z])).*\1$", line)
            if m:
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end}")
    return None

search_pattern()

"""



def search_pattern(pattern=r"^.{19}$", file=r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/labs/words"):
    lines = 0
    # Open file handle for READING in TEXT mode.
    with open(file, mode="rt") as fh_in:
        reobj = re.compile(pattern)
        for line in fh_in:
           #m = re.search(pattern, line)  # MATCH lines start/end SAME CAPITAL
           m = re.obj.search(line)
           if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    return lines

def __main__():
    lines_matched = 0
    lines_matched += search_pattern()
    lines_matched += search_pattern(r"^([A-Z]).*\1$",
                                    file=r"/Users/rghodke/Documents/python3_March_2025/Python_labs_Mar_2025/labs/words")
    print(f"Lines matched = {lines_matched}")
    return None

if __name__ == __main__:
    import cProfile
    cProfile.run("main()")
    sys.exit(0)