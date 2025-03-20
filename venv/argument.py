def area(length=1, width=2):
    return length*width


print("Area1", area())
print("Area2", area(10))
print("Area3", area(10, 3))


def names(*name):
    for n in name:
        print(n)
    print(name[0])


names(1, 2, 3)