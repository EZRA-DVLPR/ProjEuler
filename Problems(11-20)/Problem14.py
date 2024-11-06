# Problem Description
#
# The following iterative sequence is defined for the set of positive integers:
#       n -> n/2 (n is even)
#       n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#       13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem) it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts, the terms are allowed to go above one million,

# #######################################################################

# Preliminary thoughts:
# If n starts on an even, then it will continuously divided by 2 until it reaches 1.
# Thus, we must check only odd numbers for n.
# Ideally, we find a number that when multiplied by 3 and adding 1 to that product, is odd.
# Is this possible?

# Pf: WTS that if n is odd, then 3 * n is also odd.
# let n be odd. 
#   => n % 2 == 1
#   => 2k + 1 = n for some k
# 3 * 1 == 3
# 3 * 2 == 6
# 3 * 3 == 9
# 3 * 4 == 12
# ...
# 3 * n = 3 * ((2 * k) + 1)
# 3 * n = 6k + 3
# 6k + 3 = (6k + 2) + 1
#        = 2(3k + 1) + 1, let X = (3k + 1)
#        = 2(X) + 1
# 6k + 3 = 2(X) + 1
# i.e. it's odd.
# Q.E.D.

# Therefore, for any n that is odd, when multiplied by 3, it is always odd.

def calcSequence(n, numSeq):
    if n == 1:
        numSeq += 1
        return numSeq
    elif n % 2 == 0:
        return calcSequence((n/2), (numSeq + 1))
    elif n % 2 == 1:
        return calcSequence(((3 * n) + 1), (numSeq + 1))

chain = -1
res = -1
curr = 1

while curr < 1000000:
    if chain < calcSequence(curr, 0):
        chain = calcSequence(curr, 0)
        res = curr
    
    # skip all evens since they will just reduce to 1 quicker
    curr += 2

print(res)