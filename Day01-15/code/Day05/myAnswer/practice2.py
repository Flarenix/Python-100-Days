from math import sqrt

def isPrime(num):
    if num == 1: return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
        else:
            continue
    return True

def isPerfect(num):
    sum = 1
    if isPrime(num): return
    else:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                sum += i
                if i > 1 and num // i != i:
                    sum += num // i
    if sum == num: 
        print(num)
    else:
        return

for num in range(10000):
    isPerfect(num)
            