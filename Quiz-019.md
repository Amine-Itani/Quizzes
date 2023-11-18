# Quiz 019
Same idea in this quiz. I love logic gates! The results of the eqaution in part a turned out different then the given example but I believe my work is correct.
## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/988fb0ff-a005-420c-8552-c471a9bc149d)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def get_truth():
    truth, a, b, c, result = '| A | B | C | AB + not B + not CB |\n', 1, 1, 1, 0 # define variables
    for x in range(8):
        if x % 4 == 0:
            a = int(not(a))
        if x % 2 == 0:
            b = int(not(b))
        c = int(not(c))
        result = int((a and b) or (not b) or (not (c and b))) # this results in different points then expected
        truth += f'| {a} | {b} | {c} |          {result}          |\n'

    return truth
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/fa6f7e97-3417-4d63-9761-f511ea5b2934)

<sub>Fig. 2 shows results of program

## Circuit
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/5efc3e67-a5a9-4474-af58-65b202f46f6c)

<sub>Fig. 3 shows the circuit b shown above

## Truth Table
|   W Y Z  | WZ | not(W) | Y(not(W)) (A) | A XOR Z (B) | WZ XOR B |
|----------|----|--------|---------------|-------------|----------|
|  0  0  0 |  0 |    1   |       0       |      0      |     0    |
|  0  0  1 |  0 |    1   |       0       |      1      |     1    |
|  0  1  0 |  0 |    1   |       1       |      1      |     1    |
|  0  1  1 |  0 |    1   |       1       |      0      |     0    |
|  1  0  0 |  0 |    0   |       0       |      0      |     0    |
|  1  0  1 |  0 |    0   |       0       |      1      |     1    |
|  1  1  0 |  1 |    0   |       0       |      0      |     1    |
|  1  1  1 |  1 |    0   |       0       |      1      |     0    |

<sub>Fig. 4 shows truth table of circuit
