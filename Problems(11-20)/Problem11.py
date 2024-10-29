# Problem Description
#
# In the 20 x 20 grid seen in Problem11.txt, there exist 4 numbers along a diagonal: 26 63 78 14, which when multiplied together equal 1788696.

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the grid?
# #######################################################################

import numpy as np

matrix = np.loadtxt('Problems(11-20)\\Problem11.txt', dtype=int)

maxProduct = -1

# for each cell find the largest product
for row in range(0, matrix.shape[0]):
    for col in range(0, matrix.shape[1]):
        cellMax = -1

        # if the row is less than 4, disregard up dir
        if row >= 4:
            temp = matrix[row][col] * matrix[row - 1][col] * matrix[row - 2][col] * matrix[row - 3][col]
            if cellMax < temp:
                cellMax = temp

        # if the row is greater than 16, disregard the down dir
        if row <= 16:
            temp = matrix[row][col] * matrix[row + 1][col] * matrix[row + 2][col] * matrix[row + 3][col]
            if cellMax < temp:
                cellMax = temp

        # if the col is less than 4, disregard up left
        if col >= 4:
            temp = matrix[row][col] * matrix[row][col - 1] * matrix[row][col - 2] * matrix[row][col - 3]
            if cellMax < temp:
                cellMax = temp

        # if the col is greater than 16, disregard the right dir
        if col <= 16:
            temp = matrix[row][col] * matrix[row][col + 1] * matrix[row][col + 2] * matrix[row][col + 3]
            if cellMax < temp:
                cellMax = temp

        # if the row and col are less than 4, disregard diagtopleft
        if row >= 4 and col >= 4:
            temp = matrix[row][col] * matrix[row - 1][col - 1] * matrix[row - 2][col - 2] * matrix[row - 3][col - 3]
            if cellMax < temp:
                cellMax = temp

        # if the row and col are greater than 16, disregard diagbotright
        if row <= 16 and col <= 16:
            temp = matrix[row][col] * matrix[row + 1][col + 1] * matrix[row + 2][col + 2] * matrix[row + 3][col + 3]
            if cellMax < temp:
                cellMax = temp

        # if the row is less than 4 and col is greater than 16, disregard diagtopright
        if row >= 4 and col <= 16:
            temp = matrix[row][col] * matrix[row - 1][col + 1] * matrix[row - 2][col + 2] * matrix[row - 3][col + 3]
            if cellMax < temp:
                cellMax = temp

        # if the row is greater than 16 and col is less than 4, disregard diagbotleft
        if row <= 16 and col >= 4:
            temp = matrix[row][col] * matrix[row + 1][col - 1] * matrix[row + 2][col - 2] * matrix[row + 3][col - 3]
            if cellMax < temp:
                cellMax = temp
        
        if maxProduct < cellMax:
            print("currMax dims are ", row, col)
            maxProduct = cellMax

print(maxProduct)