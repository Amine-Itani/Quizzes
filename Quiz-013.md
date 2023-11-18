# Quiz 013
This quiz is our third blackbox. I was quite worried since the last one was pretty challenging for me, but it was actually quite simple. I think I overthought it last time.<br>
This program took in two strings A and B, and printed A as many times as there were characters in B (not counting spaces!).

## Input & Ouput
**Not found on the quizzzes slideshow.**<br>
_Input:_   A:"qwerty"  B:"lol lol"<br>
_Output_: "qwertyqwertyqwertyqwertyqwertyqwerty"

## Code

```py
def mysteryThree(A:str, B:str):
    output = ""
    for x in range(len(B)):
        output += A
    return output

out = mysteryThree('qwerty','lol lol')
print(out)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/3e27282a-afb8-476f-a325-d71f56137bef)

<sub>Fig.1 shows results of the program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/a426f73d-f352-4513-b07a-aa0a96a8aff9)
<sub>Fig.2 shows results of the program
