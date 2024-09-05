# Quiz 032

## Input & Output

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from matplotlib.gridspec import GridSpec
from lib_api_quizzes import get_sensors
from matplotlib import pyplot as plt

sensor4 = get_sensors(ids=[4])[4]
sensor5 = get_sensors(ids=[5])[5]
subtraction = []
for v in range(len(sensor4)):
    subtraction.append((- sensor5[v] - sensor4[v])/2)

print(subtraction)

# build composite
fig = plt.figure(figsize= (10, 5))
grid = GridSpec(3, 4, fig)
plt.subplots_adjust(wspace=0.5)

box1 = fig.add_subplot(grid[1, 0])
plt.plot(sensor4, color= 'black')
plt.title('Sensor id = 4')
plt.ylim(0,100)
plt.xlim(0,800)

box2 = fig.add_subplot(grid[0:3, 1:3])
plt.plot(subtraction, color='red')
plt.title("Sensor#4 - Sensor#5")

box3 = fig.add_subplot(grid[1, 3])
plt.plot(sensor5, color= 'blue')
plt.title('Sensor id = 5')
plt.ylim(0,100)
plt.xlim(0,800)

plt.show()

```

## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/e47749ec-b828-4a71-aba3-48fa4de6b3f9)

<sub>Fig. 2 shows results of program

