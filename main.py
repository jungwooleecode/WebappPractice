from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty


class WidgetsExample(GridLayout):
    
    count=1
    my_text= StringProperty("1")

    def on_button_click(self):
        print("button clicked")
        self.count +=1
        self.my_text= str(self.count)


    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state=="normal":
            widget.text="OFF"
        else:
            widget.text="ON"


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(0,100):

            b=Button(text=str(i+1), size_hint=(None, None), size=(100,100))
            self.add_widget(b)

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass

"""   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"

        b1=Button(text="A")
        b2=Button(text="B")
        b3=Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()