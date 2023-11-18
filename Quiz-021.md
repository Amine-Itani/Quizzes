# Quiz 021
This was our first quiz using data science and matlabplot. We used the equation and the randomly generated integers to plot the graph.
## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/2c4bea48-8baa-44d1-bf87-d2095eef63f8)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from matplotlib import pyplot as plt
import random

def produce(n, m, s):
    random.seed(1234)
    y = []
    x = []
    for i in range(n):
        x_rnd = random.randint(1,100)
        y_rnd = x_rnd**(-0.5*((m/s)**2))
        y.append(y_rnd)
        x.append(x_rnd)
    return x, y


y, x = produce(n=5, m=3, s=2)
print(y, x)
plt.plot(x, y)
plt.show()
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/6ef77983-b0eb-4016-8608-68968159c5b7)

<sub>Fig. 2 shows results of program

## Truth Table
### A(A ⊕ B)

| A B | A XOR B | A(A XOR B) |
|-----|---------|------------|
| 0 0 |    0    |      0     |
| 0 1 |    1    |      0     |
| 1 0 |    1    |      1     |
| 1 1 |    0    |      0     |

<sub>Fig. 3 shows truth table of equation
