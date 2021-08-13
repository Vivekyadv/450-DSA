# Given two strings, check whether str2 is rotation of str1
# Example: ABCD and CDAB are rotation of each other
# ABCD and ACBD are not

def solve(str1, str2):
    if len(str1) != len(str2):
        return 0
    temp = str1 + str1
    return 1 if str2 in temp else 0

str1 = 'abcd'
str2 = 'acbd'
str3 = 'cdab'
print(solve(str1, str2))
print(solve(str1, str3))

