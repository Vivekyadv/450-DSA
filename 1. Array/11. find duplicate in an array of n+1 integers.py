# Given an array of integers containing n+1 integers where each integers is in range
# [1, n]. There is only one repeated number in array, return this number
# Solve without modifying array and use O(1) space


# Method 1: sort array and check adjacent elements
def solve(arr, n):
    arr.sort()
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return arr[i]
    return -1

# Time = n*log(n)
# Space = O(1) to O(n)  (sort() take O(n) in worst case)


# Method 2: using map
def solve(arr, n):
    store = set()
    for num in arr:
        if num in store:
            return num
        store.add(num)
    return -1

# Time and Space = O(n)


# Method 3: using -ve marking
def solve(arr, n):
    for num in arr:
        indx = abs(num)
        if arr[indx] < 0:
            duplicate = indx
            break
        arr[indx] *= -1
    
    # Restore numbers
    for i in range(n):
        arr[i] = abs(arr[i])
    return duplicate



# Method 4: using binary search
def findDuplicate(arr):
    low = 1
    high = len(arr) - 1
    
    while low <= high:
        cur = (low + high) // 2
        count = 0

        count = sum(num <= cur for num in arr)
        if count > cur:
            duplicate = cur
            high = cur - 1
        else:
            low = cur + 1
            
    return duplicate

arr = [4,3,4,5,2,4,1]
print(findDuplicate(arr))

# Time = n*log(n)
# Space = O(1)

