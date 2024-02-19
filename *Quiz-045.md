# Quiz 045
It was interesting to combine python and sqlite, and I am currently thinking of application for this combination in my project 3. I've noticed, the DatabaseBridge will be vital for any and all sql+python stacks I create in the future.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/8490bfe9-c926-4ed3-91af-49c361421d58)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from my_db_library import DatabaseBridge

haiku = """Code flows like a stream
Algorithms guide its way
In silence, it solves"""

# Create Database with table Words
my_db = DatabaseBridge('quiz45.db')
create_query = """CREATE table if not exists WORDS (
    id INTEGER PRIMARY KEY,
    length int,
    word text
)
"""

my_db.run_query(query=create_query)

for word in haiku.split():
    # insert every word and length into the database
    insert_query = f"""INSERT into WORDS (length, word)
    values({len(word)},'{word}')
    """
    my_db.run_query(query=insert_query)

find_average = """SELECT avg(length) from WORDS
"""
out = my_db.search(query=find_average, multiple=False)

my_db.close()
print(f"The average word length is {out}")
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/b28cc3be-8cb6-4236-ba0d-382dc6b8ab94)

<sub>Fig. 2 shows results of program

## ER Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/a77630bc-bd5f-428a-b2e1-8e519fd9097f)

<sub>Fig. 3 shows ER Diagram

The ER diagram posted with the quiz was wrong, so made my own
