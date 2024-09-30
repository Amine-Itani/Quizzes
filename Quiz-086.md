# Quiz 086

## Task

<sub>Fig. 1 shows the task at hand</sub>

## Algorithm
```.py
class Item:
    def __init__(self):
        self.x = None
        
    def set(self, value):
        self.x = value
        
    def get(self):
        return self.x
    
# Composition: Strong association between class Item and class Queue

class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, value):
        self.data.append(Item.set(value))
        
    def dequeue(self):
        out = self.data.append[0]
        self.data = self.data[1:]
        return out
    
    def isEmpty(self):
        return len(self.data) == 0
```
<sub>Fig. 2 shows the algorithm used to tackle the task</sub>

## Results and Evidence

<sub>Fig. 3 shows the results of the task and evidence of completion</sub>
