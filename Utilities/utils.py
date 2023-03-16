from PIL import Image

def prepare_text(text: str) -> list:
    result = []
    for letter in text:
        result.append(ord(letter))
    return result

def input_symbol_into_pixel(image: Image, width: int, height: int, symbol: int) -> None:
    r,g = image.getpixel((width,height))[:2]
    image.putpixel((width, height),(r,g,symbol))
    
def prepare_coordinates(width: int, height: int) -> tuple:
    return width//255, width%255, height//255, height%255

def encode_last_symbol_coordinates(image: Image, width: int, height: int) -> None:
    prepared_coordinates = prepare_coordinates(width, height)
    for current_pixel in range(4):
        r,g = image.getpixel((current_pixel+1, 0))[:2]
        image.putpixel((current_pixel+1, 0),
                       (r,g,prepared_coordinates[current_pixel]))

def decode_last_symbol_coordinates(image: Image) -> tuple:
    encoded_coordinates = []
    for current_pixel in range(1,5):
        encoded_coordinates.append(image.getpixel((current_pixel, 0))[2])   
    width = encoded_coordinates[0]*255+encoded_coordinates[1]
    height = encoded_coordinates[2]*255+encoded_coordinates[3]
    return width, height
