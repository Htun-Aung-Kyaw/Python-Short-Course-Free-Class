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