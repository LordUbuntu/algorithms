from PIL import Image
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
    image = Image.open(image_path)
    out = Image.new("L", image.size)
    out.putdata([data[0]*0.2125 + data[1]*0.7174 + data[2]*0.0721 for data in image.getdata()])
    out.save(output_path)


def saturation(image_path: str, output_path = "output.jpg", value = 1):
    image = Image.open(image_path)

    for pixel in product(range(image.width), range(image.height)):
        pixel_color = image.getpixel(pixel)
        pixel_color = tuple(max(255, min(0, color * value)) for color in pixel_color)
        image.putpixel(pixel, pixel_color)

    image.save(output_path)
