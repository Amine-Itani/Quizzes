# Quiz 043
Maybe trying to use join for everything is not a good idea. Lesson learned.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/b6012f3a-235d-43fe-8e09-facde5475e9f)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```sql
-- 1. There are technically 4 tables counting sqlite_master, but 3 that are usable --

SELECT count()from INHABITANT where (gender='Male' and state='Friendly');

-- 2. There are 4 inhabitants that are friendly and male --

select avg(gold) from inhabitant where villageid = 1;
select avg(gold) from INHABITANT where villageid = 2;
select avg(gold) from INHABITANT where villageid = 3;
select avg(gold) from INHABITANT where villageid = 4;

-- 3. Stoneville average gold = 129.17, Slowville avg gold = 112.5,
-- Steepmount avg gold = 137.5, Wetriver avg gold = 118.75 --

select count() from item where item like 'A%'

-- 4. There are 3 items that begin with the letter A --

select distinct count(job) from INHABITANT

-- 5. There are 20 different distinct jobs --

select item.item from item, inhabitant where inhabitant.villageid=item.owner and inhabitant.job='Herbalist'

-- 6. Items in the evidence below --    
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/1645e2ce-916b-4e0c-a26d-15cb81bf3fb3)

<sub>Fig. 2 shows results of program

## ER Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/a7e986f9-fc89-4f13-8a85-06cdca355f06)

<sub>Fig. 3 shows ER Diagram of database


