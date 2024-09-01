# Quiz 073

## Task
![image](https://github.com/user-attachments/assets/47e10438-ba4a-423e-b6b6-0e0a9431ec25)

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
    else:
        return True

test1 = error_detection('100111001011001110010110011100101')
print(f"Error detected: {test1}")
test2 = error_detection('011101111101110111110111001111')
print(f"Error detected: {test2}")
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence
![image](https://github.com/user-attachments/assets/c2b38b26-b597-4754-9702-08584127519b)

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>

