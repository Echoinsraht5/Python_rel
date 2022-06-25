# areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
#          "bedroom", 10.75, "bathroom", 10.50]
# areas_1 = areas + ['poolhouse24.5']
# print(areas_1)

# list_2 = [9, 3, 6, 12, 234624, 4364, 34763]
# list_2.sort(4364)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second


# Sort full in descending
# full_sorted = sorted(full, reverse = True)

# Print out full_sorted
# print(full_sorted)
print(sorted(full, reverse = True))
# print(full.sort(reverse = True)) == None # 直接print(full.sort(reverse = True))返回None


# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()
# print(place.upper()) 直接print(place.upper())是可行的

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
# print(reversed(areas))
# print(areas.reverse()) == None 直接print(full.reverse(reverse = True))返回None

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)


# Print out dist
print(dist)


# # Create list baseball
# baseball = [180, 215, 210, 210, 188, 176, 209, 200]
#
# # Import the numpy package as np
# import numpy as np
#
# # Create a numpy array from baseball: np_baseball
# np_baseball = np.array(baseball)
#
# # Print out type of np_baseball
# print(type(np_baseball))
#
#
# import numpy as np
# np.array_1 = np.array([True, 1, 2]) + np.array([3, 4, False])
# print(np.array_1)
#
# list_1 = [True, 1, 2]
# list_2 = [3, 4, False]
# list_3 = list_1 + list_2
# print(list_3)


list_1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(list_1[1])

# import numpy as np
import numpy as np

np_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_2 = np.array(([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np_1[0, 1:]))
print(np_1.shape)
print(np_1[0:, -2:])
print(type(np_2[0, 1:]))
print(np_2.shape)
print(np_2[0:, -2:]) # 最后结果与np_1一样，但细节上的区别在哪？？？


# Create baseball and updated, two lists of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
updated = [[2.3, 1.6],
            [1, -3.5],
            [0.66, 3.1],
            [1.5, -2.2]]

height = [180, 215, 210, 188]
weight = [78.4, 102.7, 98.5, 75.2]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
np_baseball_bmi = np.baseball[:, 0] / np.baseball[:, 1] ** 2
np_baseball_3d = np.baseball + np_baseball_bmi

# Print out the type of np_baseball
print(type(np_baseball))
print(np_baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)


# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversation = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball_3d * conversation)