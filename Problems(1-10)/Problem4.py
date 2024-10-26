# Problem Description
#
# A palindromic number reads the same both ways. The largest palindrome from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers
# #######################################################################

def isPalindrome(n : int):
    #convert given int into a string
    nString = str(n)

    #start counting in place from 0 till 1/2 of length of string
    #if the char is not the same in both places => not a palindrome
    for i in range(0, (len(nString) // 2)):
        if (nString[i] != nString[- (i + 1)]):
            return False
    
    return True

def solver():
    currMax = -1

    for x in range(100,1001):
        for y in range(100, 1001):
            if ((isPalindrome(x * y)) and (currMax < x * y)):
                currMax = x * y

    return currMax

print(solver())
