# Given an array of intervals, merge all overlapping intervals and return an array of 
# merged intervals

# Method: sort the array and then compare ending of interval to starting of next interval
def solve(intervals, n):
    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, n):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solve(intervals, len(intervals)))

