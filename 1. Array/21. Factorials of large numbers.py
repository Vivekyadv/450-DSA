# Given an integer N, find its factorial.
# Time = O(n^2)
# Space = O(1)

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return str(res)

print(factorial(7))



# Method 2: using array
def multiply(x, res, size):
	carry = 0 
	i = 0
	while i < size:
		prod = res[i] * x + carry
		res[i] = prod % 10
		carry = prod//10
		i += 1

	while carry:
		res[size] = carry % 10
		carry = carry // 10
		size += 1
		
	return size

def factorial(n) :
    res = [0]*5000
    res[0] = 1
    size = 1
    x = 2
    while x <= n :
        size = multiply(x, res, size)
        x += 1

    res = list(reversed(res[:size]))
    return res

result = factorial(7)
print(result)