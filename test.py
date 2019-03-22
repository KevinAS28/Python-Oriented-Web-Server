import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
class OWS(GridLayout):
    def prin(self, label):
        print(label.text)
    def __init__(self, **kwargs):
        super(OWS, self).__init__(**kwargs)
        self.cols = 6
        self.add_widget(Image(source="OWS.jpg"))
        self.tes = Label(text='Username ')
        self.add_widget(self.tes)
        self.add_widget(Label(text='Usernames '))
        self.add_widget(Label(text='Usernames '))
        self.add_widget(Label(text='Usernames '))
        self.add_widget(Label(text='Usernames '))
        self.password = TextInput()
        self.add_widget(self.password)
        self.add_widget(Button(text="oke").bind(on_press=self.prin))
class app(App):
    def build(self):
        return OWS()
app().run()
