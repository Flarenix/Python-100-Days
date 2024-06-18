from math import sqrt

def isPrime(num):
    if num == 1: return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
        else:
            continue
    return True

for i in range(100):
    if(isPrime(i)): print(i)
    
for i in range(100):
    if(isPrime(i)): print(i)


print({0},"nmihao1")