# Problem Description
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# #######################################################################

def pythagoreanTripletChecker(a,b,c):
    if ((a ** 2) + (b ** 2)) == (c**2):
        return True
    else:
        return False

def checkSum(a,b,c):
    if (a + b + c == 1000):
        return True
    else:
        return False

def isSoln(a,b,c):
    if checkSum(a,b,c) and pythagoreanTripletChecker(a,b,c):
        return True
    else:
        return False

def solver():
    for c in range(5, 1000):
        for b in range(4, c):
            for a in range(3, b):
                if isSoln(a,b,c):
                    print("a = ",a)
                    print("b = ",b)
                    print("c = ",c)
                    return

solver()