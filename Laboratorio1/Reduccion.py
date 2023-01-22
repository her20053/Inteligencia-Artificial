from PIL import Image

# Abre la imagen BMP
im = Image.open("Laberintos/LaberintoComplejo1.bmp")

FACTOR = 50

# Reduzco la resolución a FACTOR
im = im.resize((FACTOR, FACTOR), Image.ANTIALIAS)

# Creo una nueva imagen con el mismo tamaño pero con un formato RGB
new_im = Image.new("RGB", (FACTOR, FACTOR), "white")

# Recorro cada pixel de la imagen reducida
for i in range(FACTOR):
    for j in range(FACTOR):
        # Obtengo el color del pixel
        color = im.getpixel((i, j))
        # Verifico el color y lo reemplazo por el color deseado
        if color == (0, 0, 0): # negro
            new_im.putpixel((i, j), (0, 0, 0))
        elif color == (254, 0, 0): # rojo
            new_im.putpixel((i, j), (254, 0, 0))
        elif color == (0, 255, 0): # verde
            new_im.putpixel((i, j), (0, 255, 0))

# Guardo la nueva imagen
new_im.save("laberinto_discreto.bmp")