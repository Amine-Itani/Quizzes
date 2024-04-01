# Quiz 056
Do you remember unit 2? Exams coming up soon, so be ready.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/440f5fec-599d-4c3b-ac8a-dd5f7522c1bf)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class Converter():
    def __init__(self, num):
        self.num = num

    def convert_to_binary(self):
        t = self.num
        b = ''
        while t > 1:
            b += str(t % 2)
            t = t // 2
        b += str(t)
        return b

my_number = Converter(9)
test = my_number.convert_to_binary()
print(test)
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/40ec8b67-5131-4048-8819-815d5c35c060)

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/83ad483b-a81c-4a3b-aa07-d818cbcb960f)

<sub>Fig. 3 shows UML Diagram
