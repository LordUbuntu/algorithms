# Jacobus Burger (2022)
# Box Blur
#   I was helping some students understand the algorithm behind a box
#   blur. I realized that writing a script to blur images would be
#   a fun project. So here is my attempt at it.
from PIL import Image


def box_blur(kernel_size: int, image_path: str):
    # open image file
    image = Image.open(image_path)

    # determine middle of box
    middle = kernel_size // 2

    # iterate box in bounds of image
    for i in range(middle, image.width - middle, middle):
        for j in range(middle, image.height - middle, middle):

            # get pixels in box
            #   done by getting indices of pixels relative to middle pixel
            #   eg: pretending middle = (0, 0), upper left = (-1, -1)
            box = [
                    image.getpixel((i + x, j + y))
                    for x in range(-middle, kernel_size - middle)
                    for y in range(-middle, kernel_size - middle)
            ]

            # get average of all pixel (red, green, blue) in box
            average = (
                    sum([color[0] for color in box]) // len(box),  # red
                    sum([color[1] for color in box]) // len(box),  # green
                    sum([color[2] for color in box]) // len(box)   # blue
            )

            # set all pixels in box to average colour
            for x in range(-middle, kernel_size - middle):
                for y in range(-middle, kernel_size - middle):
                    image.putpixel((i + x, j + y), average)

    # save to new image
    image.save("output.jpg")
