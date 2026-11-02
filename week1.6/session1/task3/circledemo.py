# Week 1.6, Session 1: Task 3
import math 

class Point:
    def __init__(self, x, y):

        if not isinstance(x, int):
            raise TypeError("x coordinate must be an integer")

        if not isinstance(y, int):
            raise TypeError("x coordinate must be an integer")
            
        self.x = x
        self.y = y




class Circle:
    def __init__(self, radius, centre):
        self.r = radius
        self.c = centre
    

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
