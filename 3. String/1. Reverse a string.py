# Given string in the form of array, reverse it

# Method 1: slicing
def solve(string):
    return ''.join(string[::-1])

# this is string
string = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 's', 't', 'r', 'i', 'n', 'g']
print(solve(string))

# Method 2: swapping elements
def solve(string):
    n = len(string)
    i = 0
    j = n-1
    while i <= j:
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
    return ''.join(string)

print(solve(string)) 
