# Given two sorted arrays, merge them and return sorted array without using extra space


def solve(a, b):
    for i in range(len(a)):
        if a[i] > b[0]:
            a[i], b[0] = b[0], a[i]
            b.sort()
    return a, b

a = [1,4,7,8,10]
b = [2,3,9] 
print(solve(a,b))


# extend 1st array with 2nd array and compare from the end
def merge(arr1, arr2, m, n): 
    i = m-1
    j = n-1
    arr1.extend(arr2)
    k = len(arr1)-1
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
            k -= 1
        elif arr1[i] < arr2[j]:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1
        
    while i >= 0:
        arr1[k] = arr1[i]
        i -= 1
        k -= 1
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    
    return arr1



# Method: All elements in Arr 1 must be smaller than all elements in Arr2
# Algorithm
# 1. Take two pointers -> i = m-1 and j = 0
# 2. if a[i] > b[j] -> swap(a[i], b[j]) and i -= 1, j += 1
# 3. if not, that means all elements in a is smaller than all elements in b. 
#    So break the loop
# 4. Now arrays might be unsorted so sort them

def merge(a, b, m, n): 
    i = m-1
    j = 0
    while i >= 0 and j < n:
        if a[i] >= b[j]:
            a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1
        else:
            break
    a.sort()
    b.sort()
    return a, b


a = [5, 8, 10, 12, 13, 15]
b = [2,6,7,9,11]
print(merge(a, b, len(a), len(b)))
