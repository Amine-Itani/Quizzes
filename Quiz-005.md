# Quiz 005
This algorithm sums up the number of letters of an input string based on the position of the letter in the alphabet.
We wrote the steps down for this one because it allowed us to understand it better, and our intermiediate step was the flowchart.
I did not understand the HL part of this exercise. I understand that the 1300 was added to the M is capital and it is the 13th letter of the alphabet, but where did the additional 56 come from?
## Code

```py
def sum_letters(text:str)->int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for let in text.lower():
        index = -1
        for i in range(len(alphabet)):
            if let == alphabet[i]:
                index = i + 1
        sum += index
    return sum

# proof of work
case1 = sum_letters(text="Math")
print(case1)
case2 = sum_letters(text="maTH")
print(case2)
case3 = sum_letters(text="Hello world")
print(case3)
case4 = sum_letters(text="Computer SCIENCE")
print(case4)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/13ba2c48-afc7-4037-81ef-b5c3f095d3f4)
<sub>Fig.1 shows results of the program

## Flowchart
![unnamed](https://github.com/Amine-Itani/Unit-1/assets/123438294/9a8037c7-32f0-4a3f-81cd-a48472762cb3)
<sub>Fig.2 shows results of the program
