# Quiz 007
The goal of this program was to print all rooms in an hotel from in this pattern
- Room 1F01
- Room 1F02..
Then, at 10 rooms, add 1 to the floor numer (2F01, 3F01...).
It should also be able to fetch any room requested based on a single integer input.

## Code

```py
room_requested = int(input("Please pick where you would like to stay in CompSci Hotels. We have 1-100 rooms"))
real_room_requested = room_requested - 1
rooms = []
count = 1
for f in range(10):
    for r in range(10):
        room = f"{count} - Room {f+1}F{r+1:02}"
        count += 1
        rooms.append(room)
        print(room)

print((rooms[real_room_requested]))
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/f9a6fd4d-d551-4078-ab4b-1cc6ee055d3f)
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/9db35a7b-e9f3-47eb-a1bb-4d1ee27d2806)
<sub>Fig.1 shows results of the program

## Flowchart
![Quiz007](https://github.com/Amine-Itani/Unit-1/assets/123438294/4f8b2d75-83f0-4dfe-ab66-e54bb123d515)
<sub>Fig.2 shows results of the program
