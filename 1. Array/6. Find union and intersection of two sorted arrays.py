# Given two sorted arrays, find union and intersection of these array


# Method 1: using set() function
def solve(a, b):
    set1 = set(a)
    set2 = set(b)
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    print(list(union))
    print(list(intersection))
    print()

a = [9, 5, 9, 12, 2, 4]
b = [1, 2, 9, 5, 9, 6]
solve(a, b)
   

# Method 2: Brute Force
# we use list in below solution, we can use set() to reduce Time complexity
def solve(a, b):
    union = []
    for ele in a:
        if ele not in union:
            union.append(ele)
    for ele in b:
        if ele not in union:
            union.append(ele)
    print(union)

    intersection = []
    for ele in a:
        if ele in b and ele not in intersection:
            intersection.append(ele)
    print(intersection)
    print()

solve(a, b)


# Method 3: for sorted arrays
def solve(a, b, m, n):
    i = j = 0
    intersection, union = set(), set()
    while i < m and j < n:
        if a[i] < b[j]:
            union.add(a[i])
            i += 1
        elif a[i] > b[j]:
            union.add(b[j])
            j += 1
        else:
            intersection.add(a[i])
            union.add(a[i])
            i += 1
            j += 1
    
    while i < m:
        union.add(a[i])
        i += 1
    
    while j < n:
        union.add(b[j])
        j += 1

    print(union)
    print(intersection)

a.sort()
b.sort()
solve(a, b, len(a), len(b))

