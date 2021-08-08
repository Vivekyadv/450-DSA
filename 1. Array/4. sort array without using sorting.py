# given array which consists of 0's, 1's and 2's. Sort the array
# without using sorting algorithm

def solve(arr, n):
    count = [0, 0, 0]
    for i in range(n):
        count[arr[i]] += 1
    
    return [0]*count[0] + [1]*count[1] + [2]*count[2]

arr = [0, 2, 1, 2, 0]
print(solve(arr, len(arr)))

# Space and Time = O(n)
# We can optimize space complexity
# instead of return [0]*count0 + [1]*count1 + [2]*count2, we can 
# change the value of arr

def solve(arr, n):
    count = [0, 0, 0]
    for i in range(n):
        count[arr[i]] += 1
    
    i = 0
    while count[0] > 0:
        arr[i] = 0
        count[0] -= 1
        i += 1
    
    while count[1] > 0:
        arr[i] = 1
        count[1] -= 1
        i += 1
    
    while count[2] > 0:
        arr[i] = 2
        count[2] -= 1
        i += 1
        
    return arr


arr = [0, 2, 1, 2, 0]
print(solve(arr, len(arr)))

# Time complexity = O(n)
# Space complexity = O(1)



# Method 3: using 3 pointers
def solve(arr, n):
    i, j = 0, 0
    k = n-1

    while i <= j <= k:
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        if arr[j] == 1:
            j += 1
        if arr[j] == 2:
            arr[k], arr[j] = arr[j], arr[k]
            k -= 1
        
    return arr

arr = [0, 1, 2, 0, 1, 0, 2, 1, 2]
print(solve(arr, len(arr)))
