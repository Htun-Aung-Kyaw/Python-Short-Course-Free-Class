name = "HA"
age = 26
address = "YGN"

math_mark = 70

def greet():
    global name
    name = "Someone"
    print(f'name: %s\nage: %d\naddress: %s' % (name,age,address))

print("Global varibles:",name, age)
greet()
print("Global varibles:",name, age)
# print("local variable address", address)


