# Given matrix and a key value. Find if key is present in matrix or not
# Matrix has properties 
# 1. each row is in sorted order
# 2. first int of each row is greater than last int of previous row

def BS(arr, key):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            r = mid - 1
        else:
            l = mid + 1
    return False

def solve(matrix, key):   
    l = 0
    h = len(matrix)-1
    while l <= h:
        mid = (l+h)//2
        if matrix[mid][0] <= key:
            if key <= matrix[mid][-1]:
                l = mid
                break
            else:
                l = mid + 1
        else:
            h = mid - 1
    return True if BS(matrix[l], key) else False

matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
key = 3 
print(solve(matrix, 3))

# Note: This solution does not work for matrix having either row = 1 or column = 1


# Method 2: Search for the row in which key lies, then search for the key in 
# that row using Binary Search.
def searchMatrix(matrix, key):
    indx = -1
    for i in range(len(matrix)):
        if matrix[i][0] <= key and key <= matrix[i][-1]:
            indx = i
            break
    if indx == -1:
        return False
    return True if BS(matrix[indx], key) else False

print(searchMatrix(matrix, key))
