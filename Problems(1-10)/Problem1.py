# Problem Description
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
# #######################################################################

import numpy as np

# Input: n >= 1
# 
def isMultiple(n : int):

    toCheck = np.arange(1, n)

    sum = 0

    for elt in toCheck:
        #check for divisibility w/ 3 or 5
        if ((elt % 3 == 0) or (elt % 5 == 0)) :
            sum += elt

    return sum

print(isMultiple(1000))