# Quiz 074
This quiz is an error detection algorithm, based on the parity bit of each message. An estimation of the efficiency of the algorithm will be determined at the end.

## Task
![image](https://github.com/user-attachments/assets/d3e26942-ebf6-4cc2-b169-a2c7ec5e5f57)

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
def error_detection(data:str):
    pattern_size = int(len(data)/3)
    original, copy1, copy2 = '', '', ''
    for i in range(0, pattern_size):
        original += data[i]
        copy1 += data[i+pattern_size]
        copy2 += data[i+(2*pattern_size)]

    if original == copy1 and copy1 == copy2:
        return False
    elif original == copy1 and copy1 != copy2:
        copy2 = copy1
        new = original + copy1 + copy2
        return f"Error detected and fixed, new message: {new}"
    elif original == copy2 and copy1 != copy2:
        copy1 = copy2
        new = original + copy1 + copy2
        return f"Error detected and fixed, new message: {new}"
        return f"Error detected"
    elif copy1 == copy2 and original != copy2:
        original = copy1
        new = original + copy1 + copy2
        return f"Error detected and fixed, new message: {new}"
    else:
        return "Error detected and cannot be fixed"

test1 = error_detection('100111001011001110010110011100101')
print(f"Error detected: {test1}")
test2 = error_detection('011101111101110111110111001111')
print(f"Error detected: {test2}")
...
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>
