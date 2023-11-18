# Quiz 014
This quiz was both easier and harder than other blackboxes of its kind. It was easier to figure out the pattern, but much harder to code. Dr. Ruben explained it in class and then it seemed easier. <br>
For future reference, indices are really useful with for loops when it comes to iterating through every character in a string or every item in a list.
## Inputs & Outputs
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/29aea05d-a597-4fdf-ab93-9e0013ac086c)
<sub>Fig. 1 shows inputs and outputs of given program
## Code

```py
def blackBoxThree(given:str):
    output = ""
    counts = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for x in range(26):
        counts.append(0)

    for letter in given:
        for i in range(26): # 26 iterations for 26 letter
            if letter == alpha[i]: # using index and if allow us to add 1 to the proper
                # count position only when i is correct
                counts[i] += 1
                output += str(counts[i])
        else: # adding the white space
            if letter == ' ':
                output += ' '

    return output

out = blackBoxThree(given = "hello world")
print(out)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/bd688cdf-6567-400f-9940-66a8457af146)
<sub>Fig. 2 shows results of program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/b3fd3f86-8bf0-446b-9203-5eb94359751b)
<sub>Fig.3 shows flowchart of program
