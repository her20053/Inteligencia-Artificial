class Nodo:

    # Metodo constructor, inicializa el nombre del nodo, sus padres y su matriz de probabilidades
    def __init__(self, nombre, padres, matriz):
        self.nombre = nombre
        self.padres = padres
        self.matriz = matriz

    def __str__(self):
        return str("[{}] > Padres: {}  > Matriz: {}".format(self.nombre, self.padres, self.matriz))
