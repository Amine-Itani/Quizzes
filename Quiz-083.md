# Quiz 083
Recusive functions: trace table #3
## Task
![image](https://github.com/user-attachments/assets/296bd211-e047-428f-81c6-e8c157f78bcc)

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
def FUNC(N):
  if len(N)==1:
    return N[0]
  else:
    mid = len(N)//2
    L = FUNC(N[:mid])
    R = FUNC(N[mid:])

  return L + R
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>
