# Quiz 040
Nice color changer. I also wanted to change the text of the raised button to say light mode once it is put into dark mode, for UX optimization.
## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/da11a361-041d-4835-8c36-869fed659901)
<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from kivymd.app import MDApp

class Quiz040(MDApp): # Class name needs to be capitalized by convention
    def build(self):
        return

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def button_pressed(self):
        if self.root.ids.Namaewa.md_bg_color == [1.0, 1.0, 1.0, 1.0]:
            self.root.ids.Namaewa.color = [1.0, 1.0, 1.0, 1.0]
            self.root.ids.Namaewa.md_bg_color = 'black'
            self.root.ids.Mode.md_bg_color = '#17517E'
            self.root.ids.Mode.text = 'Switch To Light Mode'
        else:
            self.root.ids.Namaewa.color = 'black'
            self.root.ids.Namaewa.md_bg_color = [1.0, 1.0, 1.0, 1.0]
            self.root.ids.Mode.md_bg_color = 'blue'
            self.root.ids.Mode.text = 'Switch To Dark Mode'

test040 = Quiz040()
test040.run()
```
```kv
Screen:
    size: 800, 800

    MDLabel:
        id: Namaewa
        color: "black"
        text: "Your Name"
        font_size: '64pt'
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Center the label
        md_bg_color: 'white'
        halign: 'center'
        valign: 'middle'


    MDRaisedButton
        id: Mode
        size_hint: 0.01, 0.06
        pos: 0, 0
        md_bg_color: 'blue'
        text: "Switch To Dark Mode"
        on_press:
            app.button_pressed()
```

## Evidence
https://drive.google.com/drive/folders/1WNot5-PMKYvYb2ZYly68xEN9eQcUS94j?usp=sharing
<sub>Fig. 2 shows results of program

## UML Diagram
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/6fb1daa2-4586-474c-913f-091b980686cd)

<sub>Fig. 3 shows UML Diagram
