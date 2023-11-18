# Quiz 027

## Input & Output

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def count_letters(my_dict, msg):

    for l in msg:
        if l in my_dict:
            my_dict[l] += 1

    return my_dict

case1 = count_letters(my_dict={'w':0,'l':0, 'c': 0}, msg= "hello world")
print(case1)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/0012043f-ecac-41e3-9858-412018523ad9)

<sub>Fig. 2 shows results of program

## Truth Table

<sub>Fig. 3 shows truth table of equation

## Circuit

<sub>Fig. 4 shows circuit of equation
