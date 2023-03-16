from PIL import Image
from Utilities.utils import *

def watermark(filename: str, text: str) -> Image:

    image = Image.open(filename)
    width, height = image.size
    
    last_pixel_width = (len(text)+4)%width
    last_pixel_height = (len(text)+4)//width
    encode_last_symbol_coordinates(image, last_pixel_width, last_pixel_height)

    symbols = prepare_text(text)
    for index, letter in enumerate(symbols):
        current_width = (index+4)%width
        current_height = (index+4)//width

        input_symbol_into_pixel(image, current_width, current_height, letter)
        
    return image

def reveal(filename: str) -> str:
    text = ""

    image = Image.open(filename)
    width = image.size[0]
    last_pixel_width, last_pixel_height = decode_last_symbol_coordinates(image)

    if last_pixel_height==0:
        text_length = last_pixel_width
    else:
        text_length = (last_pixel_height-1)*width+last_pixel_width

    for pixel in range(4,text_length):
        current_width, current_height = pixel%width, pixel//width
        text+=chr(image.getpixel((current_width,current_height))[2])
    return text

if __name__ == "__main__":
    watermark("Images/example.png","Naykat").save("HardWater.png")
    print(reveal("HardWater.png"))
    
