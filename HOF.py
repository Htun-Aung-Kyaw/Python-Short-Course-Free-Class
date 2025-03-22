import dis;

def isEven(x):
    return x % 2 == 0

# print("2 is even",isEven(2))

# def isOdd(x):
#     return not(isEven(x))

# print("3 is odd", isOdd(3))

dis.dis(isEven)

# function as a parameter
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

result = apply_function(square, 5)  # Pass the `square` function
print(result)  # Output: 25

# function as a return value
def multiplier(factor):
    def multiply_by_factor(x):
        return x * factor
    return multiply_by_factor

double = multiplier(2)  # Returns a function that doubles a number
print(double(5))  # Output: 10