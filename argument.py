def area(length=1, width=2):
    return length*width


print("Area1", area())
print("Area2", area(10))
print("Area3", area(10, 3))


def printNames(*names):
    for n in names:
        print(n)

printNames("Tony", "Rogers", "Banner", "Thor", "Natasha")
# names = ["Tony", "Rogers", "Banner", "Thor", "Natasha"]