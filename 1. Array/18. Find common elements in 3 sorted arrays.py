# Given three arrays sorted in increasing order. Find the elements that are 
# common in all three arrays.

# Approach:
# Find common element in first two arrays, store these common element in temp variable
# then find common element in temp and third arrays, store in result


# Method 1: Brute Force approach
# To find common element, we use nested loop
def solve(a, b, c):
    temp = []
    for ele in a:
        if ele in b and ele not in temp:
            temp.append(ele)
    
    result = []
    for ele in temp:
        if ele in c:
            result.append(ele)
    return sorted(result)

a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]
print(solve(a,b,c))


# Method 2: using two pointer approach
def solve(a, b, c):
    i = j = 0
    temp = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            temp.append(a[i])
            i += 1
            j += 1
    
    ij = k = 0
    result = []
    while ij < len(temp) and k < len(c):
        if temp[ij] < c[k]:
            ij += 1
        elif temp[ij] > c[k]:
            k += 1
        else:
            if temp[ij] not in result:
                result.append(temp[ij])
            ij += 1
            k += 1
    
    return result

print(solve(a,b,c))



# We can improve method 2:
# instead of using two loops we can check for condition in single loop
def solve(a,b,c):
    i = j = k = 0
    result = []
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and b[j] == c[k]:
            if a[i] not in result:
                result.append(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1
    return result

print(solve(a,b,c))
