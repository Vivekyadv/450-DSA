# Given array, move all -ve elements to the left and all +ve to right 
# with constant extra space


# Method 1: 3 pointers approach, similar approach as we used for Dutch 
# National Flag problem (arr of 0's, 1's and 2's) 

def solve(arr, n):
    i, j = 0, 0
    k = n-1

    while i <= j <= k:
        if arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        if arr[j] == 0:
            j += 1
        if arr[j] > 0:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
    return arr

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(solve(arr, len(arr)))


# Method 2: using 2 pointers
def solve(arr, n):
    i = 0
    for j in range(n):
        if arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(solve(arr, len(arr)))


# Method 3: two pointers but from start and end of array
def solve(arr, n):
    l = 0
    r = n-1
    while l <= r:
        if arr[l] < 0 and arr[r] < 0:
            l += 1
        elif arr[l] < 0 and arr[r] > 0:
            l += 1
            r -= 1
        elif arr[l] > 0 and arr[r] < 0:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        elif arr[l] > 0 and arr[r] > 0:
            r -= 1

    return arr

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(solve(arr, len(arr)))

# This method is not recommended if there is 0 present in array
