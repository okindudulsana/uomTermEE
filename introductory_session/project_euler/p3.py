#problem 3

def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


for i in range(int(600851475143**0.5+1),1,-1):
    if 600851475143 % i == 0:
        if isprime(i) == True:
            print(i)
            break