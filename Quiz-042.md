# Quiz 042
Learning how to flip through different screens opens up a world of possibilities.

## Input & Output

![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/a0032a15-c1cd-4ba5-ba11-4acd11017e14)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class MysteryPageA(MDScreen):
    def change_to_page_two(self):
        self.parent.current = "MysteryPageB"
        self.ids.msgA.text = "This is mystery page A you pressed the button"

class MysteryPageB(MDScreen):
    def change_to_page_one(self):
        self.parent.current = "MysteryPageA"
        self.ids.msgB.text = "This is mystery page B you pressed the button"

class mystery(MDApp):
    def __init(self, **kwargs):
        super().__init__(**kwargs)

test = mystery()
test.run()
```
```kv
ScreenManager:
    id: main_scr
    MysteryPageA:
        name: "MysteryPageA"

    MysteryPageB:
        name: "MysteryPageB"

<MysteryPageA>
    MDRaisedButton:
        pos_hint: {"center_x":.5, "center_y":.5}
        on_press:
            root.change_to_page_two()

    MDLabel:
        id: msgA
        pos_hint: {"center_x": .5, "center_y":.7}
        size_hint: .5, .2
        text: ''


<MysteryPageB>
    MDRaisedButton:
        pos_hint: {"center_x":.5, "center_y":.5}
        on_press:
            root.change_to_page_one()

    MDLabel:
        id: msgB
        pos_hint: {"center_x": .5, "center_y":.7}
        size_hint: .5, .2
        text: 'This is mystery page B you pressed the button'
```

## Evidence
https://drive.google.com/drive/folders/1johIfnr1COchWXKu4uqkSJ91nOEaSQA0?usp=drive_link
<sub>Fig. 2 shows results of program
