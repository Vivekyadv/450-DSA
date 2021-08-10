# Given an array of integers and a number x, find the smallest subarray with sum 
# greater than the given value. It is guaranteed that x doesn't exceed sum(array)

# Arr = [1, 4, 45, 6, 0, 19], x = 51
# ans = 3   [4, 45, 6]

# Method 1: Brute Force method
# Check sum of all possible subarray
def solve(arr, val):
    n = len(arr)
    lenSubArr = n + 1
    for i in range(n):
        currSum = 0
        for j in range(i, n):
            currSum += arr[j]
            if currSum > val:
                lenSubArr = min(lenSubArr, j - i + 1)
    return lenSubArr

arr = [1, 4, 45, 6, 0, 19]
val = 51
print(solve(arr, val))


# Method 2

def solve(arr, n, x):
    currSum = 0
    minLen = n + 1
    i = j = 0
    while j < n:
        while currSum <= x and j < n:
            currSum += arr[j]
            j += 1
        while currSum > x and i < n:
            minLen = min(minLen, j - i)
            currSum -= arr[i]
            i += 1

    return minLen

arr = [1, 4, 45, 6, 0, 19]
val = 51
print(solve(arr, len(arr), val))

