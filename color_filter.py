from PIL import Image, ImageEnhance
from itertools import product, repeat


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


# invert image colours
def invert(image_path: str, output_path = "output.jpg"):
    image = Image.open(image_path)

    for pixel in product(range(image.width), range(image.height)):
        pixel_color = image.getpixel(pixel)
        pixel_color = tuple(256 - color for color in pixel_color)
        image.putpixel(pixel, pixel_color)

    image.save(output_path)


# greyscale color filter
def grey(image_path: str, output_path = "output.jpg"):
    saturation(image_path, output_path, value = 0)


def saturation(image_path: str, output_path = "output.jpg", value = 1):
    image = Image.open(image_path)
    out = ImageEnhance.Color(image).enhance(value)
    out.save(output_path)


def mutate(image_path: str, output_path = "output.jpg", color = (0, 0, 0)):
    image = Image.open(image_path)

    for pixel in product(range(image.width), range(image.height)):
        old_color = image.getpixel(pixel)
        new_color = (old_color[0] + color[0], old_color[1] + color[1], old_color[2] + color[2])
        image.putpixel(pixel, new_color)

    image.save(output_path)


