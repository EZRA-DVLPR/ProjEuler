# Problem Description
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?
# #######################################################################

def isPrime(n : int):
    start = 2

    while start != n:
        if n % start == 0:
            return False

        start += 1

    return True

def findMPrime(m : int):
    start = 2
    numPrimesFound = 1

    while numPrimesFound != m:
        #keep finding primes
        start += 1

        if isPrime(start):
            numPrimesFound += 1

    return start

print(findMPrime(10001))