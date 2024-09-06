# Quiz 078
Please fill this in
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
![image](https://github.com/user-attachments/assets/bb0d1a8c-5874-4c04-b61d-1449d4f2e6b4)

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>

## Algorithm 2
This algorithm, instead of returning the list of numbers needed to calculate a requested parity bit k (like it's predecessor), creates a list of lists with the numbers needed to calculate ALL the parity bits for a given message msg.
```.py
def parity_maker(k,n):
    m = k+n
    par_overall = []
    for i in range (0,k):
        par = []
        for j in range(0, m+1):
            if j & 2**(i-1):
                par.append(j)
        par_overall.append(par)
    return par_overall

test1 = parity_maker(4,3)
print(test1)
...

