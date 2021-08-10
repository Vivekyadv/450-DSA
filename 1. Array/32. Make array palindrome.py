# Given array, we need to make it palindrome, only allowed operation is merging elements
# To merge two adjacent elements just simply replace them with their sum. Task is to
# # minimise the operations
# 
# Example: arr = [10, 99, 22, 10] -> [10, 143, 10]
# min no of operations = 1


# Approach
# using two pointer technique, i = 0 and j = n-1
# check arr[i] and arr[j], if equal then i += 1 and j -= 1
# if arr[i] < arr[j] there is posibility that arr[i] + arr[i+1] can be equal to arr[j]
#   so add them and increment minOperation
# if arr[i] > arr[j], then add arr[j] with arr[j-1] and increment minOperation

# Example:
# arr = [6, 5, 3, 1, 9, 6]  , i = 0 and j = 5
# step 1: 6 == 6, so move i += 1 and j -= 1
# step 2: 5 < 9, so add 5 with its next element -> 5 + 3
#         now we consider array like: [6, 8, 1, 9, 6] and minOp = 1
# step 3: 8 < 9, so add 8 with its next element -> 8 + 1
#         now we consider array like: [6, 9, 9, 6] and minOp = 2
# step 4: 9 == 9, so move i += 1 and j -= 1
# now i > j -> so stop       minOp = 2

def solve(arr, n):
    minOp = 0
    i = 0
    j = n-1
    while i < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] < arr[j]:
            i += 1
            arr[i] += arr[i-1]
            minOp += 1
        else:
            j -= 1
            arr[j] += arr[j+1]
            minOp += 1
    return minOp

arr = [6, 5, 3, 1, 9, 6]
print(solve(arr, len(arr)))
