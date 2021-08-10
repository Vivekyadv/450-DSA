# Given an array of +ve int of size n, where each value represents no of chocolates
# There are M students, the task is to distribute chocolate packets such that
# 1. each student gets exactly one packet
# 2. the difference between no of chocolates given to a student is minimum

# Arr = [3,4,1,9,56,7,9,12],  M = 5
# distribution = [3,4,9,7,9] -> min diff = 9-3 = 6

# Algorithm: sort the array and check the difference of ith element with (i+m)th element

def solve(arr, n, m):
    if m > n:
        return -1
    if m == 0 or n == 0:
        return 0
    
    arr.sort()
    result = arr[-1] - arr[0]
    for i in range(n-m+1):
        result = min(result, arr[i+m-1] - arr[i])
    return result

arr = [3,4,1,9,56,7,9,12]
m = 5
print(solve(arr, len(arr), m))
