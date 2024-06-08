# Problem Description
#
# The prime factors of 13195 are 5, 7, 13, 29.

# What is the largest prime factor of 600851475143?
# #######################################################################

import numpy as np

#find prime factors of n
def primeFinder(n : int):
    primesList = np.array([], dtype=int)

    nextPrime = findNextPrime(n)
    primesList = np.append(primesList, nextPrime)

    while (n != nextPrime):
        n //= nextPrime
        nextPrime = findNextPrime(n)
        primesList = np.append(primesList, nextPrime)

    for prime in primesList:
        print(prime)

    return primesList[-1]


def findNextPrime(n : int):
    currVal = 2

    while ((currVal != n) and (n % currVal != 0)):
        currVal += 1

    return currVal
            
print(f"The last prime is: {primeFinder(600851475143)}")