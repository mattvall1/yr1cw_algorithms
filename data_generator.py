"""
    Author: Matthew Vallance 001225832
    Purpose: Script to generate data for the coursework question in the following format: {(x1, y1), (x2, y2)}
    Date: 21/02/23
"""
from random import randint

# Function to generate coordinates
def generate_coordinates(data_length):
    coords_to_return = []
    # Loop
    for num in range(1, data_length):
        # Generate 4 random coordinates
        x1 = randint(0, 100)
        y1 = randint(0, 100)
        x2 = randint(0, 100)
        y2 = randint(0, 100)
        # Add coordinates to data structure
        coords_to_return.append([[x1, y1], [x2, y2]])

    return coords_to_return

# Run data generation - change first parameter for different lengths of data
print(generate_coordinates(10000))