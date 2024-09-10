# Quiz 079

## Task
![image](https://github.com/user-attachments/assets/1d070d19-0e38-4d5e-b757-5cd39953ccaa)

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
def parity_bit_counter(n):
    n = len(n)
    k = 1
    while not 2**k >= k + n + 1:
        k += 1
    return k

def equation_maker(k,n):
    m = k+n
    par_overall = []
    for i in range (1,k+1):
        par = []
        for j in range(0, m+1):
            if j & int(2**(i-1)):
                par.append(j-1)
        par_overall.append(par)
    return par_overall

def position_parity(m, k):
    n = []
    count_m = 0
    count_k = 0
    for i in range(0, k+len(msg)):
        if i+1 != 0 and (i+1 & (i)) == 0:
            n.append(-1)
            count_k += 1

        else:
            n.append(int(m[count_m]))
            count_m += 1

    return n

def combiner(template:list, equations:list): # takes in a list of lists
    for e in equations: # in each list of values
        total = 0
        for i in range(1, len(e)):
            total += template[e[i]]
            template[e[0]] = total % 2
    out = ''
    for l in template:
        out += str(l)
    return out

# Execution
msg = '1011'
k = parity_bit_counter(msg)
template = position_parity(msg, k)
equations = equation_maker(k, len(msg))
final = combiner(template, equations)
print(final)
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence
![image](https://github.com/user-attachments/assets/34d21c32-a63b-4797-9ba5-558688181f6e)

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>
