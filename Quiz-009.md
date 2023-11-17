# Quiz 009
This code takes an integer input and turns it into different iterations of power from pico (10^-12) to tera (10^12). It also takes a string input as the units of the output.

## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/e1996d6d-7b7f-4de9-b637-7fddf9ecc7cb)
<sub>Fig.1 shows the given of the task
## Code

```py
# define variable
num = input("Please enter a number")
unit = input(f"{num} of what? Please enter a unit")
units = [" Kilo", " Mega", " Giga", " Tera"]
powers = ["000", "000000", "0000000000", "000000000000"]
microunits = ["Mili", "Micro", "Nano", "Pico"]
powers2 = ["00", "00000", "00000000", "00000000000"]

# functions
for x in range(len(units)):
    output = f"{num}{powers[x]}{units[x]}{unit}"
    print(output)
print(f"{num} {unit}")
for x in range(len(microunits)):
    output2 = f"0.{powers2[x]}{num} {microunits[x]}{unit}"
    print(output2)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/01820b45-760d-4e41-b56b-88759da37ad6)
<sub>Fig.2 shows results of the program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/7cc59ebf-bda6-47c5-91bb-d07d7079286f)
<sub>Fig.3 shows the flowchart
