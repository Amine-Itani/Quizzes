# Quiz 052
Some more OOP practice, and even some math. I love compsci when it works with math. The more math the happier I am.

## Input & Output

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/a576539c-8cec-43ab-8c5f-a7be0d36d0e0)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class Bicycle():
    def __init__(self, wheel, frame_mat):
        self.wheel = wheel
        self.material = frame_mat

    def ride(self):
        print(f"{self.wheel.size} cm size and {self.material} frame")

class Wheel():
    def __init__(self, size):
        self.size = size
        self.p = 0
        self.kpr = 0

    def get_size(self):
        return self.size * 2.4

    def get_perimeter(self):
        self.p = 2 * 3.14 * self.size
        return self.p

    def get_kpr(self):
        self.kpr = self.p/100000
        return self.kpr

wheel_A = Wheel(26)
Bicycle_A = Bicycle(wheel_A, "aluminum")
size_A = Bicycle_A.wheel.get_size()
p_A = Bicycle_A.wheel.get_perimeter()
kpr_A = Bicycle_A.wheel.get_kpr()
print(kpr_A)
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/4594e7e3-fde2-4ae8-adf2-12268e5e03c1)

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/0e6d4152-162f-44f6-80fc-c14a0e07de67)

<sub>Fig. 3 shows UML Diagram
