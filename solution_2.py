"""
    Copyright © 2023 Matthew Vallance, All rights reserved.
    Author: Matthew Vallance 001225832
    Description: Solution 1 for quadrants question
    Date: 26/02/23
"""
# Get data from external file to keep this one clean
import test_data
import time


def process_coords(coordinates):
    # Setup variables
    erroneous_data = []
    # Counts for where each set of coordinates are
    coord_counts = {'total_count': 0, 'top_left': 0, 'top_right': 0, 'bottom_left': 0, 'bottom_right': 0, 'origin': 0,
                    'north': 0, 'east': 0, 'south': 0, 'west': 0}

    for coordinate_set in coordinates:
        # Split set into 'x' and 'y' variables (x = horizontal, y = vertical)
        try:
            x = int(coordinate_set[0])
            y = int(coordinate_set[1])
        except ValueError:
            erroneous_data.append(str(coord_counts['total_count']))

        # If statement to check where each set of coords is located
        if x > 0 and y > 0:
            coord_counts['top_right'] += 1
        elif x < 0 and y > 0:
            coord_counts['top_left'] += 1
        elif x < 0 and y < 0:
            coord_counts['bottom_left'] += 1
        elif x > 0 and y < 0:
            coord_counts['bottom_right'] += 1
        else:
            # Must be on axis or origin
            if x == 0 and y == 0:
                coord_counts['origin'] += 1
            elif x == 0 and y > 0:
                coord_counts['north'] += 1
            elif x == 0 and y < 0:
                coord_counts['south'] += 1
            elif x > 0 and y == 0:
                coord_counts['east'] += 1
            elif x < 0 and y == 0:
                coord_counts['west'] += 1

        coord_counts['total_count'] += 1

    # Print invalid data locations if needed
    if len(erroneous_data) > 0:
        print("Invalid data at position:", ", ".join(erroneous_data), "- check and retry")

    # Return data
    return coord_counts

# Lengths list for testing automation
lengths = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]
to_write = "Length,T1,T2,T3\n"
for length in lengths:
    data_name = f"data_{length}"
    tests = ""

    # Measure performance
    print('---- Performance of', str(length), 'data points ----')
    # Loop three times to get accurate performance measure
    for i in range(0, 3):
        start = time.time()
        # Run algorithm with each length of data
        processed_data = process_coords(getattr(test_data, data_name))
        end = time.time()

        # Add timings to CS string
        tests += str(end - start) + ","

        # Print results to console
        print('Top left quadrant: ', processed_data['top_left'])
        print('Top right quadrant: ', processed_data['top_right'])
        print('Bottom left quadrant: ', processed_data['bottom_left'])
        print('Bottom right quadrant: ', processed_data['bottom_right'])

        print('North: ', processed_data['north'])
        print('East:', processed_data['east'])
        print('South: ', processed_data['south'])
        print('West: ', processed_data['west'])

    # Format CSV
    to_write += str(length) + "," + tests + '\n'

# Write results to a text file - easier than pulling this information from the console
with open('testing_analysis/results_2.csv', 'w') as f:
    f.write(to_write)
