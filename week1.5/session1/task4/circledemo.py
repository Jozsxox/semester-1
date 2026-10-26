# Week 1.5, Session 1: Task 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:

    def __init__(self, radius, centre):
        self.r = radius
        self.c = centre

    def area(self):
        return math.pi*self.r**2

    def perimeter(self):
        return 2*math.pi*self.r

c = Circle(4, Point(1 ,0))
print(c.area())
print(c.perimeter())


# Add one or more impo:
# rt statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
