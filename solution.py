"""
    Copyright © 2023 Matthew Vallance, All rights reserved.
    Author: Matthew Vallance 001225832
    Description: Solution 1 for quadrants question
    Date: 26/02/23
"""
# Get data from external file to keep this one clean
from data_generator import data

# Setup variables
coordinates = data.coordinates  # Get only first few items while we work on the solution
erroneous_data = []

# Counts for where each set of coordinates are
processed_data = {'total_count': 0, 'top_left': 0, 'top_right': 0, 'bottom_left': 0, 'bottom_right': 0, 'origin': 0, 'north': 0, 'east': 0, 'south': 0, 'west': 0}

for coordinate_set in coordinates:
    # Split set into 'x' and 'y' variables (x = horizontal, y = vertical)
    try:
        x = int(coordinate_set[0])
        y = int(coordinate_set[1])
    except ValueError:
        erroneous_data.append(str(processed_data['total_count']))

    # If statement to check where each set of coords is located
    if x > 0 and y > 0:
        processed_data['top_right'] += 1
    elif x < 0 and y > 0:
        processed_data['top_left'] += 1
    elif x < 0 and y < 0:
        processed_data['bottom_left'] += 1
    elif x > 0 and y < 0:
        processed_data['bottom_right'] += 1
    else:
        # Must be on axis or origin
        if x == 0 and y == 0:
            processed_data['origin'] += 1
        elif x == 0 and y > 0:
            processed_data['north'] += 1
        elif x == 0 and y < 0:
            processed_data['south'] += 1
        elif x > 0 and y == 0:
            processed_data['east'] += 1
        elif x < 0 and y == 0:
            processed_data['west'] += 1

    processed_data['total_count'] += 1

# Print invalid data locations if needed
if len(erroneous_data) > 0:
    print("Invalid data at position:", ", ".join(erroneous_data), "- check and retry")

# Print results
print('Top left quadrant: ', processed_data['top_left'])
print('Top right quadrant: ', processed_data['top_right'])
print('Bottom left quadrant: ', processed_data['bottom_left'])
print('Bottom right quadrant: ', processed_data['bottom_right'])

print('North: ', processed_data['north'])
print('East:', processed_data['east'])
print('South: ', processed_data['south'])
print('West: ', processed_data['west'])
