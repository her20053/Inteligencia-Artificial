from PIL import Image

def task1(img):

    # Open the image file
    image = Image.open('imagen.bmp')

    # Get the size of the image
    width, height = image.size

    # Print the dimensions
    print("Width:", width)
    print("Height:", height)


task1("imagen.bmp")