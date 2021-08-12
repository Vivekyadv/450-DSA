# Given row-column wise sorted matrix, find the kth smallest element 

# K = 3
#    10, 20, 30, 40
#    15, 25, 35, 45     
#    24, 29, 37, 48
#    32, 33, 39, 50
# 3rd smallest element is 20


# Method 1: Brute Force
def solve(matrix, k):
    r = len(matrix)
    c = len(matrix[0])
    elements = []
    for i in range(r):
        for j in range(c):
            elements.append(matrix[i][j])
    elements.sort()
    return elements[k-1]

matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [24, 29, 37, 48],
    [32, 33, 39, 50]
]
k = 7
print(solve(matrix, k))

# Time = n^2 * log(n^2)
# Space = O(n^2)


# Method 2: since every row and column is sorted, we can use binary search
