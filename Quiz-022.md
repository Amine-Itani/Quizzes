# Quiz 022
Second quiz about data science using matplotlib. I've found it quite interesting so far, and especially useful. One of the most important reasons I'm passionate about computer science is for it's infinite tangible applications, and what we're studing in data science seems like the precipice of it all. This could be quite useful for the startup my grademate Ethan and myself are working on, which involves collecting a lot of satellite imagery over really big area (+ 100,000 ha!) to help reforestation efforts on the ground. I will need a lot more eperience to do so.

## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/255b4926-2194-455e-b30e-36743818fa2d)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from matplotlib import pyplot as plt

# create the lists x and y
y = []
x = []
for num in range(-10, 10):
    x.append(num)
    y.append(2*((num + 5)**2)) # mathematical function

plt.plot(x, y, 'r', linewidth=2)
plt.title("Graph of the equation $f(x)=2(x+5)^2$") # title
plt.xlabel("x", fontsize=18) # x axis label
plt.ylabel("y", fontsize=18) # y axis label
plt.show()
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/e25de5f1-7722-4322-b750-358034761703)

<sub>Fig. 2 shows results of program

## Circuit
### not(bit0 bit1 + not (bit0 + bit1))
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/71de04a2-8884-4e91-99fb-4b3858733ee7)

<sub>Fig. 3 shows circuit of equation
