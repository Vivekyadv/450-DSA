# Given two arrays, arr1 and arr2. check whether arr2 is subset of arr1

# Method 1
def isSubset(a, b):
    for x in b:
        if x not in a:
            return False
    return True


# Method 2: sorting and binary search
def isSubset(a, b, m, n):
    a.sort()
    for ele in b:
        if BS(a, 0, m-1, ele) == 0:
            return False
    return True

def BS(arr, l, r, key):
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return 0


# Method 3: using set
# we'll store elements of arr1 in set. then p = len(store)
# after that store elements of arr2 in that set, then check for length of set
# If length changes, arr2 is not subset of arr1
def isSubset(a, b, m, n):
    store = set(a)
    p = len(store)
    for ele in b:
        store.add(ele)

    return True if len(store) == p else False

