# Find min and max element in array

INT_MAX = 2**32-1
INT_MIN = -2**32
def solve(arr):
    mn = INT_MAX
    mx = INT_MIN
    for i in range(len(arr)):
        if arr[i] > mx:
            mx = arr[i]
        if arr[i] < mn:
            mn = arr[i]
    return mx, mn

arr = [11, 6, 8, 10, 5, 23, 3]
print(solve(arr))


# Method 2: using min() and max() function
def solve(arr):
    mn = min(arr)
    mx = max(arr)
    return mx, mn

print(solve(arr))