# Quiz 025
Errorbar graphs are more scientific than other graphs, allowing users to see figures while accounting for potential errors. To do this, the creator of the graph needs the mean and standard deviation on the data, which the numpy library can do very easily with it's mean and std functions. We append them to a list that we use to create the errorbar graph and the fill_between function with our maxes and minimums to give it a range to work in.

## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/f51a26ba-2a19-494d-adb5-d7df472533ee)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
import numpy as np
import matplotlib.pyplot as plt

sensorA = [16, 24, 24, 9, 23, 26, 26, 23, 25, 14]
sensorB = [2, 19, 25, 10, 11, 24, 17, 7, 24, 17]
sensorC = [15, 11, 24, 21, 6, 2, 18, 27, 1, 16]

data = []
for v in range(len(sensorA)):
    data.append([int(sensorA[v]), int(sensorB[v]), int(sensorC[v])])

x = [] # time in hours
t = 0
mean = [] # descriptive stats
std = [] # standard deviation
min_t = []
max_t = []
print(data)
for d in data:
    mean.append(np.mean(d))
    std.append(np.std(d))
    min_t.append(np.min(d))
    max_t.append(np.max(d))
    x.append(t)
    t += 1

plt.errorbar(x, mean, std, fmt="o", color="#023047")
plt.fill_between(x, max_t, min_t, alpha=0.5, linewidth=0, color='#8ecae6')
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (C)")
plt.show()
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/b846df78-bd3f-402f-a23e-77e879fbf18e)

<sub>Fig. 2 shows results of program

## Base Conversion
### red = 250, green = 100, blue = 10

#FA640A

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/966844dd-ae11-43b9-8fa4-28587640ba6d)

<sub>Fig. 3 shows color expressed by hex value



