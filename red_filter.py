# Jacobus Burger (2022)
# Takes an image and filters out all colours except red.

from PIL import Image

def redden(image_path: str):
    image = Image.open(image_path)
    
    for i in range(image.width):
        for j in range(image.height):
            red, _, _ = image.getpixel((i, j))
            image.putpixel((i, j), (red, 0, 0))

    image.save("output.jpg")
