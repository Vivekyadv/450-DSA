# Given a number in form of array. return next permutation of this number
# If such arrangement is not possible, you must rearrange it as lowest possible order
# (i.e sorted in ascending order)

from itertools import permutations as perm

def solve(arr, n):
    indx = -1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            indx = i
            break
    
    if indx == -1:
        return sorted(arr)
    
    for j in range(n-1, indx, -1):
        if arr[j] > arr[indx]:
            arr[indx], arr[j] = arr[j], arr[indx]
            break
            
    return arr[:indx+1] + arr[n-1:indx:-1]

arr = [1,2,4,6,5]
print(solve(arr, len(arr)))


# Note: This does not work if there are repeating numbers in array
