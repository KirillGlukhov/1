#coding: utf-8

import kivy
kivy.require('1.0.4') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from PIL import Image as ImagePIL
from operator import itemgetter
import math
import hashlib
import time

class VectorCompare:
  def magnitude(self,concordance):
    total = 0
    for word,count in concordance.iteritems():
      total += count ** 2
    return math.sqrt(total)

  def relation(self,concordance1, concordance2):
    relevance = 0
    topvalue = 0
    for word, count in concordance1.iteritems():
      if concordance2.has_key(word):
        topvalue += count * concordance2[word]
    return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


class Hello_worldApp( App ): # если поменять начало названия класса, то измениться заголовок приложения

    def build( self ):
        return wimg
# i = 0
# def seven(x,y):
#     range_color = [(0,0,0),(2,2,2),(1,1,1),(3,3,3),(0,0,1),]
#     global i
#     if img.getpixel((x, y)) in range_color:
#         i+=1


if __name__ == '__main__':

    # img = ImagePIL.open("1.jpg")
    # x,y = img.size # получили размер изображения
    # for x in range(x):
    #     for y in range(y):
    #         seven(x,y)
    # print('Black pixel = ', i)
    # obj = img.load()
    # img.getpixel((25, 45))              # Получаем цвет пикселя
    # print (img.getpixel((25, 45)))
    #
    # for a in range(100):
    #     img.putpixel((a, 45), (0,0,0)) # Изменяем цвет пикселя
    #
    # #print(img.getpixel((25, 45)))              # Получаем цвет пикселя
    # img.save("1.jpg")
    #                 # Просматриваем изображение
    # wimg = Image( source = '1.jpg' )
    #Hello_worldApp().run()

    im = ImagePIL.open("1.gif")
    im = im.convert("P")

    his = im.histogram()

    values = {}

    for i in range(256):
        values[i] = his[i]

    for color, kol_vo in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
        print ('color - ', color, 'kol_vo - ', kol_vo)

    im2 = ImagePIL.new("P",im.size,255)


    temp = {}

    for x in range(im.size[1]):
      for y in range(im.size[0]):
          pix = im.getpixel((y,x))
          temp[pix] = pix
          if pix == 0 or pix == 255: # these are the numbers to get
                im2.putpixel((y,x),0)

    print('temp = ', temp)
    im2.save("1-1.gif")

    # inletter = False
    # foundletter=False
    # start = 0
    # end = 0
    #
    # letters = []
