#coding: utf-8

import kivy
kivy.require('1.0.4') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

wimg = Image( source = '1.png' )

class Hello_worldApp( App ): # если поменять начало названия класса, то измениться заголовок приложения

    def build( self ):
        return wimg


if __name__ == '__main__':
    Hello_worldApp().run()