# Problem Description
#
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 19)^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# #######################################################################

def findSumOfSquares(n : int):
    sum = 0

    for i in range(1, n + 1):
        sum += i**2

    return sum

def findSquareofSums(n : int):
    sum = 0

    for i in range(1, n + 1):
        sum += i

    return sum**2

def findDifference(n : int):
    sumSquares = findSumOfSquares(n)
    squareSums = findSquareofSums(n)

    return squareSums - sumSquares

print(findSumOfSquares(10))
print(findSquareofSums(10))
print(findDifference(10))

print(findDifference(100))