# Given two arrays, find the median of array after merging them 


# Method 1: sort the array such that first half sorted elements are in arr1 and last half 
# sorted elements are in arr2
# Then the median is ==> (arr1[-1] + arr2[0])//2

def solve(a, b, n):
    i = n-1
    j = 0
    while a[i] > b[j] and i >= 0 and j < n:
        a[i], b[j] = b[j], a[i]
        i -= 1
        j += 1
    
    a.sort()
    b.sort()
    median = (a[-1] + b[0])//2
    
    return median

a = [1,12,15,26,38]
b = [2,13,17,30,45]
print(solve(a, b, len(a)))


# Optimise: instead of sorting, we can take (max(a) + min(b)) // 2
def solve(a, b, n):
    i = n-1
    j = 0
    while a[i] > b[j] and i >= 0 and j < n:
        a[i], b[j] = b[j], a[i]
        i -= 1
        j += 1
    median = (max(a) + min(b))//2
    return median

a = [1,12,15,26,38]
b = [2,13,17,30,45]
print(solve(a, b, len(a)))

