# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P637DJJGVosH1WaG_odlnYIBojg2yHEe

# NUMPY ASSIGNMENT

## 1. What is a Python library? Why ^o we use Python libraries?
"""

# A library is a collection of code that makes everyday tasks more efficient. Using Seaborn, for example, you can generate visualisations
# with just one line of code. To create a chart from an object, you’d have to write a lot of code without a library like this. Python is a popular
# choice for data analysis because of its extensive library of tools for manipulating, visualising, and training machine learning models.

"""## 2. What is the ^ifference between Numpy array an^ List?"""

#1. one main difference between array and list is that lists can containg heterogenous data whereas the numpy array is a homogenous structure...
#2. since arrays are homogenous thats why all the calculations related to maths are fast in compare to lists.
#3. one major difference between them is memory allocation.

"""## 3. Fin^ the shape, size an^ ^imension of the following array?
### [[1, 2, 3, 4]
### [5, 6, 7, 8],
### [9, 10, 11, 12]]
"""

import numpy as np

arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])

#shape of array
arr.shape

# size
arr.size

# dimension:
arr.ndim

"""## 4. Write python co^e to access the first row of the following array?
### [[1, 2, 3, 4]
### [5, 6, 7, 8],
### [9, 10, 11, 12]]
"""

arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
arr

## accessing first row:
arr[0]



"""## 5. How ^o you access the element at the thir^ row an^ fourth column from the given numpy array?
### [[1, 2, 3, 4]
### [5, 6, 7, 8],
### [9, 10, 11, 12]]
"""

arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
arr

arr[2][3]



"""## 6. Write co^e to extract all o^^-in^exe^ elements from the given numpy array?
### [[1, 2, 3, 4]
### [5, 6, 7, 8],
### [9, 10, 11, 12]]
"""



"""## 7. How can you generate a ran^om 3x3 matrix with values between 0 an^ 1?"""

np.random.rand(3,3) # it generates a matrix between 0 and1

"""## 8. Describe the ^ifference between np.ran^om.ran^ an^ np.ran^om.ran^n?"""

# the main difference between both of them is that np.random.rand() will only genrate
# the random values between 0 and 1(excluded) while np.random.randn() will generate all the
# float values between 0 and 1 including 1 also.

"""## 9. Write co^e to increase the ^imension of the following array?
### [[1, 2, 3, 4]
### [5, 6, 7, 8],
### [9, 10, 11, 12]]
"""

arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
arr
arr.ndim

arr1 = np.expand_dims(arr,axis=0)
arr1

arr1.ndim

"""## 10. How to transpose the following array in NumPy?
### [[1, 2, 3, 4]
### [5, 6, 7, 8],
### [9, 10, 11, 12]]
"""

arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
arr

a = arr.T # transposing the array:
a

"""## 11. Consi^er the following matrix:
### Matrix A2 [[1, 2, 3, 4] [5, 6, 7, 8] [9, 10, 11, 12]]
### Matrix B2 [[1, 2, 3, 4] [5, 6, 7, 8], [9, 10, 11, 12]]
"""



"""## 12. Which function in Numpy can be use^ to swap the byte or^er of an array?

## 13. What is the significance of the np.linalg.inv function?
"""

# The NumPy linalg.inv function which can be used to determine the multiplicative inverse of a matrix of order n.
# The multiplicative inverse of a matrix is the reciprocal of a regular matrix just like the reciprocal of any other number in arithmetic.
# The inverse of a matrix helps us find out unknown variables in a system of linear equations using the matrix method and the formula given below:

# AX = B => X = A-1 B

# where, A= the coefficient matrix, A-1 is the inverse of the coefficient matrix,
# X is the matrix containing the unknown variables and B is the ordinate or determinant matrix

"""## 14. What ^oes the np.reshape function ^o, an^ how is it use^?"""

# this function changes the shape of the given array:
arr.reshape(6,2) # but the size should be same thius is the condition;

"""## 15. What is broa^casting in Numpy?"""

# In NumPy, we can perform mathematical operations on arrays of different shapes. An array with a smaller shape
# is expanded to match the shape of a larger one. This is called broadcasting
## for example:

"""

```
# This is formatted as code
```
THANKYOU
"""















