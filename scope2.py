# import math

# PI = 3.142
# PI = 3.1459
# print("Constant PI",PI)
# print("Math.pi",math.pi)
# math.pi = 3.142
# print("Modified math.pi",math.pi)

num = 8
for i in range(8):
    print("i in for scope->local scope",i)

# print("accessing i from global scope",i) -> Ctrl + /

print("number in global scope", num)

j = 0
if num == 8:
    print("Number is eight.")
    j = 10
    print("j", j)

print("Accessing j from global scope",j)