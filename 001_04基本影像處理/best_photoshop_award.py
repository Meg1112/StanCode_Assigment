"""
File: best_photoshop_award.py
Name:
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
THRESHOLD = 1.13
BLACK_PIXEL = 120


def main():
    """
    創作理念：想成為霍格華滋的學生，首先就必須先擁有一枝屬於自己的魔杖，因此我來到英國最好的魔杖商店，
    奥利凡德(Ollivanders Wand Shop)找到我的魔杖了。
    """
    fg = SimpleImage('image_contest/meg_1.jpeg')
    bg = SimpleImage('image_contest/wand_shop.jpeg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(bg, fg):
    """
    : param1 bg: SimpleImage, the background image
    : param2 fg: SimpleImage, green screen figure image
    : return fg: SimpleImage, the green screen pixels are replaced by pixels of background image
    """

    for y in range(bg.height):
        for x in range(bg.width):
            pixel_fg = fg.get_pixel(x, y)
            avg = (pixel_fg.red + pixel_fg.blue + pixel_fg.green) // 3
            total = pixel_fg.red + pixel_fg.blue + pixel_fg.green
            if pixel_fg.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_fg.red = pixel_bg.red
                pixel_fg.blue = pixel_bg.blue
                pixel_fg.green = pixel_bg.green
    return fg


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
