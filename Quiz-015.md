# Quiz 015
Complicated quiz, but not impossible. Learned how to write and think with trace tables in this quiz.<br>
The trace table method of thinking has been quite useful with projects so far, especially when troubleshooting malfuctioning code.

## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/5fd3d97e-d10f-4462-8437-0b0fe1abdae4)
<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def open_doors(num_students):
    doors = []
    for x in range(num_students):
        doors.append("Close")
    step = 0
    for m in range(num_students):
        step += 1
        for y in range(0,num_students,step):
            if doors[y] == "Close":
                doors[y] = "Open"
            elif doors[y] == "Open":
                doors[y] = "Close"
    return doors

trial = open_doors(10)
print(trial)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/13c84584-0845-45bd-8fa9-224ab332b927)
<sub>Fig. 2 shows results of program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/e7007229-a1fd-47b6-9cd8-a6aa45f6aadc)<br>
<br><sub>Fig. 3 shows flowchart of program
