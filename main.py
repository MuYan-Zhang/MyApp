from re import MULTILINE
import kivy
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# MyGrid is the root widget, refer to its attributes and methods using the word "root"
class MyGrid(Widget):

    # Variable initializes as None because no obj property until kv file is read
    f_name = ObjectProperty(None)
    l_name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def btn(self):
        print("Welcome, {} {}. We have your email as: {}".format(self.f_name.text, self.l_name.text, self.email.text))

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()