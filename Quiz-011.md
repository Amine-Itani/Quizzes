# Quiz 011
In this quiz, we created a function that returned a multiplication table of a number inputed. We used an if statement to check whether the number was in betwenn 2 and 10, and a for loop to create the string. This would've made the second grade so much easier!

## Inputs & Outputs
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/7bda78a6-bd2b-427e-8075-82ec06e5939c)

## Code

```py
def mulTable(num:int)->str:
    output = ""
    if 1 < num < 10:
        for x in range(1,10):
            output += f"{num} * {x} = {num*x}\n"
    else:
        print(f"ERROR. Please enter a number between 2 and 10 inclusive.")
    return output

out = mulTable(2)
print(out)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/2dd0372e-f22a-40ba-abb5-3dfa9fa2d9ba)
<sub>Fig.1 shows results of the program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/f721da45-dcc3-417e-af17-07409ced8165)
<sub>Fig.2 shows results of the program
