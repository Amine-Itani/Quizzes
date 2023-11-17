# Quiz 010
For this quiz, we created an algorithm that presents all the days in a month in a calender fashion. This algorithm will also allow the user to input their month (theoretically their birthday month), and receive an accurate calendar of that month

## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/dffbb287-9169-4a8a-ba38-df1264c6f870)
<sub>Fig.1 shows the given task
## Code

```py
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# numbers based on 2023 month and day distribution
days1_10 = ['Sun', 'Mon', "Tues", "Wed", 'Thu', 'Fri', 'Sat']
days2_3 = ['Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue']
days4_7_11 = ['Sat','Sun', 'Mon', "Tues", "Wed", 'Thu', 'Fri']
days5 = ['Mon', "Tues", "Wed", 'Thu', 'Fri', 'Sat', 'Sun']
days6 = ['Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed']
days8_9_12 = ['Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu']
days = [days1_10, days2_3, days2_3, days4_7_11, days5, days6, days4_7_11, days8_9_12, days8_9_12, days1_10, days4_7_11, days8_9_12]

def bestMonth():
    global chosen_month # I learned that this allows the variable to be used in all for loops
    end_code = "\033[00m"
    red = "\33[0;31m"
    out_day = ""
    out_num = ''
    count = 0
    bday_month = str(input("Please input a month"))
    for x in months:
        if x == bday_month:
            chosen_month  = months.index(x) # fetching index of months to fetch index of days and connect to which list to use
    for d in range(1,32):
        out_num += f" {red}{days[chosen_month][count]} {d:2}{end_code} ".center(0)
        count += 1
        if count > 6:
            count = 0
            out_num += " | \n"

    print(out_num)
case1 = bestMonth()
print(case1)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/2098a12c-e3ae-46b7-b826-309aa4492cb8)
<sub>Fig.2 shows results of the program

## Flowchart

<sub>Fig.3 shows the flowchart of the program
