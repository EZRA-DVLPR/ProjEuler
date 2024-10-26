# Problem Description
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
# #######################################################################

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum = 0

for p in range (2,2000000):
    if isPrime(p):
        sum += p

print(sum)        

# Note: This one takes a very long time to solve