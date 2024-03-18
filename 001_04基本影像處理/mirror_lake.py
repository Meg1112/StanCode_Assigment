"""
File: mirror_lake.py
Name:Meg
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:picture which want to be reflected
    :return:mirrored picture
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            b_pixel = b_img.get_pixel(x, y)

            b_pixel.red = img_pixel.red
            b_pixel.green = img_pixel.green
            b_pixel.blue = img_pixel.blue

            b_pixel_2 = b_img.get_pixel(x, b_img.height-1-y)
            b_pixel_2.red = img_pixel.red
            b_pixel_2.green = img_pixel.green
            b_pixel_2.blue = img_pixel.blue
    return b_img


def main():
    """
    Make picture as a vertical mirror picture
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
