from PIL import Image, ImageEnhance
from itertools import product


# invert image colours
def invert(image_path: str, output_path = "output.jpg"):
    image = Image.open(image_path)

    for pixel in product(range(image.width), range(image.height)):
        pixel_color = image.getpixel(pixel)
        pixel_color = tuple(256 - color for color in pixel_color)
        image.putpixel(pixel, pixel_color)

    image.save(output_path)
