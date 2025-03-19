#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: format str concat, escape char,  str justification methods, .format methods, f-strings

planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.12313,
           'Mars': 227.94
           }

for planet in planets.keys():
    print("\t\t" + planet + ":" + str(planets[planet]) + "Gm\t" + str(hex(0xff)))

print ("-- -- " * 10)

for planet in planets.keys():
    print("{0:>12s}: {1:12.3f} Gm {2:#5x}".format(planet, planets[planet],0xff))

#using fstrings
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:12.3f} Gm {0xff:#5x}")
