# Quiz 076

## Task
Continuing our work with the the Hamming Code to efficiently check for errors in data transfers, this code is used to find the position of the parity bits in a code and add it, returning the message + the parity bits in the right positions.

## Algorithm
```.py
def position_parity(m, k):
    n=''
    count_m = 0
    count_k = 0
    for i in range(0, len(k)+len(m)):
        if i+1 != 0 and (i+1 & (i)) == 0:
            n += k[count_k]
            print(k[count_k])
            count_k += 1

        else:
            n += m[count_m]
            print(m[count_m])
            count_m += 1

    return n
```
# example test
test_1 = position_parity('1011', ['P0','P1','P2'])
print(test_1)

## Result
![image](https://github.com/user-attachments/assets/9dc742fa-e0c9-42cf-9df1-f83612f2971f)

<sub>Fig. 1 shows the result of the task</sub>
