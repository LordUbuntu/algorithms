from PIL import Image, ImageEnhance
from itertools import product


# filter out all colours that fall below a given colour
def filter(filter_color, image_path, output_path = "output.jpg"):
    image = Image.open(image_path)

    for pixel in product(range(image.width), range(image.height)):
        pixel_color = image.getpixel(pixel)
        color = tuple(
            0
            if color < filter
            else color
            for color, filter in zip(pixel_color, filter_color)
        )
        image.putpixel(pixel, color)
    image.save(output_path)
