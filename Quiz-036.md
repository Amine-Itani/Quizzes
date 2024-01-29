# Quiz 036

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/d8806f51-9ed4-4a9c-bd94-7cc1ad393f0c)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
class Converter:
    def __init__(self):
        self.my_dict_numerals = {
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert_to_roman(self, dec:float):
        output = ""
        if 0 < dec < 100:
            for key, value in self.my_dict_numerals.items():
                quot = dec // key
                output += value * quot
                dec %= key
        else:
            raise ValueError('Error. Number must be between 0 and 100')
        return output

test = Converter()
result = test.convert_to_roman(56)
print(result)
```

## Evidence
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/c2d2f732-fd1c-4688-a3c1-17504c9a9732)

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/6bdd4a0c-52b0-4630-a2f8-8e42a543b701)

<sub>Fig. 3 shows UML Diagram

