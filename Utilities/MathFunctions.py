#MathFunctions
from math import ceil

def get_mark_position(x: int, y: int) -> tuple:
    return int(x*0.15), ceil(y*0.85)

def get_step_position(x: int, y: int) -> tuple: 
    return ceil(x*0.85), int(y*0.15)

def create_model_values(rgb: tuple) -> list:
    model_rgb = []
    for colour in rgb:
        if colour==255:
            model_rgb.append(254)
        else:
            model_rgb.append(colour+1)
    return model_rgb

def calculate_step(text: str, x: int, y: int) -> int: 
    if len(text)>max(x,y):
        raise ValueError(f"text's length is too long, max text length for this picture is {max(x,y)}")
    else:
        return round(max(x,y)/len(text))

def calculate_text_length(x: int, y: int, step: int) -> int:
    return round(max(x,y)/step)

def get_stepx_and_stepy(x: int, y: int, step: int) -> list: 
    if x==y:
        stepx = stepy = step
    elif x>y:
        stepx = step
        stepy = int(y/x*step)
    else:
        stepx = int(x/y*step)
        stepy = step
    return stepx, stepy
