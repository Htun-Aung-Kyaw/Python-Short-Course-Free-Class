x = 10


def num():
    x = 20
    x += 1
    print(x)


def num1():
    global x
    x += 2
    print(x)


def add():
    global x
    x += 5
    print(x)

add()#15
num1()#
print(x)#
num()#







