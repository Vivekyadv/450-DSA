# Given string, check if it is palindrome or not

def isPalindrome(string):
    return int(string == string[::-1])


# Method 2
def isPalindrome(string):
    n = len(string)
    i = 0
    j = n-1
    while i <= j:
        if string[i] != string[j]:
            return 0
        else:
            i += 1
            j -= 1
    return 1

print(isPalindrome('this siht'))