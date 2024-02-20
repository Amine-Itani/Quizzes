# Quiz 048
Very interesting subject. Who knows, maybe this is how real, million dollar transactions around the world are calculated.
## Input & Output

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/6df67e6e-94cb-4a8f-9140-3e7b89d942fb)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from my_db_library import DatabaseBridge, get_hash
from secure_password import check_password
my_db = DatabaseBridge("bitcoin_exchange.db")
query = """SELECT * from ledger"""
results = my_db.search(query, True)
my_db.close()

total = 0
for row in results:
    id = row[0]
    sender_id = row[1]
    receiver_id = row[2]
    amount = row[3]
    hash = row[4]
    ver_start_hash = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    if not check_password(hash, ver_start_hash):
        total += amount
print(total)
```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/69cf67ef-7cb7-4ca8-8b63-943dea10bb33)

<sub>Fig. 2 shows results of program

## ER Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/06c1b089-4a13-4e11-848a-0e2bfcc1061a)

<sub>Fig. 3 shows ER Diagram
