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



def nextGap(gap):
    if gap <= 1:
        return 0
    return gap//2 + gap%2
    
def merge(arr1, arr2, n, m): 
    gap = m + n
    gap = nextGap(gap)
    while gap > 0:
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i+gap]:
                arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
            i += 1
        
        j = gap - n if gap > m else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j+gap]:
                    arr2[j], arr2[j+gap] = arr2[j+gap], arr2[j]
                j += 1
        gap = nextGap(gap)

