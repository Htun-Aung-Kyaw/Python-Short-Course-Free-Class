def add(a, b):
    print("The result is: ", (a+b)) #definition

a = input("Enter a number: ")
num1 = int(a)

b = input("Enter a number: ")
num2 = int(b)

add(num1, num2) #function invoking or calling or invokation

def sub(a=1, b=2):
    return a-b

subtraction = sub(num1,num2)
print("Subtraction:",subtraction)

print("Subtraction:",sub(2,9))



