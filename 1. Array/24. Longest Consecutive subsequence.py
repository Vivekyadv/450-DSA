# Given array, find length of longest consecutives present in array. The consecutive
# numbers can be in any order.

# Arr = [3,9,1,10,4,12,5,11,6,7]
# consecutives are -> [3,4,5,6,7]   and [9,10,11,12]
# longest = 5


# Method 1
# sort the unique numbers of array, then from end check consecutives numbers
def solve(arr):
    arr = list(sorted(set(arr)))
    n = len(arr)
    result = 0

    i = n-1
    while i >= 0:
        val = arr[i]
        j = i
        count = 0
        while j >= 0 and arr[j] == val:
            count += 1
            j -= 1
            val -= 1
        i = j
        result = max(result, count)

    return result

arr = [0,1,1,2,5,6,6,5]
print(solve(arr))


# Method 2: Brute force
# for every number in array, check for consecutiveness of that number in array
# we'll count if the next value is present or not using while loop
def solve(arr):
    result = 0
    for num in arr:
        val = num
        count = 1
        while val + 1 in arr:
            count += 1
            val += 1
        result = max(result, count)

    return result

arr = [0,1,1,2,4,7,5,6,6,5]
print(solve(arr))


# Method 3: optimisation of Method 2
# take numbers from array only once (i.e set(arr)) 
# Now for every num in array, if num - 1 not in array then check for consecutive 
# just like we did in Brute Force method

# Note: we only check for consecutiveness if num - 1 is not in array, since array is 
# not sorted so we have to check if num - 1 is present in array or not
def solve(arr):
    result = 0
    num_set = set(arr)

    for num in num_set:
        if num - 1 not in num_set:
            val = num
            count = 1
            while val + 1 in num_set:
                val += 1
                count += 1
            result = max(result, count)

    return result

arr = [0,1,1,2,4,7,5,6,6,5]
print(solve(arr))
