# Second Quiz!
In this quiz, we had to create a program that took in two integers and returned Ture if either of them were 20 or their sum was 20
It was relatively easy, but the hl with lists took me more time

## Code

```py
value1 = [10, 30, 10, 26]
value2 = [12, 15, 5, -6]
if 20 in value1 or 20 in value2:
    print("True")
for x in range(len(value1)):
    value1[x] += value2[x]
if 20 in value1:
    print("True")
else:
    print("False")
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/5a6c8d80-788c-4096-9ce2-5e37fea4cc71)
<sub>Fig.1 shows results of the program

## Flowchart
![Quiz002](https://github.com/Amine-Itani/Unit-1/assets/123438294/652ea29f-f1af-4c74-819d-20dfaec25368)
<sub>Fig.2 shows results of the program
