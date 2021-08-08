# Given array denoting heights of n towers and a positive number k, you have to modify 
# the height of each tower either by increasing or decreasing by k only once.
# After modifying, height should be non-negative integer.

# Your task is to minimise the maximum difference between heights
# Example: arr = [1, 5, 8, 10], k = 2
# modified arr = [3, 3, 6, 8] -> ans = 8-3 = 5


# When -ve height is allowed
def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[-1] - arr[0] 
    small, big = 0, 0
    
    for i in range(1,n):
        small = min(arr[0]+k, arr[i]-k) 
        big = max(arr[i-1]+k, arr[-1]-k) 
        ans = min(ans, big-small) 
			
    return ans

arr = [8, 1, 5, 4, 7, 5, 7, 9, 4, 6]
k = 5
print(getMinDiff(arr, len(arr), k))

# 6 9 9 10 10 11 12 12 3 4

# When -ve height is not allowed
def solve(arr, n, k):
    arr.sort()
    ans = arr[-1] - arr[0]
    for i in range(1, n):
        small = min(arr[0]+k, arr[i]-k)
        big = max(arr[i-1]+k, arr[-1]-k)
        if small >= 0:
            ans = min(ans, big-small)
    return ans

arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
k = 5
print(solve(arr, len(arr), k))


# Method 2
def solve(arr, n, k):
    arr.sort()
    minv = [x-k for x in arr]
    maxv = [x+k for x in arr]    
    ans = arr[-1] - arr[0]
    for i in range(1, n):
        if minv[i] >= 0:
            small = min(maxv[0], minv[i])
            big = max(maxv[i-1], minv[-1])
            ans = min(ans, big-small)
    return ans

arr = [3, 9, 12, 16, 20]
k = 3
print(solve(arr, len(arr), k))

