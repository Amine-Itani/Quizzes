# Quiz 020
In this quiz, we explored using the random integer generator. Using the seeding function, although it is random, we get the same random numbers. We also did not get the expected output even though the equation is right.  

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/c2192ab1-20be-402e-b051-1021d6a3cf52)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
import random
def produce(n, m, s):
    random.seed(1234) # seeding to get the same numbers as everyone else
    title = f"|      x       |      y(x)    |\n"
    out = f"{title.center(10)}" # center(10) to make it look nice
    y = []
    x = []
    for i in range(n):
        x_rnd = random.randint(1,100)
        y_rnd = x_rnd**(-0.5*((m/s)**2)) # the mathematical equation
        y.append(round(y_rnd, 2)) # round function
        x.append(x_rnd)
        out += f"|  {str(x[i]).center(10)}  |  {str(y[i]).center(10)}  |\n".ljust(10)
    return out

sample = produce(5, 3, 2)
print(sample)
```

## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/0491b9bd-cb1b-475a-bf27-6117b45ce5eb)

<sub>Fig. 2 shows results of program

## Truth Table Proof
### A(A + B) = A

| A B | A + B | A(A + B) |
|-----|-------|----------|
| 0 0 |   0   |     0    |
| 0 1 |   1   |     0    |
| 1 0 |   1   |     1    |
| 1 1 |   1   |     1    |

<sub>Fig. 3 shows truth table of equation

As you can see in the truth table, when A = 0 | A(A + B) = 0, and when A = 1 | A(A + B) = 1
Therefore A(A + B) = A

