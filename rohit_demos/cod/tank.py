#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: This module defines a class of tank 

"""
    Tank class for an online game
"""
import vehicle

class Tank(vehicle.Vehicle):
    # Class has 2 components -- attibuted/ data + behaviour (methods)
    def __init__(self, country, model): #constructor - used to init every tank object
        super().__init__(country,model)
        self._location = {'x':0, 'y':0, 'z':0}        
        self._direction = 0
        self._shells = 20
        self._health = 100

        # no explicit return as this method is called implicitely

    def accel(self, increase):
        self._speed += increase
        return None
    
    def decel(self, decrease):
        self._speed -=decrease
        return None
    
    def rotate_left(self,degrees):
        self._direction -= degrees % 360
        return None
    

    def rotate_right(self,degrees):
        self._direction += degrees % 360
        return None
    
    def shoot(self):
        self._shells = -1
        return None
    
    def take_damage(self,damage):
        self._health -= damage
        return None


    def __del__(self):
        print ("Boom, tank has been destroyed")
        return None

    #special methods
    #operator overloading
    def __add__(self,other):
        self._health + other._health
        return self._health + other._health
    
    #duck typing - tank can now quack like a duck - tank object represented as a string
    def __str__(self):
        return(f"Model = {self.model}, Speed = {self._speed}, Health = {self._health}")

#getter and setter
    def get_health(self):
        return self._health
    
    def set_health(self, new_health):
        self._health = new_health
        #return self._health
        return None
    
    #wrap one variable name interface go getter/ setter methods
    tank_health = property(get_health, set_health)