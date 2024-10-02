# Quiz 084
Recursive Functions: Trace Table 5
## Task
![image](https://github.com/user-attachments/assets/f9871aa0-00d2-4464-ab20-424c970b121b)

<sub>Fig. 1 shows the task at hand</sub>
*In class, given input was N = 8
## Algorithm
```.py
def FUNC(N):
  if N == 0:
    return 0
  if N== 1:
    return 1
  else:
return FUNC(N-1) + FUNC(N-2)
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence
![IMG_5534](https://github.com/user-attachments/assets/bab1c04e-a07d-41b9-849c-c9e182e570d5)
<sub>Fig. 3 shows the results of the task and evidence of completion</sub>

## Fun Fact! Other Mathematical Methods
This recursive functions automates the sum of an integer and every integer before it down to one.

In broader mathematical terminology, the results of these functions are known as a [Triangular Numbesr](https://en.wikipedia.org/wiki/Triangular_number#:~:text=0%2C%201%2C%203%2C%206,%2C%20630%2C%20666...). This is because they can be broken down and set up in a manner that turns them into an equilateral triangle. This is because every layer of the triangle contains one less number of units than the one before it.

Another interesting way of calcualting these numbers is with the very elegant formula N+1C2, where N is the same as the variable from before. The mathematical proof for this is quite interesting, and you can ask me to show it in real life.
