# Given an array of integers, find the inversion count in the array.
# Inversion count is how far or close the array is from being sorted. 
# If array sorted -> inversion count = 0
# If sorted in reverse order -> inversion count = maximum

# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.


# Method 1: Brute force method
def solve(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j] and i < j:
                count += 1
    return count

arr = [8,4,2,1]
arr = [1,20,6,7,5,8,11,3]
print(solve(arr, len(arr)))


# Method 2: using enhanced Merge sort


def mergeSort(arr, temp, l, r):
	Inv_Count = 0
	if l < r:
		mid = (l + r)//2

		Inv_Count += mergeSort(arr, temp, l, mid)
		Inv_Count += mergeSort(arr, temp, mid + 1, r)

		Inv_Count += merge(arr, temp, l, mid, r)
	return Inv_Count


def merge(arr, temp, l, mid, r):
	i = l	
	j = mid + 1 
	k = l	 
	Inv_Count = 0

	while i <= mid and j <= r:
		if arr[i] <= arr[j]:
			temp[k] = arr[i]
			k += 1
			i += 1
		else:
			temp[k] = arr[j]
			Inv_Count += (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp[k] = arr[i]
		k += 1
		i += 1

	while j <= r:
		temp[k] = arr[j]
		k += 1
		j += 1

	for x in range(l, r + 1):
		arr[x] = temp[x]
		
	return Inv_Count


arr = [1,20,6,7,5,8,11,3]
n = len(arr)
temp = [0]*n
print(mergeSort(arr, temp, 0, n-1))

