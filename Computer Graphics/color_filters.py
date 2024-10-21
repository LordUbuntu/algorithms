from PIL import Image, ImageEnhance
from itertools import product


def mutate(image_path: str, output_path = "output.jpg", color = (0, 0, 0)):
    image = Image.open(image_path)

    for pixel in product(range(image.width), range(image.height)):
        old_color = image.getpixel(pixel)
        new_color = (old_color[0] + color[0], old_color[1] + color[1], old_color[2] + color[2])
        image.putpixel(pixel, new_color)

    image.save(output_path)


def redden(image_path: str, output_path = "output.jpg"):
    image = Image.open(image_path)

    for pixel in product(range(image.width), range(image.height)):
        old_color = image.getpixel(pixel)
        new_color = (max(old_color[1], old_color[2]), 0, 0)
        image.putpixel(pixel, new_color)

    image.save(output_path)
