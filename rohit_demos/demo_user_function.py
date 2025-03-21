#! /usr/bin/env pythong3
# Author: Rohit Ghodke
# Description: functions


"""

def say_hello():
    message = "hello" + " " + "my friends"
    print(message)
    return None

    say_hello()

"""

"""
def say_hello(greeting, recipient):
    #message = greeting + " " + recipient
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello(recipient = 3.14, greeting = "hello")

"""

def say_hello(greeting:str="namaste", recipient:str="dost")->None:
    #message = greeting + " " + recipient
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello(recipient = 3.14, greeting = "hello")

print(f"Annotations for say_hello = ", say_hello.__annotations__)
