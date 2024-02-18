# Quiz 047

## Input & Output


<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from my_db_library import DatabaseBridge, get_hash
from secure_password import check_password
my_db = DatabaseBridge("bitcoin_exchange.db")
query = """SELECT * from ledger"""
results = my_db.search(query, True)
print(results)
my_db.close()

for row in results:
    id = row[0]
    sender_id = row[1]
    receiver_id = row[2]
    amount = row[3]
    hash = row[4]
    ver_start_hash = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    if check_password(hash, ver_start_hash):
        print(True)
    else:
        print(False)
```

## Evidence

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/00b9f64c-aceb-4d7d-87ab-98fa75e3071c)

<sub>Fig. 2 shows results of program

## UML Diagram

<sub>Fig. 3 shows UML Diagram