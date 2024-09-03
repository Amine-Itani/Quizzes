# Quiz 072
Although this quiz is in pseudocode, the template and logical thinking is still present in the python version. Note for revision: remember pseudocode conventions.

## Task
![image](https://github.com/user-attachments/assets/9bffa889-7d93-4cf2-aba2-d0ce880f47b4)

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
from array import array

Data = ["Ankara","Turkey","Tokyo","Japan","Lisbon","Portugal"]
Cities = [] # array(len(Data)/2)
Countries = [] # array(len(Data)/2)

for i in range(0, int(len(Data)/2)):
    Cities.append(Data[i]) # Cities[i[ instead
    Countries.append(Data[i+1]) # Countries[i] instead

print(Cities)
print(Countries)
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence
![image](https://github.com/user-attachments/assets/517e3e0b-4028-4a91-b734-e4a758dc4f43)

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>
