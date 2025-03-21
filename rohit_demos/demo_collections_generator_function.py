#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: gen func to yield 1 object at a time



def get_numbers():
    """return list of numbers"""
    numbers = []
    for x in range(0,100):
        numbers.append(x)
    return (numbers)


def generate_numbers():
    """ yield one object from collection at a time """
    for x in range (0,1000):
        yield x

#for z in get_numbers():
for z in generate_numbers():
    print(z)


# alt gen function
gen = generate_numbers()

while True:
    #num = next(gen, False)
    #fails when first value is 0, as it evaluates to False
    
    num = next(gen, -1)

    if num:
        print(num)
    else:
        break

#alternative, request next yielded value manually

gen = generate_numbers()
num1 = next(gen)
num2 = next(gen)
num3 = next(gen)
print(num1, num2, num3)
