"""
File: stanCodoshop.py
Name: Meg
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_dis = ((pixel.red-red)**2 + (pixel.green-green)**2 + (pixel.blue-blue)**2)**0.5
    return color_dis


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.
    Input:
        pixels (List[Pixel]): a list of pixels to be averaged
    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    total_r = 0
    total_g = 0
    total_b = 0
    for i in range(len(pixels)):
        total_r += pixels[i].red
        total_g += pixels[i].green
        total_b += pixels[i].blue
    red = total_r//len(pixels)
    green = total_g//len(pixels)
    blue = total_b//len(pixels)
    return [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    smallest_dis = sys.maxsize  # maximum number
    smallest_pix = int
    l_avg = get_average(pixels)
    red_1 = l_avg[0]
    green_1 = l_avg[1]
    blue_1 = l_avg[2]
    for i in range(len(pixels)):
        pix_dis = get_pixel_dist(pixels[i], red_1, green_1, blue_1)
        if pix_dis < smallest_dis:
            smallest_dis = pix_dis
            smallest_pix = pixels[i]
    return smallest_pix


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    pixels = []

    for x in range(width):
        for y in range(height):
            new_pixel = result.get_pixel(x, y)
            # collect same location in each picture
            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                pixels += [pixel]
            # put best pixel at new blank
            best_pixel = get_best_pixel(pixels)
            new_pixel.red = best_pixel.red
            new_pixel.green = best_pixel.green
            new_pixel.blue = best_pixel.blue
            # clean pixels
            pixels = []
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
