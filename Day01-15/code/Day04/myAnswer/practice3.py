import math

def plotTriangle(row):
    for i in range(row):
        for _ in range(i+1):
            print("*", end = '')
        print()
    
    for i in range(row):
        for j in range(row):
            if j <= row - i - 2:
                print(" ", end = '')
            else:
                print("*", end = '')
        print()
    
    mid = math.ceil(row / 2)
    for i in range(row):
        for _ in range(row - i - 1):
            print(" ", end = '')
        for _ in range(2 * i + 1):
            print("*", end ='')
        print()

plotTriangle(5)
            