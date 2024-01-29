# Quiz 038

## Input & Output

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/d8bfb9f2-1561-475d-99a5-51a28c800fd6)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
import random
from matplotlib import pyplot as plt
class SalemanMap:
    def __init__(self):
        self.x = []
        self.y = []
        self.names = []

    def set_names(self, list_names:list):
        self.names = list_names
        for i in range(len(self.names)):
            self.x.append(random.randint(0,100))
            self.y.append(random.randint(0,100))

    def get_map(self):
        plt.scatter(self.x, self.y)
        for i in range(len(self.names)):
            plt.text(self.x[i], self.y[i], self.names[i])
        plt.xlabel("Distance (km)", fontsize=18)
        plt.ylabel("Distance (km)", fontsize=18)
        plt.show()

c = SalemanMap()
c.set_names(['Sapporo', 'Fukuoka', 'Osaka', 'Kyoto', 'Kawasaki', 'Nagoya', 'Kobe', 'Kusatsu', 'Takadanobaba'])
c.get_map()
```

## Evidence

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/f2b944e6-bde9-4796-8a8b-26a34e07e4f5)

<sub>Fig. 2 shows results of program

## UML Diagram

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/619c82d3-046d-4cc6-a59b-92f2c127e7ac)

<sub>Fig. 3 shows UML Diagram
