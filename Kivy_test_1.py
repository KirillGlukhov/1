#coding: utf-8

import kivy
kivy.require('1.0.4') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class Hello_worldApp(App): # если поменять начало названия класса, то измениться заголовок приложения

    def build(self):
        return Label(text = 'Hello world')


if __name__ == '__main__':
    Hello_worldApp().run()