# Given array and a given value, find if there exist a triplet whose sum == value


# Method 1: Brute Force
def solve(arr, n, val):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == val:
                    return True
    return False


# Method 2: using hashmap
def solve(arr, n, val):
    for i in range(n):
        store = set()
        for j in range(i+1, n):
            comp = val - (arr[i] + arr[j])
            if comp in store:
                return True
            store.add(arr[j])
    return False


# Method 3: sorting and two pointer approach
# sort the array, fix first number and use two pointer approach on other two numbers
# fix at i, j starts from i+1  and k starts from n-1 (end of array)
def solve(arr, n, val):
    arr.sort()
    for i in range(n):
        j = i + 1
        k = n -1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total == val:
                return True
            elif total < val:
                j += 1
            else:
                k -= 1
    return False
