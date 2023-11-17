# Quiz 006
The goal of this algorith is to generate a random 8 digit password, using the new function random.randInt()
We imported our first library called: random
## Code

```py
import random

def get_password()->str:
    password = ''
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for x in range(20):
        n = random.randint(0,len(symbols))
        password += symbols[n]
    return password

case1 = get_password()
print(case1)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/a0a22d8b-cd9b-413a-9244-567a431fb141)
<sub>Fig.1 shows results of the program

## Flowchart
![Quiz006](https://github.com/Amine-Itani/Unit-1/assets/123438294/96522c9c-5fb3-437c-83ed-8fa23030ef7b)
<sub>Fig.2 shows results of the program
