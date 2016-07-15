#coding: utf-8

from PIL import Image as ImagePIL
from PIL import ImageDraw as ImageDrawPIL
from operator import itemgetter
import math
import hashlib
import random, os, shutil

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


def get_line_symbols( image_open ):
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

            if x == width - 1 and ( black_pixel == True or numper_black_pixel < 3 ):
                for col in range( x ):
                    image.putpixel(( col, y ), ( 125, 0, 125 )) # Изменяем цвет пикселя

    #image.save('1111111.png')
    list_name_part = []

    x = 1
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

        if pix == (125, 0, 125) and white_pixel == True and black_pixel == False and number_white_pixel > 3 :
            white_pixel = False
            number_black_pixel = 0

            name_part = random.randint(1,100000000)
            part_text = image.crop((x, y - number_white_pixel, width, y))
            part_text.save('{}.png'.format(name_part))
            list_name_part.append(name_part)

        if pix == (125, 0, 125):
            white_pixel = False
            black_pixel = False

            number_white_pixel = 0
            number_black_pixel = 0

    return list_name_part


def remove_part_file( list_name_parts ):
    for name in list_name_parts:
        os.remove('{}.png'.format(name))
        shutil.rmtree('{}'.format(name))

def enclose_symbols( list_name_parts ): #обносим символы рамкой
    for name in list_name_parts:
        image_name = '{}.png'.format( name )
        image = ImagePIL.open( image_name ) #открываем изображение.
        width, height = image.size # получили размер изображения

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


                if y == height-1 and white_pixel == True and ( black_pixel == False or number_black_pixel == 0 ):
                    for col in range( height ):
                        image.putpixel(( x, col ), ( 125, 0, 125 )) # Изменяем цвет пикселя
                    white_pixel = False
                    number_black_pixel = 0


                if y == height-1:
                    white_pixel = False
                    black_pixel = False

                    number_white_pixel = 0
                    number_black_pixel = 0

        image.save(image_name)

def get_symbols( list_name_parts ):
    for name in list_name_parts:
        image_name = '{}.png'.format( name )
        image = ImagePIL.open( image_name ) #открываем изображение.
        width, height = image.size # получили размер изображения

        os.mkdir('{}'.format(name))

        y = 0
        count = 0
        count_symbols = 1
        for x in range( width ):
            pix = image.getpixel(( x,y ))

            if pix == (255, 255, 255) or pix == (0, 0, 0):
                count += 1

            if pix == (125, 0, 125) and count != 0:
                if count < 4:
                    count = 0
                else:
                    part_text = image.crop(( x - count, y, x, height ))
                    part_text.save('{}/{}.png'.format( name, count_symbols ))
                    count = 0
                    count_symbols += 1

def transcript_symbols( list_name_parts ):
    open = 0
    for name in list_name_parts:
        count_files_in_string = len(os.listdir('{}'.format( name )))
        for number in range( count_files_in_string ):
            image_name = '{}.png'.format( number + 1 )
            image = ImagePIL.open('{}/{}'.format( name, image_name )) #открываем изображение.
            open +=1
    return open


if __name__ == '__main__':

    transform_image( '3.jpg', 'test.png' )
    list_name_parts = get_line_symbols( 'test.png' )
    enclose_symbols( list_name_parts )
    get_symbols( list_name_parts )
    print(transcript_symbols( list_name_parts ))
    remove_part_file(list_name_parts)
