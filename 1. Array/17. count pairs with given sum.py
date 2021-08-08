# Given an array of N integers, and an integer K, find the number of pairs of elements 
# in the array whose sum is equal to K.

# Example: arr = [1, 5, 7, 1]   k = 6
# pairs = (1, 5) and (5, 1) -> total pairs = 2

# Method 1: Brute Force method
def solve(arr, n, k):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                count += 1
                
    return count

arr = [1,1,1,1]
print(solve(arr, len(arr), k=2))


# Method 2: 
# 1. Create a map to store frequency of each number
# 2. for every element (other than itself), if its complementry is present in map, count it
# 3. we've twice the required value stored in counter because every pair is counted 
#    twice. So divide by 2
from collections import Counter
def solve(arr, n, k):
    counter = Counter(arr)
    count = 0
    for i in range(n):
        comp = k - arr[i]
        count += counter[comp]
        if arr[i] + arr[i] == k:
            count -= 1
    
    return count//2

arr = [1,5,7,1]
print(solve(arr, len(arr), k=6))

