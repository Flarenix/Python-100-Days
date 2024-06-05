def getGCD(a, b):
    return b if (a % b == 0) else getGCD(b, a%b)

def getLCM(a, b):
    return a * b // getGCD(a, b)

a = int(input("input a: "))
b = int(input("input b: "))
print(getGCD(a, b))
print(getLCM(a, b))