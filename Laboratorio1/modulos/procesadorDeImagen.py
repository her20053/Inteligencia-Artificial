from PIL import Image, ImageFilter

def sharpen_new(img):
    
    # Aplicamos el filtro de sharpening a la imagen:
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    pixels = img.load()

    # Definimos los 4 colores que vamos a usar
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    for i in range(img.width):
        for j in range(img.height):
            # Obtenemos el valor de los pixeles RGB
            r, g, b = pixels[i, j][:3]

            # Comparamos los valores con los umbrales para determinar el color
            if (r > 200) and (g < 50) and (b < 50):
                pixels[i, j] = red
            elif (r < 50) and (g > 200) and (b < 50):
                pixels[i, j] = green
            elif (r < 50) and (g < 50) and (b < 50):
                pixels[i, j] = black
            else:
                pixels[i, j] = white
    
    # Retornamos la imagen con el filtro aplicado
    return img


def disminuir_imagen_original(img, factor = 10):

    # Abrimos la imagen original
    image = Image.open(img)

    # Obtenemos el ancho y el alto de la imagen
    width, height = image.size

    # Reescalamos la imagen por el factor indicado (DEFAULT = 10)
    new_width = width // factor
    new_height = height // factor
    im = image.resize((new_width, new_height), Image.BILINEAR)

    # Enviamos la imagen reescalada al metodo sharpenNew para limpiarla
    im = sharpen_new(im)
    
    im.save("laberintos/imagen_reescalada.bmp")

