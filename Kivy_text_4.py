#coding: utf-8

import kivy
kivy.require('1.0.4') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from PIL import Image as ImagePIL



class Hello_worldApp( App ): # если поменять начало названия класса, то измениться заголовок приложения

    def build( self ):
        return wimg
i = 0
def seven(x,y):
    range_color = [(0,0,0),(2,2,2),(1,1,1),(3,3,3),(0,0,1),]
    global i
    if img.getpixel((x, y)) in range_color:
        i+=1


if __name__ == '__main__':

    img = ImagePIL.open("1.jpg")
    x,y = img.size # получили размер изображения
    img.getpixel((25, 45))              # Получаем цвет пикселя
    print (img.getpixel((25, 45)))

    for a in range(100):
        img.putpixel((a, a), (0,0,0)) # Изменяем цвет пикселя

    img.save("1.jpg")
                    # Просматриваем изображение
    wimg = Image( source = '1.jpg' )
    Hello_worldApp().run()