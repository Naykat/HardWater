#Utilities
from PIL import Image
from Utilities.MathFunctions import get_step_position, get_mark_position, create_model_values

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

def mark(image: Image) -> None:
    width, height = image.size
    mark_x, mark_y = get_mark_position(width, height)
    model_r,model_g, model_b = image.getpixel((mark_x+1, mark_y))
    r,g,b = create_model_values((model_r,model_g, model_b))
    image.putpixel((mark_x,mark_y),(r,g,b))

def is_watermarked(image: Image) -> bool:
    width, height = image.size
    mark_x, mark_y = get_mark_position(width, height)
    model_r, model_g, model_b  = image.getpixel((mark_x+1, mark_y))
    r,g,b = image.getpixel((mark_x, mark_y))
    if abs(model_r-r) == 1 \
       and abs(model_b-b) == 1 \
       and abs(model_b-b) == 1:
        return True
    else:
        return False
