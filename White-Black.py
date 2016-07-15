#coding: utf-8

from PIL import Image as ImagePIL
from PIL import ImageDraw as ImageDrawPIL
from operator import itemgetter
import math
import hashlib
from pytesser import *

def black_white_jpg( image ):
    width = image.size[0] #Определяем ширину.
    height = image.size[1] #Определяем высоту.
    pix = image.load() #Выгружаем значения пикселей.
    draw = ImageDrawPIL.Draw(image) #Создаем инструмент для рисования.

    for i in range( width ):
        for j in range( height ):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if ( S > ((( 255 + 100 ) // 2 ) * 3 )):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point(( i, j ), ( a, b, c ))
    image.save("test.jpg", "JPEG")
    del draw

def transform_image(image_open, image_save):
    image = ImagePIL.open(image_open) #Открываем изображение.

    # -------------------------------------------- Преобразуем картинку в черно белый цвет и увеличиваем контрастность
    width, height = image.size # получили размер изображения
    white = 200

    for x in range(width):
        for y in range(height):
            pix = image.getpixel((x,y))

            if pix[0] > white and pix[1] > white and pix[2] > white:
                image.putpixel(( x, y ), ( 255, 255, 255 )) # Изменяем цвет пикселя
            else:
                image.putpixel(( x, y ), ( 0, 0, 0 )) # Изменяем цвет пикселя
    image.save( image_save )


def enclose_symbols( image_open, image_save ): #обносим символы рамкой
    image = ImagePIL.open( image_open ) #открываем изображение.
    width, height = image.size # получили размер изображения

    for y in range( height ):
        black_pixel = True
        numper_black_pixel = 0
        current_line = True # текущая строчка

        for x in range( width ):
            pix = image.getpixel(( x,y ))

            if pix == (0, 0, 0):
                black_pixel = False
                numper_black_pixel += 1

            if  pix == (0, 0, 0) and current_line == True:
                current_line = False

            if x == width - 1 and ( black_pixel == True or numper_black_pixel < 5 ):
                for col in range( x ):
                    image.putpixel(( col, y ), ( 125, 0, 125 )) # Изменяем цвет пикселя


    for x in range( width ):
        white_pixel = False
        black_pixel = False

        number_white_pixel = 0
        number_black_pixel = 0

        for y in range( height ):
            pix = image.getpixel(( x,y ))

            if pix == (255, 255, 255 ):
                white_pixel = True
                number_white_pixel += 1


            if pix == (0, 0, 0):
                black_pixel = True
                number_black_pixel += 1


            if pix == (125, 0, 125) and white_pixel == True and ( black_pixel == False or number_black_pixel == 0 ):
                for col in range( number_white_pixel + 1 ):
                    image.putpixel(( x, y-col ), ( 125, 0, 125 )) # Изменяем цвет пикселя
                white_pixel = False
                number_black_pixel = 0


            if pix == (125, 0, 125):
                white_pixel = False
                black_pixel = False

                number_white_pixel = 0
                number_black_pixel = 0

    image.save(image_save)


def get_size_symbols(image_open):
    image = ImagePIL.open( image_open ) #открываем изображение.
    width, height = image.size # получили размер изображения

    list_height_x = {} # в словаре ширина всех знаков и их кол-во
    list_height_y = {} # словарь высот всех знаков

    list_height_x_list = [] # в словаре ширина всех знаков и их кол-во
    list_height_y_list = [] # словарь высот всех знаков

    height_x = 0
    height_y = 0

    for x in range( width ):
        for y in range( height ):
            pix = image.getpixel(( x,y ))

            if pix == (255, 255, 255 ):
                height_y += 1

            if pix == (0, 0, 0):
                height_y += 1

            if pix == (125, 0, 125) :
                if height_y > 4:
                    # if height_y  in list_height_y.keys():
                    #     list_height_y[height_y] += 1
                    #     height_y = 0
                    # else:
                    #     list_height_y[height_y] = 1

                    if height_y not in list_height_y_list:
                        list_height_y_list.append( height_y )
                        height_y = 0
                    else:
                        height_y = 0

                else:
                    height_y = 0

    for y in range( height ):
        for x in range( width ):
            pix = image.getpixel(( x,y ))

            if pix == (255, 255, 255 ):
                height_x += 1

            if pix == (0, 0, 0):
                height_x += 1

            if pix == (125, 0, 125) :
                if height_x > 4:
                    # if height_x  in list_height_x.keys():
                    #     list_height_x[ height_x ] += 1
                    #     height_x = 0
                    # else:
                    #     list_height_x[ height_x ] = 1

                    if height_x not in list_height_x_list:
                        list_height_x_list.append( height_x )
                        height_x = 0
                    else:
                        height_x = 0
                else:
                    height_x = 0

    return list_height_x_list, list_height_y_list

if __name__ == '__main__':

    transform_image( '3.jpg', 'test.png' )
    enclose_symbols( 'test.png', 'test2.png' )
    print(u'ширина = ', get_size_symbols('test2.png')[0], 'высота = ', get_size_symbols('test2.png')[1])

    # text = image_to_string(image)
    # text = image_file_to_string(image_file)
    # text = image_file_to_string(image_file, graceful_errors=True)
    # print "=====output=======\n"
    # print text



