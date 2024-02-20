# Quiz 044

Coninuation of the answer:
3. The reason the bank went bankrupt is because the sql table was being manipulated to increase the amount of money in user 12's balance artificially. This allowed to withdraw theoretically infinte money, or till the bank went bankrupt.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/e89e9294-4ad7-4337-b333-1ac3f075e389)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```sql
select total(amount) from transactions where transaction_type='deposit' group by account_id;
select sum(amount) from transactions where transaction_type='withdraw' group by account_id;
select balance from accounts;
select first_name, last_name from customers where customer_id=12
-- 2. deposits = 5200, withdrawals = 600, therefore real balance = 4600, but in fact it is 5000 --

```
## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/13f2df3c-95ab-432b-8d62-bb6671242206)

<sub>Fig. 2 shows results of program

## ER Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/a7e986f9-fc89-4f13-8a85-06cdca355f06)

<sub>Fig. 3 shows ER Diagram

