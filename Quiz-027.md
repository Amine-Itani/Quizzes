# Quiz 027
Nice quiz, pretty fun to do overall. 

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/4b4251b0-42a0-4342-bd30-999af5ead03f)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def count_letters(my_dict, msg):

    for l in msg: # simple yet powerful, as repeats nested loop for every loop
        if l in my_dict:
            my_dict[l] += 1

    return my_dict

case1 = count_letters(my_dict={'w':0,'l':0, 'c': 0}, msg= "hello world")
print(case1)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/0012043f-ecac-41e3-9858-412018523ad9)

<sub>Fig. 2 shows results of program

### How many color could you represent in a 6 bit computer?

262000
