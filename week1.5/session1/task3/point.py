# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.hypot(self.x, self.y)

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.hypot(dx, dy)

p1 = Point(6.7, 3.4)
p2 = Point(2, 3)
print(p1.x, p1.y)
print(int(p1.distance()))
print(int(p1.distance_to(p2)))
    
    # Add constructor here

    # Add distance() method here

    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
