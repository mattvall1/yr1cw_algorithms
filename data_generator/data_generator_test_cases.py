"""
    Copyright © 2023 Matthew Vallance, All rights reserved.
    Author: Matthew Vallance 001225832
    Description: Script to generate data for the coursework question in the following format: {(x1, y1), (x2, y2)}
    Date: 26/02/23
"""
from random import randint


# Function to generate coordinates
def generate_coordinates(data_length):
    coords = []
    # Loop
    for num in range(1, data_length):
        # Generate 4 random coordinates
        x1 = randint(-100, 100)
        y1 = randint(-100, 100)
        # Add coordinates to data structure
        coords.append([x1, y1])

    return coords


# Run data generation and write data to file
lengths = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]
to_write = ''
for length in lengths:
    to_write += 'data_' + str(length) + ' = ' + str(generate_coordinates(length))
    to_write += '\n'

# Write data to text file
try:
    with open('data.py', 'w') as f:
        f.write(to_write)
    print("Complete")
except:
    print("Fail")
