# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle
import math
import pytest
from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)

def test_cirlce_constructor():
    test_radius = 5.0
    c = Circle(test_radius)
    assert c.radius == 5.0

def test_circle_area():
    radius = 5.0
    expected = math.pi * radius ** 2
    c = Circle(radius)
    res = c.area
    assert res == pytest.approx(expected)

def test_circle_perimeter():
    r = 5.0
    expected = 2 * math.pi * r
    c = Circle(r)
    res = c.perimeter
    assert res == pytest.approx(expected)
    # complete the implementation for
    # testing distance_to()
    

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates
