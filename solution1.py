"""
    Copyright © 2023 Matthew Vallance, All rights reserved.
    Author: Matthew Vallance 001225832
    Description: Solution 1 for quadrants question
    Date: 26/02/23
"""
# Get data from external file to keep this one clean
from data_generator import data

coordinates = data.coordinates  # Get only first few items while we work on the solution

# Counts for where each set of coordinates are
top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0

for coordinate_set in coordinates:
    # Split set into 'x' and 'y' variables (x = horizontal, y = vertical)
    x = coordinate_set[0]
    y = coordinate_set[1]

    # If statement to check where each set of coords is located
    if x > 0 and y > 0:
        top_right += 1
    elif x < 0 and y > 0:
        top_left += 1
    elif x < 0 and y < 0:
        bottom_left += 1
    else:
        bottom_right += 1

# Print results
print('Top left: ', top_left)
print('Top right: ', top_right)
print('Bottom left: ', bottom_left)
print('Bottom right: ', bottom_right)


