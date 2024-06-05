def genFib(num):
    a1 = 1
    a2 = 1
    for _ in range(num):
        sum = a1 + a2
        print(sum)
        a1 = a2
        a2 = sum
        
genFib(5)
