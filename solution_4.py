"""
Author: Basil Shibu
Date:16/03/2023
Description: my final solution
"""

def get_quadrant(coords):
    x1, y1 = coords[0]
    x2, y2 = coords[1]

    if x1 == 0 and y1 == 0:
        quad1 = "Point 1 is at the origin"
    elif x1 == 0:
        quad1 = "Point 1 is on the y-axis"
    elif y1 == 0:
        quad1 = "Point 1 is on the x-axis"
    elif x1 > 0 and y1 > 0:
        quad1 = "Point 1 is in quadrant 1"
    elif x1 < 0 and y1 > 0:
        quad1 = "Point 1 is in quadrant 2"
    elif x1 < 0 and y1 < 0:
        quad1 = "Point 1 is in quadrant 3"
    elif x1 > 0 and y1 < 0:
        quad1 = "Point 1 is in quadrant 4"
    else:
     quad1 = "Invalid coordinates"

    if x2 == 0 and y2 == 0:
        quad2 = "Point 2 is at the origin"
    elif x2 == 0:
        quad2 = "Point 2 is on the y-axis"
    elif y2 == 0:
        quad2 = "Point 2 is on the x-axis"
    elif x2 > 0 and y2 > 0:
        quad2 = "Point 2 is in quadrant 1"
    elif x2 < 0 and y2 > 0:
        quad2 = "Point 2 is in quadrant 2"
    elif x2 < 0 and y2 < 0:
        quad2 = "Point 2 is in quadrant 3"
    elif x2 > 0 and y2 < 0:
        quad2 = "Point 2 is in quadrant 4"
    else:
        quad2 = "Invalid coordinates"

    return f"{quad1}, {quad2}"


coords = ((-2, 3), (4, -5))
print(get_quadrant(coords))
