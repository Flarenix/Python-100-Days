from math import sqrt

def isPrime(num):
    if num == 1: return False
    for i in range (2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
        else:
            continue
    return True

result = int(input("Pleas input a number: "))

print(isPrime(result))
    