# Given an array of +ve integers and a number k. Find the min no of swaps required 
# to bring all the numbers <= k together.

# Example:
# arr = [2,7,9,5,8,10,4] , k = 6   =>    min swaps = 2
# we can swap (7,5) and (9,4)   or swap (2,9) and (8,4)   or swap (2,8) and (5,10)


# Algorithm
# count no of integers which are <= k
# take sliding window of this length (count) -> i.e arr[i:i+count]
# then traverse the array with this sliding window and check no of elements which are > k
# we have to swap these elements, search the window in which no of elements > k is minimum

# Method 1: Brute force approach
def solve(arr, n, k):
    count = sum(1 for x in arr if x <= k)
    minSwap = 2**32
    for i in range(n - count + 1):
        countMaxEle = 0
        for i in range(i, i + count):
            if arr[i] > k:
                countMaxEle += 1
        minSwap = min(minSwap, countMaxEle)

    return minSwap

arr = [2, 7, 3, 5, 8, 10, 4]
k = 6
print(solve(arr, len(arr), k))


# Method 2: sliding window approach
def solve(arr, n, k):
    count = sum(1 for x in arr if x <= k)
    countMax = 0
    for i in range(count):
        if arr[i] > k:
            countMax += 1

    minSwap = countMax
    i = 0
    j = count
    while j < n:
        if arr[i] > k:
            countMax -= 1
        if arr[j] > k:
            countMax += 1
        minSwap = min(minSwap, countMax)
        i += 1
        j += 1
    
    return minSwap

print(solve(arr, len(arr), k))
