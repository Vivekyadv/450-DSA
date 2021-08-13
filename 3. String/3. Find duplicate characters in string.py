# Write an efficient program to print all the duplicates and their counts 
# in the input string 

def solve(string):
    store = {}
    for char in string:
        if char in store:
            store[char] += 1
        else:
            store[char] = 1
    return store

string = 'This is String Count'
print(solve(string))