import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='First Name'))
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)
        self.add_widget(Label(text='Last Name'))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)
        self.add_widget(Label(text='Email'))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)
        self.submit = Button(text='Submit', font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        first = self.first_name.text
        last = self.last_name.text
        email = self.email.text
        print("First Name:", first, "Last Name:", last, "Email:", email)
        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""
        self.first_name.focus = True