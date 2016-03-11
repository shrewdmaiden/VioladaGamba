__author__ = 'gregory'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.button import Button
import random

class String(Widget):
    def __init__(self, startx, starty, endx, endy, name):
        super(String, self).__init__()
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.name = name
        with self.canvas:
            Color(255, 255, 255, mode='rgb')
            Line(points=(self.startx, self.starty, self.endx, self.endy))

    def highlight(self):
        with self.canvas:
            Color(255, 0, 0, mode='rgb')
            Line(points=(self.startx, self.starty, self.endx, self.endy))

    def clear(self):
        with self.canvas:
            Color(255,255,255, mode='rgb')
            Line(points=(self.startx, self.starty, self.endx, self.endy))


class Fret(Widget):
    def __init__(self, startx, starty, endx, endy, name):
        super(Fret, self).__init__()
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.name = name
        with self.canvas:
            Color(255, 255, 255, mode='rgb')
            Line(points=(self.startx, self.starty, self.endx, self.endy))

    def highlight(self):
        with self.canvas:
            Color(255, 0, 0, mode='rgb')
            Line(points=(self.startx, self.starty, self.endx, self.endy))

    def clear(self):
        with self.canvas:
            Color(255,255,255, mode='rgb')
            Line(points=(self.startx, self.starty, self.endx, self.endy))

class Button(Button):
    pass

class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()

        self.string_pos = {"D": [100, 10, 100, 500],
                           "A": [150, 10, 150, 500]}

        self.fret_pos = {"open": [100, 500, 150, 500],
                         "First": [100, 450, 150, 450]}

        self.string_list = []
        self.fret_list = []

        for key in self.string_pos:
            self.string_list.append(key)

        for key in self.fret_pos:
            self.fret_list.append(key)

        self.string_choice = "A"
        self.fret_choice = "open"

        for key in self.string_pos:
            self.add_widget(String(self.string_pos[key][0],self.string_pos[key][1],self.string_pos[key][2],self.string_pos[key][3],key))

        for key in self.fret_pos:
            self.add_widget(Fret(self.fret_pos[key][0],self.fret_pos[key][1],self.fret_pos[key][2],self.fret_pos[key][3],key))


        self.button1 = Button(text = "A",font_size = 15,pos=(300,500),size = (50,50))
        self.button1.bind(on_press=self.choose_answer)
        self.button2 = Button(text = "Bb",font_size = 15,pos=(300,440),size = (50,50))
        self.button2.bind(on_press=self.choose_answer)
        self.button3 = Button(text = "Eb",font_size = 15,pos=(300,315),size = (50,50))
        self.button3.bind(on_press=self.choose_answer)
        self.button4 = Button(text = "D",font_size = 15,pos=(300,200),size = (50,50))
        self.button4.bind(on_press=self.choose_answer)

        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.add_widget(self.button3)
        self.add_widget(self.button4)

        self.choose_answer()

    def choose_answer(self,*ignore):
        self.string_choice = random.choice(self.string_list)
        self.fret_choice = random.choice(self.fret_list)

        for child in self.children:
            if child.__class__.__name__ == "Fret" or child.__class__.__name__ == "String":
                child.clear()
                if child.name == self.string_choice or child.name == self.fret_choice:
                    child.highlight()


class VioladaGamba(App):
    def build(self):
        return Game()


if __name__ == '__main__':
    VioladaGamba().run()
