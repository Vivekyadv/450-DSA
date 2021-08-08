# Given an array of integers. Find if there is a subarray with 0 sum
# Example 
# arr = [4,2,-3,1,6,2]  -> [2,-3,1] sum is 0

def solve(arr,n):
    sumVal = set()
    arrSum = 0
    for i in range(n):
        arrSum += arr[i]
        if arrSum == 0 or arrSum in sumVal:
            return True
        sumVal.add(arrSum)
    return False

arr = [4, 2, -3, 1, 6]
print(solve(arr, len(arr)))
