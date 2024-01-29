# Quiz 037

## Input & Output

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/847e4f02-e41f-433b-a392-5fc1bfc6f04c)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class CompoundInterest:
    def __init__(self, principal, rate, number_of_years):
        self.principal = principal
        self.rate = rate
        self.time = number_of_years

    def calculate_interest(self):
        projection = self.principal * (1 + self.rate) ** self.time
        return projection

class AccountingProgram(CompoundInterest):
    def __init__(self, principal, rate, number_of_years):
        super().__init__(principal, rate, number_of_years)

    def return_project(self):
        amount = self.calculate_interest()
        return amount

bob_money = AccountingProgram(100,0.1,20)
print(bob_money.return_project())
```

## Evidence

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/81cc5cf9-2e77-492c-b61f-4377416f23f0)

<sub>Fig. 2 shows results of program

## UML Diagram

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/66878fbf-1773-430b-8baa-5364e3c41c99)

<sub>Fig. 3 shows UML Diagram
