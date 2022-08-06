from kivy.app import App
from kivy.properties import BooleanProperty, StringProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color





class WidgetsExample(GridLayout):
    
    count=1
    count_enabled= BooleanProperty(False)
    my_text= StringProperty("1")
    slider_value_txt= StringProperty("value")
    text_input_str= StringProperty("Bamm")

    def on_button_click(self):
        print("button clicked")
        self.count +=1
        self.my_text= str(self.count)


    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state=="normal":
            widget.text="OFF"
            self.count_enabled=False
        else:
            widget.text="ON"
            self.count_enabled= True

    def on_switch_active(self, widget):
        print("Switch: "+ str(widget.active))

    # def on_slider_value(self, widget):
    #     print("Slider: "+ str(int(widget.value)))
    #     self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str= widget.text

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

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,200,300,500), width=2)
            Color(0,1,0)
            Line(circle=(100,100,100))
            self.rect= Rectangle(pos=(500,500), size=(300,500))

    def on_button_a_click(self):
        print("foo")
        x, y =self.rect.pos
        w,h= self.rect.size
        inc=100
        diff=self.width-(x+w)

        if diff< inc:
            inc= diff
        x += inc
        self.rect.pos= (x,y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size= 100
        self.vx= 10
        self.vy= 15
        with self.canvas:
            self.ball=Ellipse(pos=self.center, size=(self.ball_size,self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        self.ball.pos=(self.center_x-self.ball_size/2,self.center_y-self.ball_size/2)

    def update(self, dt):
        x, y=self.ball.pos

        x += self.vx
        y += self.vy

        if y+ self.ball_size > self.height:
            y= self.height - self.ball_size
            self.vy= -self.vy

        if x+ self.ball_size>self.width:
            x=self.width-self.ball_size
            self.vx=-self.vx
        if y<0:
            y=0
            self.vy=-self.vy
        if x<0:
            x=0
            self.vx=-self.vx

        self.ball.pos=(x,y)

class CanvasExample6(Widget):
    pass

class CanvasExample7(BoxLayout):
    pass



TheLabApp().run()
