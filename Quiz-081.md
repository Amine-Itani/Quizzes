# Quiz 081
Recursive functions: trace table 2
## Task
![image](https://github.com/user-attachments/assets/c6724895-c210-49a8-986a-7b0d0ed55844)

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
def swap_letter(s, k, i):
    s_list = []
    for l in s:
        if l == k:
            to_swap_1 = s[k]
            s_list.append(0)
        if l == i:
            to_swap_2 = s[i]
            s_list.append(0)
        else:
            s_list.append(s[l])
    new_s = ''
    for j in range(0, len(s_list)):
        if j == k:
            new_s += to_swap_2
        if j == i:
            new_s += to_swap_1
        else:
            new_s += s_list[j]
def PERM(s:str, k:int):
    if k == len(s):
        return [s]
    else:
        out = []
        for i in range(len(s)):
            t = swap_letter(s, k, i)
            out.extend(PERM(t, k+1))

```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>
