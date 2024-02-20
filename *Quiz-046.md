# Quiz 046
My first full stack of sqlite, python, and kivy. I wonder the world of possibilites this opens up for me in making new projects.

## Input & Output
![image](https://github.com/Amine-Itani/Quizzes/assets/123438294/5ec2627b-011e-4fdc-bda4-fdb37ff354b6)


<sub>Fig. 1 shows given intput and outputs of task
## Code
```py
from kivymd.app import MDApp
from my_db_library import DatabaseBridge, get_hash
from Quizzes.quiz046.secure_password import check_password
db = DatabaseBridge("payments (3).db")


class quiz046(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components = {"base":0, "inhabitant":0, "income_tax":0, "health":0, 'pension':0, 'total':0, 'hash':''}
        self.my_db = db

    def build(self):
        return

    def save(self):
        pass

    def update(self):
        base = self.root.ids.base.text
        if base:
            total = int(base)
            hash_str = ""

            inhabitant = total* int(self.root.ids.inhabitant.text or 0)//100
            self.root.ids.inhabitant_label.text = f"{inhabitant} JPY"

            pension = total* int(self.root.ids.pension.text or 0) // 100
            self.root.ids.pension_label.text = f"{pension} JPY"

            health = total* int(self.root.ids.health.text or 0) // 100
            self.root.ids.health_label.text = f"{health} JPY"

            income = total * int(self.root.ids.income_tax.text or 0) // 100
            self.root.ids.income_tax_label.text = f"{income} JPY"

            total = total - (inhabitant + pension + health + income)

            # save taxes in the self.components dict defined in the init
            hash = f"base{base},inhabitant{inhabitant},income_tax{income},pension{pension},health{health},total{total}"
            self.components['hash'] = hash
            self.components['base'] = base
            self.components['inhabitant'] = inhabitant
            self.components['pension'] = pension
            self.components['income_tax'] = income
            self.components['total'] = total

            self.root.ids.salary_label.text = f'{total} JPY'
            query = """SELECT * from payments"""
            results = db.search(query, True)
            for row in results:
                id = row[0]
                base = row[1]
                inhabitant = row[2]
                income = row[3]
                pension = row[4]
                health = row[5]
                total = row[6]
                hash_make = f"base{base},inhabitant{inhabitant},income_tax{income},pension{pension},health{health},total{total}"
                hash_pay = row[7]
                if not check_password(hash_pay, hash_make):
                    self.root.ids.titlet.text = 'Database fraudulent! Data not saved'
                else:
                    print(False)


    def save(self):
        base = self.components['base']
        income_tax = self.components['income_tax']
        pension = self.components['pension']
        health = self.components['health']
        inhabitant = self.components['inhabitant']
        total = self.components['total']
        hash = get_hash(self.components['hash'])
        query = f"""INSERT into payments(base, inhabitant, income_tax, pension, total, health, hash)
        values({base},{inhabitant},{income_tax},{pension},{total},{health},'{hash}')
        """

        self.my_db.run_query(query=query)

        self.root.ids.hash.text = f"Payment saved"

    def clear(self):
        for label in ["base", "inhabitant","income_tax","pension","health"]:
            self.root.ids[label].text = ""
            self.root.ids[label+"_label"].text = " JPY"

        self.root.ids["salary_label"].text = " JPY"
        self.root.ids.hash.text = "----"

    def check_hash(self):

        query = """SELECT * from ledger"""
        results = db.search(query, True)
        db.close()




test = quiz046()
test.run()

```

```kv
MDScreen:
    id:bck
    size: 200, 500

    MDBoxLayout:
        id: bck
        size_hint: .8,.9
        md_bg_color: "#F2F2F2"
        orientation: "vertical"
        pos_hint: {"center_x":.5, "center_y":.5}
        spacing: dp(10)

        MDLabel:
            id: titlet
            text:"Compensation Calculator"
            halign: "center"
            font_style:"H4"
            color: "#222222"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDIcon:
                icon: "plus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
            MDLabel:
                text:"Base Salary"
                size_hint_x: .4
            MDTextField:
                id:base
                mode: "rectangle"
                input_filter:"int"
                text_color_normal: "#222222"
                line_color_normal: "#222222"
                hint_text: "Base Salary"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    root.ids.base_label.text = f"{self.text} JPY"
                    app.update()
            MDLabel:
                id: base_label
                text:" JPY"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Health"
                size_hint_x: .4
                color: "#6a040f"
            MDTextField:
                id:health
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Health"
                pos_hint: {"center_x": .5, "center_y": .5}
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: health_label
                text:" JPY"
                color: "#9d0208"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text: "Pension"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:pension
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Pension"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: pension_label
                text:" JPY"
                color: "#9d0208"


        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Income Tax"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:income_tax
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Income"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: income_tax_label
                text:" JPY"
                color: "#9d0208"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Inhabitant Tax"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:inhabitant
                mode: "rectangle"
                input_filter:"int"
                hint_text: "%  Income"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: inhabitant_label
                text:" JPY"
                color: "#9d0208"


        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#22223b"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDLabel:
                size_hint_x: .5
            MDIcon:
                icon: "calculator"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#F2F2F2"
            MDLabel:
                text:"Net Salary"
                size_hint_x: .4
                color: "#F2F2F2"
            MDLabel:
                id: salary_label
                text:" JPY"
                color: "#F2F2F2"
            MDFloatingActionButton:
                icon:"content-save-plus"
                md_bg_color:"#ffc300"
                icon_color:"#222222"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:
                    app.save()


            MDFloatingActionButton:
                icon:"autorenew"
                md_bg_color:"#2a9d8f"
                icon_color:"#222222"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:
                    app.clear()


        MDBoxLayout:
            size_hint: .8, .2
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}

            MDLabel:
                id: hash
                halign: "center"
                text: "----"
                font_style: "Caption"
```

## Evidence
https://drive.google.com/drive/folders/16vmLtwAy_Iv1EPWMQ-HVx8WCsYLnPtx7?usp=drive_link 

<sub>Fig. 2 shows results of program

## UML Diagram

<sub>Fig. 3 shows UML Diagram

## ER Diagram

<sub>Fig. 4 shows ER Diagram
