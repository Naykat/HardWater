#HardWater
from PIL import Image
from Utilities.MathFunctions import calculate_step, calculate_text_length, get_stepx_and_stepy
from Utilities.Utils import *
from os.path import abspath as path

def watermark(filename: str, text: str) -> Image:

    #Exceptions
    if not(type(filename) is str):
        raise TypeError(f"""filename must be str, not {get_type(filename)}""")
    if not(type(text) is str):
        raise TypeError(f"""text must be str, not {get_type(filename)}""")

    image = Image.open(path(filename))
    width, height = image.size
    mark(image)
    
    while calculate_step(text, width, height)>255:
        text+=chr(0)
    step = calculate_step(text, width, height)
    draw_step(image, step)

    current_x = 0
    current_y = 0
    step_x, step_y = get_stepx_and_stepy(width, height, step)

    for symbol in text:
        if ord(symbol)>255:
            raise ValueError(f"Unknown symbol: {symbol}")

        r,g = image.getpixel((current_x, current_y))[:2]
        image.putpixel((current_x, current_y),(r,g,ord(symbol)))

        current_x += step_x
        current_y += step_y

    return image


def reveal(filename: str or Image) -> str:

    #Exceptions
    if not(type(filename) is str):
        raise TypeError(f"""filename must be str, not {get_type(filename)}""")

    image = Image.open(path(filename))
    if is_watermarked(image):
        width, height = image.size
    
        step = get_step(image)
        text_length = calculate_text_length(width, height, step)

        text = ""
        current_x = 0
        current_y = 0
        step_x, step_y = get_stepx_and_stepy(width, height, step)

        for pixel in range(text_length):
            text += chr(image.getpixel((current_x, current_y))[2])
            current_x += step_x
            current_y += step_y

        return text.replace(chr(0),"")
    else:
        return None


    
    
