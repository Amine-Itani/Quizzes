# Quiz 023
Third data science quiz. This quiz coincided with my math lesson on absolute value functions, and building a graph from scratch on python actually helped me understand it better. Maybe data science has applications beyond data analysis but also learning.

## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/6f4a04c4-d79d-4236-862c-a4d95c2e2743)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from matplotlib import pyplot as plt

y = []
x = []
for num in range(-10, 11):
    x.append(num)
    y.append(abs(num))

plt.plot(x, y, 'r', linewidth=2)
plt.title("Graph of the equation Quiz 023")
plt.xlabel("x", fontsize=18)
plt.ylabel("$f(x)=|x|$", fontsize=18)
plt.show()
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/50a16064-b8dd-44ca-84d2-00c4d0a9dcc3)

<sub>Fig. 2 shows results of program

## Base Conversion
### FFA5 to decimal

15 x 16<sup>3</sup> + 15 x 16<sup>2</sup> + 10 x 16<sup>1</sup> + 5 x <sup>0</sup> =

61,440 + 3,840 + 160 + 5 = 

**65,445**
