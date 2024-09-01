![image](https://github.com/user-attachments/assets/6d0bf97b-0bd0-4cfa-8de8-c273e1d8000f)# Quiz 073
This quiz is an error detector that bases itself off of the assum;tion that the message has been sent three times, one original and 2 copies. It only works if the only one of the copies is changed, but in that case it can be fixed as well, as shown in the second algorithm.

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

## Task 2
This algorithm looks at two identical copies and fixes the third one on that basis. Not the most efficient as it requires specific coniditons to work.

## Algorith 2: Error fix
``.py
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
```
## Results and Evidence
![image](https://github.com/user-attachments/assets/14b32e0e-db79-4abc-a8fb-88f58cbd26b2)

<sub>Fig. 4 shows the results of the task and evidence of completion</sub>
