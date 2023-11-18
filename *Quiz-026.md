# Quiz 026
Describe this quiz
## Input & Output

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
# Create a graph using a dictionary
from matplotlib import pyplot as plt

data = {
    'x' : [],
    'y' : [24, 1, 2, 25, 26, 21, 23, 34, 49, 2, 19, 32, 7, 17, 36, 7, 45, 28, 40, 46]
}
t = 0
for x in range(len(data['y'])):
    data['x'].append(t)
    t += 1

data['title'] = 'quiz_data_science'

plt.plot(data['x'], data['y'], 'r', linewidth=2)
plt.title(data['title'])
plt.xlabel("x", fontsize=18)
plt.ylabel("y", fontsize=18)
plt.show()
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/85053875-2f92-44ca-a33a-2ba766bb0718)

<sub>Fig. 2 shows results of program

## Base Conversion
### Red = 10, Blue = 255, Green = 255

0AFFFF
<sub>Fig. 3 shows truth table of equation
