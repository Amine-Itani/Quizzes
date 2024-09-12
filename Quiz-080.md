# Quiz 080
First recursive function + trace table
## Task
![image](https://github.com/user-attachments/assets/f369263e-3dd4-4124-86f6-d77e1aceb6bb)

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
def function1(ins:list):
    if len(ins) == 1:
        return ins[0]
    else:
        m = function1(ins[1::])
        if ins[0] > m:
            return ins[0]
        else:
            return m

test1 = function1([4,5,8,7])
print(test1)
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Trace Table
![image_6209779](https://github.com/user-attachments/assets/b9d6f923-47fc-42f0-a15c-1c1a14e1b368)

<sub>Fig. 3 shows the trace table of the algorithm </sub>

## Results and Evidence
![image](https://github.com/user-attachments/assets/2168a13d-4a0c-46cd-b7ae-d0759437665f)

<sub>Fig. 4 shows the results of the task and evidence of completion</sub>
