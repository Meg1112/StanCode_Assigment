"""
File: blur.py
Name:Meg
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:SimpleImage, the image would be blurred
    :return:SimpleImage, the blurred image
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(x, y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                around_pixel_1 = img.get_pixel(x + 1, y)
                around_pixel_2 = img.get_pixel(x + 1, y + 1)
                around_pixel_3 = img.get_pixel(x, y + 1)

                new_pixel.red = (around_pixel_1.red+around_pixel_2.red+around_pixel_3.red+img_pixel.red)//4
                new_pixel.green = (around_pixel_1.green+around_pixel_2.green+around_pixel_3.green+img_pixel.green)//4
                new_pixel.blue = (around_pixel_1.blue+around_pixel_2.blue+around_pixel_3.blue+img_pixel.blue)//4

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                around_pixel_3 = img.get_pixel(x, y + 1)
                around_pixel_4 = img.get_pixel(x - 1, y)
                around_pixel_5 = img.get_pixel(x - 1, y + 1)

                new_pixel.red = (around_pixel_4.red+around_pixel_5.red+around_pixel_3.red+img_pixel.red)//4
                new_pixel.green = (around_pixel_4.green+around_pixel_5.green+around_pixel_3.green+img_pixel.green)//4
                new_pixel.blue = (around_pixel_4.blue+around_pixel_5.blue+around_pixel_3.blue+img_pixel.blue)//4

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                around_pixel_1 = img.get_pixel(x + 1, y)
                around_pixel_6 = img.get_pixel(x + 1, y - 1)
                around_pixel_7 = img.get_pixel(x, y - 1)

                new_pixel.red = (around_pixel_1.red+around_pixel_6.red+around_pixel_7.red+img_pixel.red)//4
                new_pixel.green = (around_pixel_1.green+around_pixel_6.green+around_pixel_7.green+img_pixel.green)//4
                new_pixel.blue = (around_pixel_1.blue+around_pixel_6.blue+around_pixel_7.blue+img_pixel.blue)//4

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                around_pixel_4 = img.get_pixel(x - 1, y)
                around_pixel_7 = img.get_pixel(x, y - 1)
                around_pixel_8 = img.get_pixel(x - 1, y - 1)

                new_pixel.red = (around_pixel_4.red+around_pixel_8.red+around_pixel_7.red+img_pixel.red)//4
                new_pixel.green = (around_pixel_4.green+around_pixel_8.green+around_pixel_7.green+img_pixel.green)//4
                new_pixel.blue = (around_pixel_4.blue+around_pixel_8.blue+around_pixel_7.blue+img_pixel.blue)//4

            elif 0 < x < img.width - 1 and y == 0:
                # Get top edge's pixels (without two corners)
                around_pixel_1 = img.get_pixel(x + 1, y)
                around_pixel_2 = img.get_pixel(x + 1, y + 1)
                around_pixel_3 = img.get_pixel(x, y + 1)
                around_pixel_4 = img.get_pixel(x - 1, y)
                around_pixel_5 = img.get_pixel(x - 1, y + 1)

                new_pixel.red = (around_pixel_4.red+around_pixel_5.red+around_pixel_3.red
                                 + around_pixel_2.red+around_pixel_1.red+img_pixel.red)//6
                new_pixel.green = (around_pixel_4.green+around_pixel_5.green+around_pixel_3.green
                                   + around_pixel_2.green+around_pixel_1.green+img_pixel.green)//6
                new_pixel.blue = (around_pixel_4.blue+around_pixel_5.blue+around_pixel_3.blue
                                  + around_pixel_2.blue+around_pixel_1.blue+img_pixel.blue)//6

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                around_pixel_1 = img.get_pixel(x + 1, y)
                around_pixel_4 = img.get_pixel(x - 1, y)
                around_pixel_6 = img.get_pixel(x + 1, y - 1)
                around_pixel_7 = img.get_pixel(x, y - 1)
                around_pixel_8 = img.get_pixel(x - 1, y - 1)

                new_pixel.red = (around_pixel_4.red+around_pixel_8.red+around_pixel_7.red
                                 + around_pixel_6.red+around_pixel_1.red+img_pixel.red)//6
                new_pixel.green = (around_pixel_4.green+around_pixel_8.green+around_pixel_7.green
                                   + around_pixel_6.green+around_pixel_1.green+img_pixel.green)//6
                new_pixel.blue = (around_pixel_4.blue+around_pixel_8.blue+around_pixel_7.blue
                                  + around_pixel_6.blue+around_pixel_1.blue+img_pixel.blue)//6

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                around_pixel_1 = img.get_pixel(x + 1, y)
                around_pixel_2 = img.get_pixel(x + 1, y + 1)
                around_pixel_3 = img.get_pixel(x, y + 1)
                around_pixel_6 = img.get_pixel(x + 1, y - 1)
                around_pixel_7 = img.get_pixel(x, y - 1)

                new_pixel.red = (around_pixel_7.red+around_pixel_6.red+around_pixel_1.red
                                 + around_pixel_2.red+around_pixel_3.red+img_pixel.red)//6
                new_pixel.green = (around_pixel_7.green+around_pixel_6.green+around_pixel_1.green
                                   + around_pixel_2.green+around_pixel_3.green+img_pixel.green)//6
                new_pixel.blue = (around_pixel_7.blue+around_pixel_6.blue+around_pixel_1.blue
                                  + around_pixel_2.blue+around_pixel_3.blue+img_pixel.blue)//6

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                around_pixel_3 = img.get_pixel(x, y + 1)
                around_pixel_4 = img.get_pixel(x - 1, y)
                around_pixel_5 = img.get_pixel(x - 1, y + 1)
                around_pixel_7 = img.get_pixel(x, y - 1)
                around_pixel_8 = img.get_pixel(x - 1, y - 1)

                new_pixel.red = (around_pixel_7.red + around_pixel_8.red + around_pixel_4.red
                                 + around_pixel_5.red + around_pixel_3.red + img_pixel.red) // 6
                new_pixel.green = (around_pixel_7.green + around_pixel_8.green + around_pixel_4.green
                                   + around_pixel_5.green + around_pixel_3.green + img_pixel.green) // 6
                new_pixel.blue = (around_pixel_7.blue + around_pixel_8.blue + around_pixel_4.blue
                                  + around_pixel_5.blue + around_pixel_3.blue + img_pixel.blue) // 6

            else:
                # Inner pixels.
                around_pixel_1 = img.get_pixel(x + 1, y)
                around_pixel_2 = img.get_pixel(x + 1, y + 1)
                around_pixel_3 = img.get_pixel(x, y + 1)
                around_pixel_4 = img.get_pixel(x - 1, y)
                around_pixel_5 = img.get_pixel(x - 1, y + 1)
                around_pixel_6 = img.get_pixel(x + 1, y - 1)
                around_pixel_7 = img.get_pixel(x, y - 1)
                around_pixel_8 = img.get_pixel(x - 1, y - 1)

                new_pixel.red = (around_pixel_1.red + around_pixel_2.red + around_pixel_3.red + around_pixel_4.red
                                 + around_pixel_5.red + around_pixel_6.red + around_pixel_7.red
                                 + around_pixel_8.red + img_pixel.red) // 9
                new_pixel.green = (around_pixel_1.green + around_pixel_2.green + around_pixel_3.green
                                   + around_pixel_4.green + around_pixel_5.green + around_pixel_6.green
                                   + around_pixel_7.green + around_pixel_8.green + img_pixel.green) // 9
                new_pixel.blue = (around_pixel_1.blue + around_pixel_2.blue + around_pixel_3.blue + around_pixel_4.blue
                                  + around_pixel_5.blue + around_pixel_6.blue + around_pixel_7.blue
                                  + around_pixel_8.blue + img_pixel.blue) // 9

    return new_img


def main():
    """
    Make image be blurred and can change blur times.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
