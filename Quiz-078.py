# Quiz 078

## Task

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
def parity_maker(k,n,p):
    par = []
    m = k+n
    for i in range (0, m+1):
        if i & 2**(p-1):
            par.append(i)
    return par

test1 = parity_maker(3,4,3)
print(test1)
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>

