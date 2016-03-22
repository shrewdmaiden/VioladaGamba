__author__ = 'gregory'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import NumericProperty

import random

'''class Sprite(Image):
    def __init__(self,**kwargs):
        super(Sprite,self).__init__(**kwargs)
        self.size = self.texture_size

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
            Line(points=(self.x, self.y, self.x+self.width, self.y + self.height))

    def highlight(self):
        with self.canvas:
            Color(255, 0, 0, mode='rgb')
            Line(points=(self.x, self.y, self.x+self.width, self.y + self.height))

    def clear(self):
        with self.canvas:
            Color(255,255,255, mode='rgb')
            Line(points=(self.x, self.y, self.x+self.width, self.y + self.height))


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

class Game(FloatLayout):
    def __init__(self):
        super(Game, self).__init__()

        self.string_pos = {"D": [150, 10, 150, 500],
                           "A": [100, 10, 100, 500]}

        self.fret_pos = {0: [100, 500, 150, 500],
                         1: [100, 450, 150, 450]}

        self.string_list = []
        self.fret_list = []
        self.note_names = ["A","Bb","B","C","C#","D","D#/Eb","E","F","F#","G","G#/Ab"]
        self.notes = {}

        for key in self.string_pos:
            self.string_list.append(key)

        for key in self.fret_pos:
            self.fret_list.append(key)

        for string in self.string_list:
            start_note = 0
            if string == "D":
                start_note = 5
            elif string == "A":
                start_note = 0
            elif string == "E":
                start_note = 7
            elif string == "C":
                start_note = 3
            elif string == "G":
                start_note = 10
            elif string == "D1":
                start_note = 5

            for fret in self.fret_list:
                self.notes[(string, fret)] = self.note_names[start_note]
                if start_note < 11:
                    start_note += 1
                else:
                    start_note = 0
        self.string_choice = random.choice(self.string_list)
        self.fret_choice = random.choice(self.fret_list)
        self.answer = self.notes[(self.string_choice, self.fret_choice)]

        self.choices = [self.answer]
        counter = 0
        while counter < 3:
            note = random.choice(self.note_names)
            if note != self.answer and note not in self.choices:
                self.choices.append(note)
                counter += 1
        random.shuffle(self.choices)

        self.background = Sprite(source='Violcropped.png')
        Window.size = self.background.size
        self.add_widget(self.background)

        for key in self.string_pos:
            self.add_widget(String(self.string_pos[key][0],self.string_pos[key][1],self.string_pos[key][2],self.string_pos[key][3],key))

        for key in self.fret_pos:
            self.add_widget(Fret(self.fret_pos[key][0],self.fret_pos[key][1],self.fret_pos[key][2],self.fret_pos[key][3],key))

        self.answer_label = Label()
        self.add_widget(self.answer_label)

        self.button1 = Button(text=self.choices[0], font_size=15, pos_hint={"x":.75,"y":.65}, size_hint = (.15, .1))
        self.button1.bind(on_release=self.choose_answer, on_press=self.respond)
        self.button2 = Button(text=self.choices[1], font_size=15, pos_hint={"x":.75,"y":.5}, size_hint = (.15, .1))
        self.button2.bind(on_release=self.choose_answer, on_press=self.respond)
        self.button3 = Button(text=self.choices[2], font_size=15, pos_hint={"x":.75,"y":.35}, size_hint = (.15, .1))
        self.button3.bind(on_release=self.choose_answer, on_press=self.respond)
        self.button4 = Button(text=self.choices[3], font_size=15, pos_hint={"x":.75,"y":.2}, size_hint = (.15, .1))
        self.button4.bind(on_release=self.choose_answer, on_press=self.respond)

        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.add_widget(self.button3)
        self.add_widget(self.button4)



        self.choose_answer()

    def respond(self,instance):
        if instance.text == self.answer:
            self.answer_label.text = "Correct"
        else:
            self.answer_label.text = "Wrong"
        def reset_text(*args):
            self.answer_label.text = ""

        Clock.schedule_once(reset_text, 2)

    def choose_answer(self,*ignore):
        self.string_choice = random.choice(self.string_list)
        self.fret_choice = random.choice(self.fret_list)
        self.answer = self.notes[(self.string_choice, self.fret_choice)]
        self.choices = [self.answer]
        counter = 0
        while counter < 3:
            note = random.choice(self.note_names)
            if note != self.answer and note not in self.choices:
                self.choices.append(note)
                counter += 1
        random.shuffle(self.choices)

        for child in self.children:
            if child.__class__.__name__ == "Fret" or child.__class__.__name__ == "String":
                child.clear()
                if child.name == self.string_choice or child.name == self.fret_choice:
                    child.highlight()
        counter = 0
        for child in self.children:
            if child.__class__.__name__ == "Button":
                child.text = self.choices[counter]
                counter += 1'''
class Sprite(Image):
    def __init__(self,**kwargs):
        super(Sprite,self).__init__(**kwargs)
        self.size = self.texture_size

class String(Widget):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)
    sx = NumericProperty(0)
    sy = NumericProperty(0)
    ex = NumericProperty(0)
    ey = NumericProperty(0)
    def __init__(self, **kwargs):
        super(String, self).__init__(**kwargs)
        self.r = 1
        self.g = 1
        self.b = 1
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0


        with self.canvas:
            self.line = Line()


class Viol(FloatLayout):
    def __init__(self, **kwargs):
        super(Viol, self).__init__(**kwargs)
        self.astring = String(pos_hint={"x":.3},size_hint=(1,1))
        self.astring.sy = 1
        self.astring.sx = 1
        self.astring.ex = -1.5
        self.astring.ey = -1
        self.dstring = String(pos_hint={"x":.25},size_hint=(1,1))
        self.dstring.sy = 1
        self.dstring.sx = 1
        self.dstring.ex = -.3
        self.dstring.ey = -1
        self.estring = String(pos_hint={"x":.2},size_hint=(1,1))
        self.estring.sy = 1
        self.estring.sx = 1
        self.estring.ex = .3
        self.estring.ey = -1
        self.cstring = String(pos_hint={"x":.15},size_hint=(1,1))
        self.add_widget(self.astring)
        self.add_widget(self.dstring)
        self.add_widget(self.estring)



class VioladaGamba(App):
    def build(self):
        return Viol()


if __name__ == '__main__':
    VioladaGamba().run()
