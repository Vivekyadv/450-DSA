# Given a matrix of size r*c. Traverse the matrix in spiral form.

# Solution
def spiral(matrix):
    top = 0
    right = len(matrix[0])-1
    down = len(matrix)-1
    left = 0
    dirc = 0
    result = []
    while top <= down and left <= right:
        if dirc == 0:
            for j in range(left, right+1):
                result.append(matrix[top][j])
            top += 1
        
        elif dirc == 1:
            for i in range(top, down+1):
                result.append(matrix[i][right])
            right -= 1
        
        elif dirc == 2:
            for j in range(right, left-1, -1):
                result.append(matrix[down][j])
            down -= 1
        
        elif dirc == 3:
            for i in range(down, top-1, -1):
                result.append(matrix[i][left])
            left += 1
        
        dirc = (dirc + 1) % 4
    return result

