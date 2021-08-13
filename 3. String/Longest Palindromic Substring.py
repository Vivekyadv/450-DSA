# Given a string, find the longest substring which is palindrome. Incase of conflict, 
# return the substring which occurs first ( with the least starting index).

# Example: 'aaaaabbaa' -> 'aabbaa'
# 'abc' -> 'a' (since longest palindromic substrings are 'a', 'b', 'c'. result is the one
#           with least starting index)


# Method 1: Brute Force 
def solve(string):
    n = len(string)
    SubString = string[0]
    subStrLen = 1
    for i in range(n):
        for j in range(i+1, n):
            subStr = string[i:j+1]
            if subStr == subStr[::-1] and len(subStr) > subStrLen:
                subStrLen = len(subStr)
                SubString = subStr
    return SubString

string = 'aaaaaabbbaab'
print(solve(string))
# Time complexity = O(n^3)
# n^2 for substrings and O(n) for subStr == subStr[::-1]



# Dynamic Programming: 
def longestPalSubstr(string) :
    n = len(string)
    dp = [[0]*n for i in range(n)]
    maxLen = 1

    for i in range(n):
        dp[i][i] = 1
    
    left = 0
    i = 0
    while i < n - 1:
        if string[i] == string[i + 1]:
            dp[i][i + 1] = 1
            left = i
            maxLen = 2
        i += 1
    
    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and string[i] == string[j]:
                dp[i][j] = 1
                if k > maxLen:
                    left = i
                    maxLen = k
            i += 1
        k += 1
    
    return string[left:left+maxLen]
 
string = 'aaaabbaa'
print(longestPalSubstr(string))