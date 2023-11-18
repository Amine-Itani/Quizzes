# Quiz 017
In this quiz, we learned how to use dictionaries to pair keys and values and call on them in a for loop. This replaces much more teadious if statements that would take a lot more time to write.
## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/ac81c00c-7187-49f3-866f-20adb516f54f)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def get_l3tt3r(msg:str):
    rules = {'a': 4, 'e': 3, 'i': 1, 'o': 0, ' ': '_'}
    new_msg = ""
    for x in msg:
        if x in rules:
            new_msg += str(rules[x])
        else:
            new_msg += x
    return new_msg

case1 = get_l3tt3r("Hello World")
print(case1)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/ec5e45c2-ab70-4fbf-98c6-48a222f75052)

<sub>Fig. 2 shows results of program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/064a8cae-d2e8-4db2-908f-f8c6438e73be)

<sub>Fig. 3 shows flowchart of program
