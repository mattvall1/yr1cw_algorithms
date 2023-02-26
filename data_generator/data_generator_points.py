"""
    Copyright © 2023 Matthew Vallance, All rights reserved.
    Author: Matthew Vallance 001225832
    Description: Script to generate data for the coursework question in the following format: {(x1, y1), (x2, y2)}
    Date: 26/02/23
"""
from random import randint


# Function to generate coordinates
def generate_coordinates(data_length, to_console):
    coords = []
    # Loop
    for num in range(1, data_length):
        # Generate 4 random coordinates
        x1 = randint(-100, 100)
        y1 = randint(-100, 100)
        # Add coordinates to data structure
        coords.append([x1, y1])

    # Write data to text file - if option is chosen, else print to terminal
    if to_console:
        return coords
    else:
        try:
            with open('data.txt', 'w') as f:
                f.write(str(coords))
            return "Complete"
        except:
            return "Fail"


# Run data generation - change first parameter for different lengths of data, change second parameter to print to text file
print(generate_coordinates(10000, False))
