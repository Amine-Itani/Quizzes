# Quiz 049
Messing with the bitcoin exchange ledger a little more, developing it to greater extent.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/edb9ffa6-cd2c-4a04-9687-221c9d89cff1)


<sub>Fig. 1 shows given intput and outputs of task
## Code

```sql
create table if not exists users(
    id int,
    name text,
    email text
);

insert into users (id, name, email)
values (560, 'AlGore', 'Algore@xyz.com'),
       (371, 'Kennedy', 'Kennedy@uwcisak.jp'),
       (488, 'Abraham', 'abraham@bl.jp'),
       (561, 'Ulysses', 'ulys@klo.eu'),
       (254, 'Clinton', 'clint@or.por'),
       (920, 'Adams', 'adam@ad.dm'),
       (438, 'Washington', 'wash@shash.wash'),
       (744, 'Truman', 'tru@man.com'),
       (261, 'Eisenhower', 'eisen@hower.usa');

select * from ledger where receiver_id=920 or sender_id=920
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/e2d0a3cf-a7ba-4290-a110-ec074cd21dd4)

<sub>Fig. 2 shows results of program

## ER Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/bbaa32e2-2c51-42df-950a-e5a5b8a14f49)

<sub>Fig. 3 shows ER Diagram
