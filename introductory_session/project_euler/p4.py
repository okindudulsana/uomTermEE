#problem 04
def ispalindrome(n):
    return str(n) == str(n)[::-1]
max_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if ispalindrome(product) and product > max_palindrome:
            max_palindrome = product
print(max_palindrome)

