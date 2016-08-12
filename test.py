from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.scatterlayout import ScatterLayout

class Menu(Screen):
    pass

class Game(Screen):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.s = ScatterLayout(do_rotation=False)
        self.f = FloatLayout()
        self.image = Image(source='Violnobackground.png')
        self.s.add_widget(self.image)
        self.f.add_widget(self.s)
        self.add_widget(self.f)

class TutorialApp(App):
    def build(self):
        Window.clearcolor = (.47,.47,.47,1)
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Game(name='game'))
        return sm

if __name__ == "__main__":
    TutorialApp().run()