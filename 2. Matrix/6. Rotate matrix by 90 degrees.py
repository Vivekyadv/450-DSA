# Given a matrix, rotate it with 90 degree clockwise

# 1 2 3             7 4 1
# 4 5 6     -->     8 5 2
# 7 8 9             9 6 3

# Method 1: Transpose the matrix and then reverse each row
def solve(matrix, n):
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

    return matrix

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = len(matrix)
print(solve(matrix, n)) 


# Method 2: reverse indices as well as rever row elements

# 00 01 02      20 10 00
# 10 11 12      21 11 01
# 20 21 22      22 12 02

def solve(matrix, n):
    for j in range(n):
        for i in range(n-1, -1, -1):
            print(matrix[i][j], end=" ")
        print()

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = len(matrix)
solve(matrix, n)


# Method 3: Rotate about diagonal (transpose)
# then rotate about middle column
# Note: This is method 1
def solve(matrix, n):
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
    
    return matrix

print(solve(matrix,n))