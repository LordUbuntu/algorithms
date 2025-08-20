from PIL import Image, ImageEnhance


def saturation(image_path: str, output_path = "output.jpg", value = 1):
    image = Image.open(image_path)
    out = ImageEnhance.Color(image).enhance(value)
    out.save(output_path)


# greyscale color filter
def grey(image_path: str, output_path = "output.jpg"):
    saturation(image_path, output_path, value = 0)
