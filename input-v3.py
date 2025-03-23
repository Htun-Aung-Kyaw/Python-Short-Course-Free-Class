num1 = None
num2 = None

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except:
        print("Wrong input: Please enter a number")
    
    if type(num1) == int and type(num2) == int:
        break

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2

print("Addition: ", add)
# num3 = int(input(("Another number:")))
# add = add + num3
# sub = sub - num3
# add += num3
# sub -= num3
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", int(div))
print("Modulus: ", mod)