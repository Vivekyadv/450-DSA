# Given a row-wise sorted matrix of size R X C, find median of the matrix
# Example:
# matrix = [[1,3,5],
#           [2,6,9],        output = 5
#           [3,6,9]]
# 
# median of [1,2,3,3,5,6,6,9,9] -> 5

# Method 1:
# store elements of matrix in array, sort the array then return mid element in sorted array
# if number of elements in array is even, then return average of middle two elements

# Time complexity -> O(rc*log(rc))
# Space complexity = O(rc)

# Method 2:
# median is (rc + 1)//2 th element 
# 1. x will be median if no of elements <= x is (1+rc)/2
# 2. first, find the maximum and maximum element in matrix
# 3. If no of elements <= x are (1+rc)//2 then it is median

from bisect import bisect_right as upper_bound
def median(matrix, r, c):
    minEle = 2**32
    maxEle = -2**32

    for i in range(r):
        minEle = min(minEle, matrix[i][0])
        maxEle = max(maxEle, matrix[i][-1])

    target = (1 + r*c)//2

    while minEle <= maxEle:
        mid = (minEle + maxEle)//2
        count = 0
        for i in range(r):
            count += upper_bound(matrix[i], mid)
        
        if count < target:
            minEle = mid + 1
        else:
            maxEle = mid - 1
    return minEle

matrix = [[1,3,5],
          [2,6,9],        
          [3,6,9]]

r = len(matrix)
c = len(matrix[0])
print(median(matrix, r, c))

