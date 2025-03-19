#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: generate 6 random unique numbers

"""
Docstring:
"""

import random
lotto = []


"""
num = random.randint(1,50)
lotto.append(num)

num = random.randint(1,50)
lotto.append(num)

num = random.randint(1,50)
lotto.append(num)

num = random.randint(1,50)
lotto.append(num)

num = random.randint(1,50)
lotto.append(num)

num = random.randint(1,50)
lotto.append(num)
"""


"""
while len(lotto)<6:
    num = random.randint(1,50)
    lotto.append(num)
"""


while len(lotto)<6:
    num = random.randint(1,50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number generated", num)

print("lottery numbers =", lotto)