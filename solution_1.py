"""
Author: Kayleigh Harmsworth
Date: 28/02/23
Description: My final solution to the coursework problem provided.
"""
import random
import time
import test_data

# Unused function
def generate_coords():
    # generates pairs of coordinates
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    coords = x,y
    # calls the next function with it using the generated coordinates
    quadrants(coords)
    return coords

def quadrants(coords):
    #assigns blank arrays for each of the given sectors
    quad1 = []
    quad2 = []
    quad3 = []
    quad4 = []
    xAxis = []
    yAxis = []
    origin = []
    # allocates data to given varibales from the generated coordinates
    x = coords[0]
    y = coords[1]
    # gives parameters so the program can accurately assign each coordinate a sector
    if x > 0 and y > 0:
        # adds the coordinates to the list of all coordinates for that sector
        quad1.append(coords)
        # displays that the coordinate belong in this sector, and shows all coordinates found within that sector so far
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

# Lengths list for testing automation
lengths = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]
to_write = "Length,T1,T2,T3\n"
for length in lengths:
    data_name = f"data_{length}"
    tests = ""

    # Run three times
    for i in range(0, 3):
        # establishes the start of the program
        start = time.time()
        x = 0
        # establishing how many pairs of coordinates need to be generated, in this case 10000
        for x in range(0, len(getattr(test_data, data_name))):
            # calls the starting function
            coords = getattr(test_data, data_name)[x][0],getattr(test_data, data_name)[x][1]
            quadrants(coords)
            x = x + 1
        end = time.time()
        # Add timings to CS string
        tests += str(end - start) + ","

    # Format CSV
    to_write += str(length) + "," + tests + '\n'

# Write results to a text file - easier than pulling this information from the console
with open('testing_analysis/results_1.csv', 'w') as f:
    f.write(to_write)
