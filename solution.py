"""
Author: Varnika Mogali
Description: Coursework solution
Date: 27/02/23
"""

# randint from random to generate random integers
# Queue from queue to create a queue data structure.
from random import randint
from queue import Queue

""" 
This is a function find which quadrant the coordinates are located in,
The function determines which quadrant the point is in, based on the values of the coordinates.
If the point is on an axis or at the origin, the function returns a string indicating this.
"""


def find_quadrant(coord):
    x1, y1 = coord[0]
    x2, y2 = coord[1]
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        return "Origin"
    elif x1 == 0 and x2 == 0:
        return "On the y-axis"
    elif y1 == 0 and y2 == 0:
        return "On the x-axis"
    elif x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0:
        return "Quadrant 1"
    elif x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0:
        return "Quadrant 2"
    elif x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0:
        return "Quadrant 3"
    elif x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0:
        return "Quadrant 4"
    else:
        return "Boundary point"


"""
The function generates random x and y values between -100 and 100 for both points of each pair, 
and then adds the pair to the coords queue. 
"""


def generate_coordinates(data_length, to_console=True):
    coords = Queue()
    for num in range(1, data_length):
        x1 = randint(-100, 100)
        y1 = randint(-100, 100)
        x2 = randint(-100, 100)
        y2 = randint(-100, 100)
        coords.put(((x1, y1), (x2, y2)))
    if to_console:
        return coords
    else:
        try:
            with open('data.txt', 'w') as f:
                f.write(str(list(coords.queue)))
            return "Complete"
        except:
            return "Fail"


"""
function implements the merge sort algorithm to sort a list of coordinate pairs.
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)


"""
function takes two sorted lists and merges them into a new sorted list.
"""


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


"""
sort_coordinates() function takes a queue of coordinate pairs, 
converts it to a list, sorts it using the merge_sort() function, 
and returns the sorted list of coordinate pairs.
"""


def sort_coordinates(coords):
    coords_list = list(coords.queue)
    sorted_coords = merge_sort(coords_list)
    return sorted_coords


"""
find_quadrants() function takes a list of sorted coordinate pairs,
iterates through each pair, and uses the `find_quadrant'
"""


def find_quadrants(coords):
    for coord in coords:
        print(f"{coord}: {find_quadrant(coord)}")


# Generate coordinates and sort them
coords = generate_coordinates(10000, True)
sorted_coords = sort_coordinates(coords)

# Find the quadrant for each coordinate pair
find_quadrants(sorted_coords)
