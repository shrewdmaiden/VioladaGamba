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
from kivy.config import Config
from functools import partial

import random

class Button(Button):
    pass

class Image(Image):
    pass

class String(Widget):
    r = NumericProperty(255)
    g = NumericProperty(255)
    b = NumericProperty(255)
    def __init__(self,startx,starty,endx,endy, name):
        super(String, self).__init__()
        self.name = name
        self.startx = startx
        self.endx = endx
        self.starty = starty
        self.endy = endy
        with self.canvas:
            self.line = Line(points=(self.startx,self.starty,self.endx,self.endy),width=2)

class Fret(Widget):
    r = NumericProperty(255)
    g = NumericProperty(255)
    b = NumericProperty(255)
    def __init__(self,startx,starty,endx,endy, name):
        super(Fret, self).__init__()
        self.name = name
        self.startx = startx
        self.endx = endx
        self.starty = starty
        self.endy = endy
        with self.canvas:
            self.line = Line(points=(self.startx,self.starty,self.endx,self.endy),width=2)

class Game(FloatLayout):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.viol = Image(source="Violcropped.png",allow_stretch=True)
        self.viol.size = Window.size
        self.add_widget(self.viol)
        self.image_width = self.viol.get_norm_image_size()[0]
        self.image_height = self.viol.get_norm_image_size()[1]
        self.image_left = Window.size[0]/2 - self.image_width/2
        self.image_bottom = Window.size[1]/2 - self.image_height/2

        self.string_pos = {"D": [.188,.078,.218,.745],
                           "G": [.21,.078,.235,.745],
                           "C": [.243,.078,.247,.745],
                           "E": [.276,.078,.265,.745],
                           "A": [.3,.078,.28,.745],
                           "D1": [.329,.078,.29,.745]}

        self.fret_pos = {0: [.2,.745,.305,.745],
                         1: [.195,.72,.309,.72],
                         2: [.195,.69,.315,.69],
                         3: [.192,.66,.316,.66],
                         4: [.19,.63,.319,.63],
                         5: [.189,.6,.322,.6],
                         6: [.186,.57,.325,.57],
                         7: [.183,.54,.327,.54]}

        self.string_list = ["D","G","C","E","A","D1"]
        self.fret_list = [0,1,2,3,4,5,6,7]
        self.note_names = ["A","Bb","B","C","C#","D","D#/Eb","E","F","F#","G","G#/Ab"]
        self.notes = {}

        for key in self.fret_pos:
            self.add_widget(Fret(self.image_left+self.image_width*self.fret_pos[key][0],self.image_bottom+self.image_height*self.fret_pos[key][1],self.image_left+self.image_width*self.fret_pos[key][2],self.image_bottom+self.image_height*self.fret_pos[key][3],key))

        for key in self.string_pos:
            self.add_widget(String(self.image_left+self.string_pos[key][0]*self.image_width,self.image_bottom+self.image_height*self.string_pos[key][1],self.image_left+self.string_pos[key][2]*self.image_width,self.image_bottom+self.image_height*self.string_pos[key][3],key))

        '''for child in self.children:
            if child.__class__.__name__ == "Fret":
                if child.name == 0:
                    child.r = 0
                    child.g = 0
                    child.b = 0'''



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
        self.answer = self.notes[(self.string_choice,self.fret_choice)]

        self.choices = [self.answer]
        counter = 0
        while counter < 3:
            note = random.choice(self.note_names)
            if note != self.answer and note not in self.choices:
                self.choices.append(note)
                counter += 1
        random.shuffle(self.choices)

        self.answer_label = Label()
        self.add_widget(self.answer_label)

        self.button1 = Button(text=self.choices[0], pos_hint={"x":.75,"y":.65}, size_hint = (.2, .1))
        self.button1.bind(on_release=self.choose_answer, on_press=self.respond)
        self.button2 = Button(text=self.choices[1], pos_hint={"x":.75,"y":.5}, size_hint = (.2, .1))
        self.button2.bind(on_release=self.choose_answer, on_press=self.respond)
        self.button3 = Button(text=self.choices[2], pos_hint={"x":.75,"y":.35}, size_hint = (.2, .1))
        self.button3.bind(on_release=self.choose_answer, on_press=self.respond)
        self.button4 = Button(text=self.choices[3], pos_hint={"x":.75,"y":.2}, size_hint = (.2, .1))
        self.button4.bind(on_release=self.choose_answer, on_press=self.respond)
        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.add_widget(self.button3)
        self.add_widget(self.button4)

        self.choose_answer(None)

    def respond(self,instance):
        if instance.text == self.answer:
            self.answer_label.text = "Correct"
            self.choose_answer("correct")
        else:
            self.answer_label.text = "The correct\nanswer is \n" + self.answer + "."
            Clock.schedule_once(partial(self.choose_answer, "wrong"),2)

    def choose_answer(self, answer2, *ignore):
        def reset_text(*args):
            self.answer_label.text = ""

        if answer2 == "correct":
            Clock.schedule_once(reset_text, 2)
        elif answer2 == "wrong":
            reset_text()

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
                child.r = 255
                child.g = 255
                child.b = 255
                if child.name == 0:
                    child.r = 0
                    child.g = 0
                    child.b = 0
                elif child.name != 1:
                    child.r = 255
                    child.g = 255
                    child.b = 255
                if child.name == self.string_choice or child.name == self.fret_choice:
                    child.g = 0
                    child.b = 0

        counter = 0
        for child in self.children:
            if child.__class__.__name__ == "Button":
                child.text = self.choices[counter]
                counter += 1

class main(App):
    def build(self):
        Window.clearcolor = (.45,.45,.45,1)
        return Game()

if __name__ == '__main__':
    main().run()
