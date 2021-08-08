# Given an array, reverse the elements of array
# Example: [1,2,3,4] -> ans = [4,3,2,1]

# Method 1: List slicing
def solve(arr):
    return arr[::-1]

arr = [4, 5, 1, 2]
print(solve(arr))

# Method 2: using two pointers
def solve(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [2, 4, 8, 6, 3]
print(solve(arr))

# Method 3: using recursion
def solve(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    return solve(arr, start+1, end-1)

arr = [2, 4, 8, 6, 3]
n = len(arr)
solve(arr, 0, n-1)
print(arr)