# Quiz 074
This quiz is an error detection algorithm, based on the parity bit of each message. An estimation of the efficiency of the algorithm will be determined at the end.

## Task
![image](https://github.com/user-attachments/assets/d3e26942-ebf6-4cc2-b169-a2c7ec5e5f57)

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
def parity_error_check(msg:str):
    count = 0
    for n in range(1,len(msg)):
        if msg[n] == '1':
            count += 1
    if count % 2 == 0: # even number of ones
        if msg[0] == 1:
            return False
        else:
            return True
    else: # odd number of ones
        if msg[0] == '0':
            return False
        else:
            return True

test1 = parity_error_check('100111001011001110010110011100101')
print(test1)
test2 = parity_error_check('011101111101110111110111001111')
print(test2)

```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence
![image](https://github.com/user-attachments/assets/f39bb338-cf62-44d5-8132-bab8a564838e)

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>
