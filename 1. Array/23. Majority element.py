# Given interger array of length n, find all elements which appears more than n/3 times

# Method 1: using counter 
from collections import Counter
def solve(arr, n):
    counter = Counter(arr)
    result = []
    for ele in counter:
        if counter[ele] > n//3:
            result.append(ele)
    return result

# Time and Space O(n)


# Method 2: sort the array and then check arr[i] == arr[i+n/3]
def solve(arr, n):
    arr.sort()
    m = n//3
    result = []
    for i in range(n-m):
        if arr[i] == arr[i+m] and arr[i] not in result:
            result.append(arr[i])
    return result

arr = [1,2,1,3,5,5,4,4,4]
print(solve(arr, len(arr)))

# Time = n*log(n)
# Space = O(n)