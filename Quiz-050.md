# Quiz 050
Making a little object system for flights. I am realizing that as our skills progress we slowly but surely approach solving real world problems.                 

## Input & Output


<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class Flight:
    def __init__(self, flight_number, origin, destination, departure, duration):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.duration = duration

    def get_duration(self):
        self.text = f"{self.duration[0]} hours, {self.duration[1]} minutes, {self.duration[2]} seconds"
        return self.text

flight_A = Flight("AA123", "New York", "Los Angeles", "10:00AM", [5, 30, 3])
flight_B = Flight("BA468", "Beirut", "Paris", "2:45PM", [4,0,0])
test1 = flight_A.get_duration()
print(test1)
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/2da9971b-a83a-42f7-b74b-e2c6ce3a3577)

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/ee5dc96e-3883-49c4-94f7-c37af63e69d7)

<sub>Fig. 3 shows UML Diagram
