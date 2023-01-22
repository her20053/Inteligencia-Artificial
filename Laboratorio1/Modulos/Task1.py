from PIL import Image, ImageFilter

def resizeOriginal(img, factor = 10):

    # Open the image file
    image = Image.open(img)

    # Get the size of the image
    width, height = image.size

    # Scale down the image by a factor
    new_width = width // factor
    new_height = height // factor
    im = image.resize((new_width, new_height), Image.BILINEAR)

    # Save the new image
    im.save("scaled_down.bmp")

def sharpenNew(img):
    
    # Open the image
    image = Image.open(img)
    
    # Apply the unsharp mask filter
    image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    # Save the sharpened image
    image.save("sharpened.bmp")



resizeOriginal("laberinto1.bmp", 15)
sharpenNew("scaled_down.bmp")