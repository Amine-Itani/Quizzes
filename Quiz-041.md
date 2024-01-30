# Quiz 041
Coding an XO game is nice because it does not need wifi to run, so theoretically if I code a win function (easier said than done), I can have a wifi free XO game made by yours truly.
## Input & Output

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/bd3b9c8d-d9ab-4cb3-aa68-d1f3ce746fb0)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from kivymd.app import MDApp

class quiz041(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turn = 1
        self.label = ''

    def build(self):
        pass

    def switch(self, btn):
        if self.turn == 1:
            btn.md_bg_color = "yellow"
            btn.text = "X"
            self.turn = 0
            self.root.ids.label.text = "It is O's turn"
        else:
            btn.md_bg_color = "orange"
            btn.text = "O"
            self.turn = 1
            self.root.ids.label.text = "It is X's turn"

test1 = quiz041()
test1.run()
```
```kv
Screen:
    size: 500, 500

    MDBoxLayout:
        orientation: "horizontal"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        size_hint: 1, 0.2

        MDLabel:
            md_bg_color: "white"

        MDRaisedButton:
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)

        MDRaisedButton:
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)

        MDRaisedButton:
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)

        MDLabel:
            md_bg_color: "white"

    MDBoxLayout:
        orientation: "horizontal"
        pos_hint: {"center_x":0.5, "center_y":0.4}
        size_hint: 1, 0.2

        MDLabel:
            md_bg_color: "white"

        MDRaisedButton:
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)

        MDRaisedButton:
            id: five
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)


        MDRaisedButton:
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)


        MDLabel:
            md_bg_color: "white"


    MDBoxLayout:
        orientation: "horizontal"
        pos_hint: {"center_x":0.5, "center_y":0.6}
        size_hint: 1, 0.2

        MDLabel:
            md_bg_color: "white"

        MDRaisedButton:
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)


        MDRaisedButton:
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)


        MDRaisedButton:
            text: ''
            md_bg_color: "green"
            font_size: "20pt"
            size_hint: 1, 1
            on_press:
                app.switch(self)


        MDLabel:
            md_bg_color: "white"

    MDLabel:
        id: label
        pos_hint: {"center_x":0.5, "center_y":0.75}
        md_bg_color: "white"
        size_hint: 0.15, 0.05
        text: "It is X's turn"


    MDLabel:
        pos_hint: {"center_x":0.55, "center_y":0.85}
        md_bg_color: "white"
        size_hint: 0.4, 0.05
        text: "Tic Tac Toe by Amine"
        font_size: "20pt"
```

## Evidence

https://drive.google.com/drive/folders/1GBcHMjhRzC8VT2uPyMK8UhZ2oEx41XGX?usp=sharing

<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/c0694d27-9c98-4584-bd21-33c23c215713)

<sub>Fig. 3 shows UML Diagram

