# deep copy
a = num1 = 10

# = -> assignment operator

a = 10
b = a

print("b=",b)

b = 1
print("a=",a)
print("b=",b)
print("a=",a)


list1 = [1, 2, 3]
list2 = list1  # list2 now aliases list1

print(f"list1: {list1}")
print(f"list2: {list2}")

list2[0] = 10  # Modifying list2 also modifies list1

print(f"list1 after modification: {list1}")
print(f"list2 after modification: {list2}")