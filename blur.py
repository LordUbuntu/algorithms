# Jacobus Burger (2022)
# Info
#   Various image blur algorithms in Python
from PIL import Image
from itertools import product, repeat


# Box Blur
#   I was helping some students understand the algorithm behind a box
#   blur. I realized that writing a script to blur images would be
#   a fun project. So here is my attempt at it.
# Explanation
#   The basic process here is to treat every pixel in the image like a
#   tile on a grid. Next, we imagine an NxN box (kernel) by tracking
#   the position of it's imagined middle. We then set all the pixels
#   inside the imagined box to the average of all the pixels in the
#   box, and we then move over to the next position of the box.
#   We move the imagined middle over by increments of half the width
#   of the box, and we go down rows by half the height of the box.
#   Once iteration is done, we've blurred the image.
# More Info
#   https://en.wikipedia.org/wiki/Box_blur
def box_blur(kernel_size: int, image_path: str):
    # open image file
    image = Image.open(image_path)

    # determine middle of box
    middle = kernel_size // 2

    # iterate box in bounds of image
    for i in range(middle, image.width - middle, middle):
        for j in range(middle, image.height - middle, middle):

            # iterate over range of pixels inside box kernel
            box_kernel = range(-middle, kernel_size - middle)

            # get pixels in box
            #   done by getting indices of pixels relative to middle pixel
            #   eg: pretending middle = (0, 0), then upper left = (-1, -1)
            box = [
                    image.getpixel((i + x, j + y))
                    for x, y in product(*repeat(box_kernel, 2))
            ]

            # get average of all pixel (red, green, blue) in box
            average = (
                    sum([color[0] for color in box]) // len(box),  # red
                    sum([color[1] for color in box]) // len(box),  # green
                    sum([color[2] for color in box]) // len(box)   # blue
            )

            # set all pixels in box to average colour
            for x, y in product(*repeat(box_kernel, 2)):
                image.putpixel((i + x, j + y), average)

    # save to new image
    image.save("output.jpg")


# n-pass box-blur
