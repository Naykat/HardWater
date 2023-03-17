#Utilities
from PIL import Image
from Utilities.MathFunctions import get_step_position

def get_type(variable) -> str:
    return str(type(variable)).split("'")[1]

def draw_step(image: Image, step: str) -> None:
    width, height = image.size
    step_position = get_step_position(width, height)
    r,g = image.getpixel(step_position)[:2]
    image.putpixel(step_position, (r,g,step))

def get_step(image: Image) -> int:
    width, height = image.size
    step_position = get_step_position(width, height)
    return image.getpixel(step_position)[2]
