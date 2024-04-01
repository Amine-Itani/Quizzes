# Quiz 054
OOP pling plang plong. More practice!

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/91e7d09f-df8a-4219-ae92-70833467b43b)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class rainDrops():
    def __init__(self):
        self.string = ''
        self.empty_check = False

    def pour(self, n:int):
        if n % 3 == 0:
            self.string += "Pling"
        if n % 5 == 0:
            self.string += "Plang"
        if n % 7 == 0:
            self.string += "Plong"
        if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
            self.empty_check = True

        if self.empty_check == True:
            return f"{n}"
        else:
            return self.string

rainy_day = rainDrops()
test = rainy_day.pour(30)
print(test)
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/b1289798-292d-42a5-82ac-8a5ae341ea30)

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/8efe642f-ab75-4b4b-bc52-cde02129d83a)

<sub>Fig. 3 shows UML Diagram
