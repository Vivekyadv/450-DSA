# Given an array of +ve and -ve numbers, arrange them in alternating +ve and -ve numbers
# in constant space

# Example: arr = [1, 2, 3, -4, -1, 4]
# after rearrangement -> arr = [-4, 1, -1, 2, 3, 4]

# Method 1: using O(n) extra space and two pointer method
def solve(arr):
    positive = [x for x in arr if x >= 0]
    negative = [x for x in arr if x < 0]

    i = j = k = 0
    while i < len(positive) and j < len(negative) and k < len(arr):
        arr[k] = negative[j]
        k += 1
        j += 1
        arr[k] = positive[i]
        k += 1
        i += 1
    
    while i < len(positive) and k < len(arr):
        arr[k] = positive[i]
        i += 1
        k += 1
    while j < len(negative) and k < len(arr):
        arr[k] = negative[j]
        j += 1
        k += 1

    return arr

arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(solve(arr))



# Method 2: sort the array, count no of positive and negative integers. 
# Then we'll swap one negative and one positive
def solve(arr, n):
	arr.sort()

	i, j = 1, 1
	while j < n:
		if arr[j] > 0:
			break
		j += 1

	while arr[i] < 0 and j < n:
		arr[i], arr[j] = arr[j], arr[i]
		i += 2	
		j += 1
	
	return(arr)

arr = [-5, -2, 5, 2, 4, 7, 1, 8, -1, -8]
print(solve(arr, len(arr)))
