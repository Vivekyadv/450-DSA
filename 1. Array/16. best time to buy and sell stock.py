# Given array prices where prices[i] is the price of a given stock on ith day
# you want to maximise your profit by choosing a single day to buy one stock and a 
# different day in future to sell that stock.

# Example: prics = [7,1,5,3,6,4]
# buy at 1 and sell at 6 -> profit = 6-1 = 5


# Method 1: Brute Force Method
def solve(arr, n):
    profit = 0
    for i in range(n):
        buyAt = arr[i]
        for j in range(i+1, n):
            sellAt = arr[j]
            if sellAt - buyAt > profit:
                profit = sellAt - buyAt

    return profit

arr = [7, 9, 5, 6, 3, 2]
print(solve(arr, len(arr)))



# Method 2: instead of taking difference of picked element with every other element, we 
# take the difference with the minimum element found so far
def solve(arr, n):
	profit = 0
	minSoFar = arr[0]
	
	for i in range(1, n):
		if arr[i] - minSoFar > profit:
			profit = arr[i] - minSoFar
	
		if arr[i] < minSoFar:
			minSoFar = arr[i]
	return profit
	
arr = [7, 9, 5, 6, 3, 2]
print(solve(arr, len(arr)))


# Method 3: similar to method 2, instead of minSoFar we take max from right
def solve(arr, n):
    profit = 0
    maxRight = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > maxRight:
            maxRight = arr[i]
        if maxRight - arr[i] > profit:
            profit = maxRight - arr[i]
    return profit

arr = [7, 9, 5, 6, 3, 2]
print(solve(arr, len(arr)))

