from PIL import Image
from Pixel import Pixel

def read_bmp(filepath):
    # Open the image
    img = Image.open(filepath)
    # Get the image's width and height
    width, height = img.size
    # Create an empty list to store the Pixel objects
    matriz_pixeles = []
    # Iterate over the image's pixels
    for y in range(height):
        row = []
        for x in range(width):
            # Create a new Pixel object with the pixel's color and position
            pixel = Pixel(img.getpixel((x, y))[:3], (x,y))
            row.append(pixel)
        matriz_pixeles.append(row)
    # Return the list of Pixel objects
    return matriz_pixeles