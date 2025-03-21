#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: tank game

"""
    Tank game
"""

import sys
import tank

def main():
    #create / instanciate 3 new tank objects
    david_tank = tank.Tank('German', 'Tiger')
    rohit_tank = tank.Tank('american','sherman')
    john_tank = tank.Tank('british','churchill')
    
    #begin game
    david_tank.accel(59)
    rohit_tank.accel(32)

    john_tank.rotate_right(289)
    john_tank.accel(27)
    john_tank.shoot()

    #success
    david_tank.take_damage(65)
    rohit_tank.take_damage(40)
    
    #david tank gets a health boost
    #david_tank._health = 100
    #print (f"New Health of Davids tank is {david_tank._health}")    #poor code

    #visuals (prints)

    #print (f"Health of Davids tank is {david_tank._health}")
    print (f"Health of Davids and Rohit's tank is {david_tank + rohit_tank}")
    
    #print (f"Health of Rohit tank is {rohit_tank._health}")
    #print (f"Health of John tank is {john_tank._health}")
        
    david_tank.set_health(101) #example of a setter method
    print(f"Health of David's tank = {david_tank.get_health()}")

    david_tank.tank_health = 102
    print(f"Newhealth of David's tank = {david_tank.tank_health}")

    print(f"Status of David's tank = {david_tank}")



    return None

#Namspace trick

if __name__ == "__main__":
    main()
    sys.exit(0) #also causes all 3 tanks to be destroyed
