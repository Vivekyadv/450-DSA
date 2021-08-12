# Given a boolean 2D array of n x m dimensions where each row is sorted. 
# Find the 0-based index of the first row that has the maximum number of 1's.

# Arr[][] = {{0, 1, 1, 1},
#            {0, 0, 1, 1},
#            {1, 1, 1, 1},
#            {0, 0, 0, 0}}
# Ans = 2       -> Row 2 contains 4 1's


# Method 1: Brute Force 
# for every row, count no of 1's present, and update the index 
def solve(matrix, r, c):
    indx = -1
    maxCount = 0
    for i in range(r):
        count = sum(matrix[i])
        if count > maxCount:
            maxCount = count
            indx = i
    return indx


matrix = [[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
r = len(matrix)
c = len(matrix[0])
print(solve(matrix, r, c))


# Method 2:
# since each row is sorted, we can use binary search to count of 1's in each row.
# We've to find index of the first instance of 1 in each row
# Number of 1's = C - indx  (no of column - first index of 1)
def first(arr):
    l = 0
    h = len(arr) - 1
    while l <= h:		
        mid = l + (h - l)//2
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        elif arr[mid] == 0:
            l = mid + 1
        else:
            h = mid - 1
    return -1

def solve(matrix, r, c):
	firstRow = -1
	maxCount = -1
	for i in range(r):
		indx = first (matrix[i])
		if indx != -1 and c - indx > maxCount:
			maxCount = c - indx
			firstRow = i
	return firstRow

# Driver Code
matrix = [[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1],	[0, 0, 0, 0]]
r = len(matrix)
c = len(matrix[0])
print(solve(matrix, r, c))


# Method 3: 
# 1. start from the index = c-1 i.e last element of first row
# 2. we'll move from that index towards 0 i.e move left
# 3. while moving left, check for arr[i][index], if it is 1, then update the ans = i
# 4. if not, then increment i
def solve(matrix, r, c):
    firstRow = -1
    index = c-1
    i = 0
    while index >=0 and i < r:
        if matrix[i][index] == 1:
            index -= 1 
            firstRow = i
        else:
            i += 1
    return firstRow

matrix = [[0,0,0,0,1,1], [0,1,1,1,1,1], [0,0,0,0,0,1], [0,0,1,1,1,1], [1,1,1,1,1,1]]
r = len(matrix)
c = len(matrix[0])
print(solve(matrix, r, c))

