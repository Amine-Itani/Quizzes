# Quiz 035
The quiz's program is relatively simple, but the teasting is where the real work is. The green tick from all tests passed is quite satisfying.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/1b9ee8a3-9d9b-42a3-a4eb-4054332a93d6)

<sub>Fig. 1 shows task and code functionality
## Code

```py
def mystery(list1, list2):

    output = []

    for x in list1:
        for y in list2:
            if x == y:
                output.append(x)

    return output
```

## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/83b8e666-b35c-42f1-93d6-488b9b4eb88d)

<sub>Fig. 2 shows results of program
