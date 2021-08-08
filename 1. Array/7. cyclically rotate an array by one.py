# Given an array, rotate the array by one position in clockwise

# Example: arr = [9, 8, 7, 6, 4, 2, 1, 3]
# ans = [3, 9, 8, 7, 6, 4, 2, 1]


# Method 1: List slicing
def solve(arr, n):
    arr[:] = [arr[-1]] + arr[:n-1]
    return arr

arr = [9, 8, 7, 6, 4, 2, 1, 3]
print(solve(arr, len(arr)))


# Method 2: shift each element to forward
def solve(arr, n):
    last = arr[-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = last
    return arr

arr = [9, 8, 7, 6, 4, 2, 1, 3]
print(solve(arr, len(arr)))



# Method 3: using two pointers
# start = 0 and end = n-1
# swap(start, end) and increment start

def solve(arr, n):
    i, j = 0, n-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr

arr = [9, 8, 7, 6, 4, 2, 1, 3]
print(solve(arr, len(arr)))

# 9 8 7 6 4 2 1 3
# 3 8 7 6 4 2 1 9
# 3 9 7 6 4 2 1 8
# 3 9 8 6 4 2 1 7
# 3 9 8 7 4 2 1 6 
# 3 9 8 7 6 2 1 4
# 3 9 8 7 6 4 1 2
# 3 9 8 7 6 4 2 1

