"""
Author: Varnika Mogali
Description: This is the same as my coursework solution except it includes time complexity
and varying data lengths so that large inputs can be tested to see how the run times vary for each.
Date: 15/03/23
"""


from random import randint
from queue import Queue
import time
start = time.time()

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

def sort_coordinates(coords):
    coords_list = list(coords.queue)
    sorted_coords = merge_sort(coords_list)
    return sorted_coords

def find_quadrants(coords):
    for coord in coords:
        find_quadrant(coord)

# Now we can see how different large inputs affect the time complexity of my solution.
data_lengths = [50000]

for data_length in data_lengths:
    # Generates coordinates
    coords = generate_coordinates(data_length,True)
    sorted_coords=sort_coordinates(coords)

    # Finds the quadrant for each coordinate pair
    find_quadrants(sorted_coords)

end = time.time()
print("time is ",end - start)
