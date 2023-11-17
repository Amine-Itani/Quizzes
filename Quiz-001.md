# Quiz 001
## My first computer science quiz!!!!

In this exercise, we were to take a word, count the letters in it using the len function and concatonate it with the first and last letter of an input string, single or double letter strings are left the same

## Code

```py
a = str(input("Please enter a word"))
a = a.split()
output = ""
for word in a:
    if len(word) <= 2:
        output += word
    else:
        output += (word[:1] + str(len(word) - 2) + word[-1:] + " ")
print(output)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/4c67539b-9cea-48b5-8d4a-6648b7e4d35c)

<sub>Fig.1 shows results of the program

## Flowchart
![Quiz001](https://github.com/Amine-Itani/Unit-1/assets/123438294/e60f231a-387d-4326-9f3c-4e91243e8f08)
<sub>Fig.2 shows results of the program
