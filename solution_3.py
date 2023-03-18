"""
Author: Varnika Mogali
Description: This is my coursework solution which includes time complexity
and varying data lengths so that large inputs can be tested to see how the run times vary for each.
Date: 15/03/23
"""


from random import randint
from queue import Queue
import time
start = time.time()

""" 
This is a function that finds which quadrant the coordinates are located in,
The function allocates which quadrant the point is in, based on the values of the coordinates.
If the point is on an axis or at the origin, the function returns a statement stating this.
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

Adapted the DataGenerator script written by Matthew Vallance (group member) for our coursework to generate the 
coordinates. I have adapted the function to add the pairs to a queue titled coords.
Reference:
Title: DataGenerator
Author: Matthew Vallance 
Date: 26/02/23
Code version: Python3
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
This is a function that implements the merge sort algorithm to sort a list of coordinate pairs.

Adapted the MergeSort implementation from the GeeksforGeeks website to use in my solution.
Reference:  
Title: MergeSort 
Author: GeeksforGeeks 
Date: last updated - 17 Feb 2023 
Code version: Python3 
Availability: https://www.geeksforgeeks.org/merge-sort/ 
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
This is a function takes two sorted lists and merges them into a new sorted list.

Reference:   
Title: MergeSort  
Author: GeeksforGeeks  
Date: last updated - 17 Feb 2023  
Code version: Python3  
Availability: https://www.geeksforgeeks.org/merge-sort/  
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
This is a function that takes a queue of coordinate pairs, 
converts it to a list and sorts it using the merge_sort() function 
and returns the sorted list of coordinate pairs.
"""


def sort_coordinates(coords):
    coords_list = list(coords.queue)
    sorted_coords = merge_sort(coords_list)
    return sorted_coords


"""
This is a function that takes a list of sorted coordinate pairs,
iterates through each pair, and uses the `find_quadrant' function.
"""


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
