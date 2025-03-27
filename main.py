from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainWidget(Widget):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     boutton = Button(text="Button")
    #     label = Label(text="Je suis un label")
    #     label.pos = (200,0 )
    #     label.color = "red"
    #     self.add_widget(boutton)
    #     self.add_widget(label)

    pass

class MainApp(App):
    # def build(self):
    #     interface = MainWidget()
    #     return interface
    pass

app = MainApp()
app.run()