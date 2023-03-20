"""
Author: Varnika Mogali
Description: This is my coursework solution which includes time complexity
and varying data lengths so that large inputs can be tested to see how the run times vary for each.
Date: 15/03/23
"""


from random import randint
from queue import Queue
import time
import test_data

""" 
This is a function that finds which quadrant the coordinates are located in,
The function allocates which quadrant the point is in, based on the values of the coordinates.
If the point is on an axis or at the origin, the function returns a statement stating this.
"""


def find_quadrant(coord):
    x1, y1 = coord
    if x1 == 0 and y1 == 0:
        return "Origin"
    elif x1 == 0:
        return "On the y-axis"
    elif y1 == 0:
        return "On the x-axis"
    elif x1 > 0 and y1 > 0:
        return "Quadrant 1"
    elif x1 < 0 and y1 > 0:
        return "Quadrant 2"
    elif x1 < 0 and y1 < 0:
        return "Quadrant 3"
    elif x1 > 0 and y1 < 0:
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


def process_coordinates(data):
    coords = Queue()
    for i in range(1, len(data)):
        c_set = data[i]
        print(c_set)
        x = c_set[0]
        y = c_set[1]
        coords.put((x, y))

    return coords


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
lengths = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]
to_write = "Length,T1,T2,T3\n"
# for length in lengths:
data_lengths = [2]
for length in lengths:
    data_name = f"data_{length}"
    tests = ""

    # Run three times
    for i in range(0, 3):
        start = time.time()
        # Process coordinates
        coords = process_coordinates(getattr(test_data, data_name))
        # Sort coordinates
        sorted_coords = sort_coordinates(coords)
        # Finds the quadrant for each coordinate set
        find_quadrants(sorted_coords)
        end = time.time()
        # Add timings to CS string
        tests += str(end - start) + ","

    # Format CSV
    to_write += str(length) + "," + tests + '\n'

# Write results to a CSV file - easier than pulling this information from the console
with open('testing_analysis/results_3.csv', 'w') as f:
    f.write(to_write)
