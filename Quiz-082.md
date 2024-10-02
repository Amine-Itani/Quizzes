# Quiz 082
Recursive functions: trace table #3

This recursive function, while seemingly basic, is an ingenious and elegant way of calculating factorials.
## Task
![image](https://github.com/user-attachments/assets/77b17892-1a69-4f5e-b450-5f789f01413b)

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
def FUNC(N):
  if N == 1 or N == 0:
    return 1

  else:

    return N*FUNC(N-1)
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence
![IMG_5539](https://github.com/user-attachments/assets/804382a4-f46a-4062-8e69-478435d7e66d)

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>
