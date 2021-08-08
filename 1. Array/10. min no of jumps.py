


def solve(arr, n):
    ptr = jump = 0
    count = 0
    for i in range(n):
        ptr += jump
        if ptr >= n-1:
            return count
        jump = arr[ptr]

        if jump <= 0:
            return -1
        count += 1

arr = [1,3,5,8,9,2,6,7,6,8,9]
# arr = [1, 4, 3, 2, 6, 7]
print(solve(arr, len(arr)))

