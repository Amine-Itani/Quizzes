# Quiz 055
Slightly more compelx math. I didn't want to use the formula for the distance of two points because it is quite annoying but it seems like it is the only way to solve this question.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/05591f32-874a-4d76-8ee7-fe6b8a8e4c01)


<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class Darts():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_points(self):
        points = 0
        distance_to_center = ((self.y ** 2) + (self.x ** 2)) ** (1/2)
        if distance_to_center <= 1:
            points += 10
        elif distance_to_center <= 5:
            points += 5
        elif distance_to_center <= 10:
            points += 1

        return points

my_shot = Darts(0.5, 1)
test = my_shot.calculate_points()
print(test)
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/f2fb88c3-b704-4d9b-8f43-9e818398c5e7)

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/fbc55818-e325-405f-9490-276a0db1bf26)

<sub>Fig. 3 shows UML Diagram
