# Quiz 026
Another useful quiz whne it comes to data science. Learning how to store data in a dictionary, one of the most efficient ways when it comes to graphs, and using them to plot, is pretty important.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/3187f4d0-8543-4e50-a2cc-4d11439782f1)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
# Create a graph using a dictionary
from matplotlib import pyplot as plt
# dict defined as x key with list as value attached, same for y
data = {
    'x' : [],
    'y' : [24, 1, 2, 25, 26, 21, 23, 34, 49, 2, 19, 32, 7, 17, 36, 7, 45, 28, 40, 46] # addded manually
}
t = 0
for x in range(len(data['y'])): # x-axis is time, buidling it out here
    data['x'].append(t)
    t += 1

data['title'] = 'quiz_data_science' # adding key and value to dict

plt.plot(data['x'], data['y'], 'r', linewidth=2) # plot data from dictionary
plt.title(data['title'])
plt.xlabel("x", fontsize=18)
plt.ylabel("y", fontsize=18)
plt.show()
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/85053875-2f92-44ca-a33a-2ba766bb0718)

<sub>Fig. 2 shows results of program

## Base Conversion
### Red = 10, Blue = 255, Green = 235

#0AFFEB

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/fd8a431c-09e0-446a-bfcb-e989fe47427e)


<sub>Fig. 3 shows color corresponding hex value
