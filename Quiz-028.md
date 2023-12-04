![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/72d9641e-d484-4a8c-9b3e-fc0534239fed)# Quiz 028
The SL part was easy, but the HL part was quite tricky. Fortunately, Python is awesome and good troubleshooting techniques (inserting strings everywhere) can get me through anything.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/9bf9dbce-88cc-468d-9fa1-646286210791)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def inverter(in_dict):
    invert_keys, invert_values, out_dict = [], [], {}
    for k, v in in_dict.items():
        invert_values.append(k)
        invert_keys.append(v)
    print(f"the new keys are {invert_keys}\n the new values are {invert_values}")
    for i in range(len(invert_keys)):
        if invert_keys[i] in out_dict:
            print(f"{out_dict[invert_keys[i]]},round:{i}")
            out_dict[invert_keys[i]].append(invert_values[i])
        else:
            out_dict[invert_keys[i]] = [invert_values[i]]
    return out_dict

some = inverter({'q1':True, 'q2':False, 'q3':True})
print(some)
```

## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/e867cf7b-db87-49ff-9768-b525463d18f9)

<sub>Fig. 2 shows results of program

## Binary Addition
### 1011 + 1101 

1011 in decimal is 11

1101 in decimal is 13

11 + 13 = 24

24 in binary is **11000**
