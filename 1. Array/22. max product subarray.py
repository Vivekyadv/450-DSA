# Given an array that contains both positive and negative integers, find the product of 
# the maximum product subarray. Expected Time complexity is O(n) and only O(1) extra 
# space can be used.

# Example: arr = [6, -3, -10, 0, 2] 
# ans = 180    [6, -3, -10]


# Method 1: Brute Force 
def maxProduct(arr, n):
    result = arr[0]
    for i in range(n):
        mul = arr[i]
        for j in range(i + 1, n):
            result = max(result, mul)
            mul *= arr[j]

        result = max(result, mul)
    return result

arr = [-8, 5, 3, 1, 6]
print(maxProduct(arr, len(arr)))


# Method 2
def maxProduct(arr, n):
    if n == 1:
        return arr[0]
    max_end = 1
    min_end = 1
    maxSoFar = flag = 0

    for i in range(0, n):
        if arr[i] > 0:
            max_end = max_end * arr[i]
            min_end = min(min_end * arr[i], 1)
            flag = 1

        elif arr[i] == 0:
            max_end = 1
            min_end = 1

        else:
            temp = max_end
            max_end = max(min_end * arr[i], 1)
            min_end = temp * arr[i]
        if maxSoFar < max_end:
            maxSoFar = max_end
            
    if flag == 0 and maxSoFar == 0:
        return 0
    return maxSoFar


arr = [2, 3, 4, 5, -1, 0]
print(maxProduct(arr, len(arr)))
