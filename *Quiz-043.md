# Quiz 043
THIS QUIZ IS COMPLETELY WRONG WTF ARE YOU DOING
## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/b6012f3a-235d-43fe-8e09-facde5475e9f)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```sql
CREATE TABLE if not exists movies(
    id INTEGER PRIMARY KEY,
    name text,
    year int,
    budget real,
    category VARCHAR(100),
    director VARCHAR(100),
    producer VARCHAR(100)
);

INSERT INTO movies (year, budget, category, director, producer, name)
values('Whiplash', 2014, 3300000.00, 'Indie Psych Drama', 'Damien Chazelle', 'Bold Films, Blumhouse Productions, and Right of Way Films');

INSERT INTO movies (year, budget, category, director, producer, name)
values('The Grand Budapest Hotel', 2014, 25000000.00, 'Comedy-Drama', 'Wes Anderson', 'American Empirical Pictures, Studio Babelsberg, Fox Searchlight Pictures, Scott Rudin, and Steven Rales');

SELECT * from movies;
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/03bedd87-0d72-4277-b632-bd053bf1f482)

<sub>Fig. 2 shows results of program


