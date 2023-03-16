from PIL import Image, ImageDraw

def prepare_text(text):
    result = []
    for letter in text:
        result.append(ord(letter))
    return result

def input_symbol_into_pixel(image, width, height, symbol):
    r,g,b = image.getpixel((width,height))
    image.putpixel((width, height),(r,g,symbol))
    
def prepare_coordinates(width, height):
    return width//255, width%255, height//255, height%255

def encode_last_pixel_coordinates(image, width, height):
    prepared_coordinates = prepare_coordinates(width, height)
    for current_pixel in range(4):
        r,g,b = image.getpixel((current_pixel, 0))
        image.putpixel((current_pixel, 0),
                       (r,g,prepared_coordinates[current_pixel]))

def decode_last_pixel_coordinates(image):
    encoded_coordinates = []
    for current_pixel in range(4):
        encoded_coordinates.append(image.getpixel((current_pixel, 0))[2])
    width = encoded_coordinates[0]*255+encoded_coordinates[1]
    height = encoded_coordinates[2]*255+encoded_coordinates[3]
    return width, height

def watermark(filename: str, text: str) -> Image:
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    width, height = image.size
    symbols = prepare_text(text)
    last_pixel_width = (len(text)+4)%width
    last_pixel_height = (len(text)+4)//width
    encode_last_pixel_coordinates(image, last_pixel_width, last_pixel_height)
    for index, letter in enumerate(symbols):
        current_width = (index+4)%width
        current_height = (index+4)//width
        input_symbol_into_pixel(image, current_width, current_height, letter)
    image.save("hardwater.png")

def reveal(filename: str) -> str:
    text = ""
    image = Image.open(filename)
    width = image.size[0]
    last_pixel_width, last_pixel_height = decode_last_pixel_coordinates(image)
    if last_pixel_height==0:
        text_length = last_pixel_width
    else:
        text_length = (last_pixel_height-1)*width+last_pixel_width
    for pixel in range(4,text_length):
        current_width, current_height = pixel%width, pixel//width
        text+=chr(image.getpixel((current_width,current_height))[2])
    return text

if __name__ == "__main__":
    watermark("pink_turtle.png","Naykat")
    
