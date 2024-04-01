![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/d3ecbdd7-f2c4-4934-9f8d-c0fb193e7258)# Quiz 053
Palindromes! And OOP!

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/cc6778f5-44c2-46c3-b1c1-9ec21a0c382b)


<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class palNum():
    def __init__(self, A:int, B:int):
        self.pal_list = []
        self.A = A
        self.B = B

    def get_pal_list(self):
        for x in range(self.A, self.B):
            string = str(x)
            reverse_string = ''
            for l in range(len(string)-1, -1, -1):
                reverse_string += string[l]

            if reverse_string == string:
                self.pal_list.append(string)
                print(string)

        return self.pal_list
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/72f66a7b-f9b1-4590-8f59-e5b4f81e9eac)

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/aa310403-77bd-41ce-be62-15a7c0946752)

<sub>Fig. 3 shows UML Diagram
