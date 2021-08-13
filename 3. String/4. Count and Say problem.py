# Given a number n, return the nth pattern 
# pattern is defined as 
# N = 4
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


def countAndSay(n):
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    
    result = '11'
    for i in range(3, n+1):
        temp = ''
        count = 1
        result += '@'
        for j in range(len(result)-1):
            if result[j] == result[j+1]:
                count += 1
            else:
                temp += str(count) + result[j]
                count = 1
        result = temp
    return result

print(countAndSay(6))