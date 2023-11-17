# Quiz 004
The function of this piece of code was to take a given integer and count how many factors it had. The modulus operator, for loops, and if statements came in handy here.
I enjoyed the HL part of this quiz as I learned about perfect numbers.

## Code

```py
in_number = int(input("Please enter a number"))
factors = []
sum = 0
for i in range(1, in_number):
    if in_number % i == 0:
        factors.append(i)
for x in range(len(factors)):
    sum += factors[x]
print(factors)
if sum == in_number:
    print("True")
else:
    print("False")
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/3bb8ff9b-fdf7-40df-96ac-b8a67def85c5)

<sub>Fig.1 shows results of the program

## Flowchart
![Quiz004](https://github.com/Amine-Itani/Unit-1/assets/123438294/14ff5464-238c-4db7-b932-49a8e42dddd7)
<sub>Fig.2 shows results of the program
