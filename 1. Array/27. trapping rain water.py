# Given an array which represents the heights of blocks. If width of each block is 1,
# compute how much water can be trapped between the blocks during rainy season
# Example:
# arr = [3,0,0,2,0,4]   water trapped = 10 units

# Algorithm
# 1. find highest block on left and on right
# 2. take smaller of two heights
# 3. the difference between smaller height and height of current block is the amount of
#    water can be stored by that building
def trappingWater(arr, n):
    leftMax = [0]*n
    rightMax = [0]*n
    
    leftMax[0] = arr[0]    
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], arr[i])

    rightMax[-1] = arr[-1]
    for j in range(n-2, -1, -1):
        rightMax[j] = max(rightMax[j+1], arr[j])
    
    water = 0
    for i in range(n):
        height = min(leftMax[i], rightMax[i])
        water += height - arr[i]
    return water

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingWater(arr, len(arr)))


# Approach 2: instead of maintaing two arrays, maintain two variables to store the 
# max till that point
def solve(arr, n):
    leftMax = rightMax = 0
    low, high = 0, n-1
    water = 0

    while low <= high:
        if arr[low] < arr[high]:
            if arr[low] > leftMax:
                leftMax = arr[low]
            else:
                water += leftMax - arr[low]
            low += 1
        else:
            if arr[high] > rightMax:
                rightMax = arr[high]
            else:
                water += rightMax - arr[high]
            high -= 1
    
    return water

print(solve(arr, len(arr)))
