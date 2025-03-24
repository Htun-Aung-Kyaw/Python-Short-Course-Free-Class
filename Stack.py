arr = []
def push(item):
    global arr
    # arr = arr + [item] # list concat with + syntax
    arr = [*arr, item] # unpacking with * syntax

def pop():
    global arr
    pop = arr[-1]
    arr = arr[:-1]
    return pop

arr = [1,2,3,5,6,7,9]
push(19)
print("push 19 ",arr)
push(0)
print("push 0 ",arr)
push(10)
print("push 10 ",arr)

# pop, arr = pop(arr)
print("pop ", pop())
print("after pop ", arr)

push(20)
print("push 20 ",arr)