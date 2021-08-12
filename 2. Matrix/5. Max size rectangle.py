# Given a binary matrix. Find the maximum area of a rectangle formed only of 1's 
# in the given matrix.

#   0 1 1 0
#   1 1 1 1     max area =    1 1 1 1   ==> 4 * 2 = 8
#   1 1 1 1                   1 1 1 1
#   1 1 0 0

# Approach: This problem can be solve using Largest Rectangle in Histogram
# Convert each row into height of histogram. then find the largest rectangle in each row
# 
# Histogram of each row:
# For ith row = add up the height till first row, if there is 0 in ith row, height of
#               that column is 0
# Example -> Height of histogram for each row in above metrix is
# 0 1 1 0
# 1 2 2 1
# 2 3 3 1
# 3 4 0 0


def Histogram(row):
    stack = []
    top_val = max_area = 0
    area = 0 

    i = 0
    while i < len(row):
        if len(stack) == 0 or row[stack[-1]] <= row[i]:
            stack.append(i)
            i += 1
        else:
            top_val = row[stack.pop()]
            area = top_val * i
            if len(stack):
                area = top_val * (i - stack[-1] - 1)
            max_area = max(area, max_area)

    while len(stack):
        top_val = row[stack.pop()]
        area = top_val * i
        if len(stack):
            area = top_val * (i - stack[-1] - 1)
        max_area = max(area, max_area)

    return max_area

def maxRectangle(matrix, r, c):
    max_area = Histogram(matrix[0])
    for i in range(1, r):
        for j in range(c):
            if matrix[i][j] == 1:
                matrix[i][j] += matrix[i - 1][j]
        histogram_area = Histogram(matrix[i])
        max_area = max(max_area, histogram_area)

    return max_area

matrix = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]

r = len(matrix)
c = len(matrix[0])
print(maxRectangle(matrix, r, c))
