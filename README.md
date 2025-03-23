# Fundamentals

* high-level -> machine 
* machine 0,1 

## assembly
``` 
    LOAD
    ADD 
```

1. Imperative Programming -> How to do -> sequencially 
   programmer -> coding -> HLPL -> How to do

2. Declarative Programming -> What to do [Functional Programming || OOP]

3. Python code(HL) -> Machine (LL)

```
Compile
HL -> LL(bytecode)

Interpret
HL -> LL(bytecode produce but store internally)
Run time -> bytecode line by line interpret

Compile time -> HL -> LL 
Run time
```

#### static type language -> type define

#### dynamic type language -> type fluid

##### type inferencing 
``` name = 1;
name -> int type
name = "Htun"
name -> string type
```

# Basic Coding and How to approach

1. output CLI -> Command Line Interface
2. GUI -> Graphical User Interface
3. UI / UX

```
Win + R -> cmd
```

* **desire -> output**
* **what?, how?, why?**

### syntax -> အရေးအသား

### semantic -> အနက်

### pragmatic -> လက်တွေ့အနက်အဓိပ္ပာယ်

#### Print Function

```
print(data,sep=' ',end='\n')
```

#### Cpython

```
python -m dis file.py
```

##### string

* char -> single ch -> H, A, 1, 2 -> ' '(single quote)
* string -> a bunch of chs -> HtunAungKyaw -> " "(double quote)

```
print('Hello') 
print("1") # string
print(1) # number
```
### Homework

```
`` , | , & , % -> what are they called?
```

```
`` - back tick
| - pipe
& - amphasand
% - percentage / modulus
```
#### print()

```
print(number) -> ''/"" no need
print('string',"string")
print("output", sep=" ", end="\n")
```

#### Scope

local - block access
[if, for, while, function] - static type PL
python -> function scope
```
if(name == "Htun Aung")
{
    int age = 26;
    print("Welcome Htun Aung");
}
print(age) # error: cannot access 
```
global - universal access

python creates scope using indentation

##### Variable - container

local scope -> local variable
global scope -> global variable
constant -> naming UPPERCASE

##### LEGB
L - local
E - enclose
G - global
B - built-in

##### Memory overwrite
```
name = "HA"
name = "HAK"
```
###### CPU -> RAM -> Harddisk
-------------------------
###### Homework
* March 20, 2025
```
1. print(f'name: %s\nage: %d\naddress: %s',name,age,address)
2. LEGB
```

-------------------------
##### Looping

* for var in iteratable items/function

```
for i in range(start, stop, step):
    print(i)
```

* while condition:

```
i = 0
while i<=10:
    print(i)
```

* iteratable items -> list(array) -> [2,3,4,5,6]
* iteratable function -> range()

* condition
0 and 1 -> true and false

true -> code
false -> code

logical operation
switch
binary system
octa system
hexa system
decimal system 0->9

```
if condition:
    //code
elif condition:
    //code
else:
    //code
```

------------------

##### List (Array) 

var1 = 1
var2 = 2
var3 = 3
var4 = 4

num = [1,2,3,4] -> data
      [0,1,2,3] -> index
      [-4,-3,-2,-1] -> negative index

index -> value
room no. -> data

num[0] -> 1
num[1] -> 2
num[3] -> 4

---------------
##### Tracing
bug -> error

1. Theory
2. Coding Experience

code -> how does it work?
-------------------------
## Operator
operand
operator
operation

Arithmetic Operations
1 + 2 - (3 + 4)

1+2 = 3 +3 = 6 + 4 -> 10

3 + 4 

```2**3**2```

Relational Operations

< > <= >=

Equality Operations

== != <>

logical Operations

and or not

binary operation

precedence - priority
associativity 
-------------------------
###### Homework
* March 22, 2025
```
1. argument vs parameter
2. for vs while
3. print(1 + 2 - (3 + 4))
```
------------------------

### Type Casting - Type Change

input() -> string

int()

float()

--------------------
### Exception Handling

default -> error -> auto terminate

error handle -> continue the program

```
try:
    \\ error ဖြစ်စေနိုင်တဲ့ code
except:
    \\ error message
``` 

