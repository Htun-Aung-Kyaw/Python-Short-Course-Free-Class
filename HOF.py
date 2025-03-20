import dis;

def isEven(x):
    return x % 2 == 0

# print("2 is even",isEven(2))

# def isOdd(x):
#     return not(isEven(x))

# print("3 is odd", isOdd(3))

dis.dis(isEven)