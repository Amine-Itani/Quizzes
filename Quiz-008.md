# Quiz 008
This program takes in any message and encrypts it by shifting the letter down the alphabet a chosen amount of times. A simpler version of the enigma machine!<br>
Two for loops and some indexing logic should do the trick here. The modulo equation keeps the index from going out of the alphabet's bounds.
## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/ce5d76aa-bcc6-421f-85d4-50675cb70fcb) 
<sub>Fig.1 shows the given of the task
## Code

```py
def SimpleEncryptor(data, shift):
    encryption = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in data:
        for l in alphabet:
            if letter == l:
                encryption += f"{alphabet[(alphabet.index(l)+shift)%len(alphabet)]}"
        if letter == " ":
            encryption += f" "
    return encryption

trial = SimpleEncryptor(data= "secret", shift=-10)
print(trial)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/4d400387-d648-4fa8-a5df-e3c415c51f78)
<sub>Fig.2 shows results of the program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/e0e80209-b30d-4ab8-9cf2-a2957bd32221)
<sub>Fig.3 shows the flowchart of the program
