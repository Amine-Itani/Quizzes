# Quiz 039
This is the first quiz that used our newly acquired OOP and Kivy skills to make something cool and useful. We even added a minus button.

## Input & Output

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/3cf09340-19f7-4681-8147-da405f46646e)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from kivymd.app import MDApp

class quiz039(MDApp): # the name of this class is the same as the name of the *.kv file*
    def build(self):
        return

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.amount = 0

    def counter_pressed(self):
        self.amount += 1
        the_counter = self.root.ids.counter
        the_counter.text = f"Count {self.amount}"

    def remove_pressed(self):
        self.amount -= 1
        the_counter = self.root.ids.counter
        the_counter.text = f"Count {self.amount}"

test = quiz039()
test.run()
```
```kv
Screen:
    size: 500, 700

    MDBoxLayout:
        orientation: "horizontal"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size_hint: .7, .3 # width, height, h: relative
        md_bg_color: "#bde0fe"

        MDLabel:
            id: counter
            text: "Count 0"
            halign: "center"
            size_hint: .33, 1
            font_size: "34pt"
            color: "red"


        MDRaisedButton:
            id: add
            text: "Add +1"
            md_bg_color: "black"
            size_hint: .33, 1
            font_size: "34pt"
            on_press:
                app.counter_pressed()

        MDRaisedButton:
            id: remove
            text: "Remove -1"
            text_color: 'black'
            md_bg_color: "white"
            size_hint: .33, 1
            font_size: "34pt"
            on_press:
                app.remove_pressed()
```

## Evidence

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/a321c49f-4807-4017-838a-da38c0c27e59)

<sub>Fig. 2 shows results of program

## UML Diagram

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/477c5de0-24af-4bf8-9c6d-c12fae57c824)

<sub>Fig. 3 shows UML Diagram
