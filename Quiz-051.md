# Quiz 051
Inheritance practice in OOP and the like. We slowly approach G11 exams (start studying Amine!)

## Input & Output

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/75f8ea39-97ce-401a-af55-2151d654b2d8)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class Aircraft:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def get_info(self):
        self.info = f"{self.model} (Capacity: 150)"
        return self.info

class Flight(Aircraft):
    def __init__(self, model, capacity, flight_number, origin, destination, departure, duration):
        super().__init__(model, capacity)
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.duration = duration
        self.text = ''


    def get_duration(self):
        self.text = f"{self.duration[0]} hours, {self.duration[1]} minutes, {self.duration[2]} seconds"
        return self.text

    def print_object_info(self):
        self.flight_info = super().get_info()
        self.f_info = f"Flight {self.flight_number} from {self.departure} to {self.destination}. Aircraft: {self.info}"
        return self.f_info


aircraft_A = Aircraft("Airbus 123", "200")
flight_A = Flight("Airbus 123", "200",  "AA123", "New York", "Los Angeles", "10:00AM", [5, 30, 3])
test2 = flight_A.print_object_info()
print(test2)
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/28996856-a410-4212-92e2-f1a646dc62fd)

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/f3b41046-96f0-4509-94a2-81f3db8d69a0)

<sub>Fig. 3 shows UML Diagram
