"""
Author: Kayleigh Harmsworth
Date: 28/02/23
Description: My final solution to the coursework problem provided.
"""
import random

def generate_coords():
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    coords = x,y
    quadrants(coords)
    return coords

def quadrants(coords):
    quad1 = []
    quad2 = []
    quad3 = []
    quad4 = []
    xAxis = []
    yAxis = []
    origin = []
    x = coords[0]
    y = coords[1]
    if x > 0 and y > 0:
        quad1.append(coords)
        print("Points in 1st quadrant", quad1)
    elif x < 0 and y > 0:
        quad2.append(coords)
        print("Points in 2nd quadrant =", quad2)
    elif x < 0 and y < 0:
        quad3.append(coords)
        print("Points in 3rd quadrant =", quad3)
    elif x > 0 and y < 0:
        quad4.append(coords)
        print("Points in 4th quadrant =", quad4)
    elif y == 0:
        xAxis.append(coords)
        print("Points on x-axis =", xAxis)
    elif x == 0:
        yAxis.append(coords)
        print("Points on y-axis =", yAxis)
    else:
        origin.append(coords)
        print("Points on origin =", origin)

i = 0
for i in range (0, 10000):
    generate_coords()
    i = i + 1
