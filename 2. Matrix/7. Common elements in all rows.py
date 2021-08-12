# Given rXc matrix, find all common elements present in all rows in O(rXc) time
# and one traversal

# Matrix:
# 1 2 1 4 8
# 3 7 8 5 1         common elements = 1, 8
# 8 7 7 3 1
# 8 1 2 7 9


def solve(matrix, r, c):
    store = dict()
    common = []
    for j in range(c):
        store[matrix[0][j]] = 1

    for i in range(1, r):
        for j in range(c):
            num = matrix[i][j]
            if num in store and store[num] == i:
                store[num] = i + 1
                if i == r - 1:
                    common.append(matrix[i][j])
    return common

matrix = [
    [1,2,1,4,8,8],
    [3,7,8,5,1,8],
    [8,7,7,8,3,1],
    [8,1,2,8,7,9]
]
r = len(matrix)
c = len(matrix[0])
print(solve(matrix, r, c))
