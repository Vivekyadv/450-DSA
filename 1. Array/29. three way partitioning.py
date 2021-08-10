# Given an array of size n and a range [a, b]. The task is to partition the array 
# around the range such that array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to 
# return the modified array.

# Note: this is variation of Dutch National Flag problem
def solve(arr, a, b):
    i = j = 0
    k = len(arr) - 1
    while j <= k:
        if arr[j] < a:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > b:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1
    
    return arr

arr = [1, 2, 3, 3, 4]
a = 1
b = 2
print(solve(arr, a, b))




def solve(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n//2]
    else:
        a = arr[n//2 - 1]
        b = arr[n//2]
        return (a+b)//2

arr = [1,3,5,6,9,10]
print(solve(arr))