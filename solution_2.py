"""
    Copyright © 2023 Matthew Vallance, All rights reserved.
    Author: Matthew Vallance 001225832
    Description: Solution 1 for quadrants question
    Date: 26/02/23
"""
# Get data from external file to keep this one clean
from data_generator import data_generator_points
import time

# Get generated data
coordinates = data_generator_points.generate_coordinates(100000, True)

def process_coords(coordinates):
    # Setup variables
    erroneous_data = []
    # Counts for where each set of coordinates are
    coord_counts = {'total_count': 0, 'top_left': 0, 'top_right': 0, 'bottom_left': 0, 'bottom_right': 0, 'origin': 0, 'north': 0, 'east': 0, 'south': 0, 'west': 0}

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

# Measure performance
start = time.time()

processed_data = process_coords(coordinates)

end = time.time()
print(end - start)


# Print results
print('Top left quadrant: ', processed_data['top_left'])
print('Top right quadrant: ', processed_data['top_right'])
print('Bottom left quadrant: ', processed_data['bottom_left'])
print('Bottom right quadrant: ', processed_data['bottom_right'])

print('North: ', processed_data['north'])
print('East:', processed_data['east'])
print('South: ', processed_data['south'])
print('West: ', processed_data['west'])
