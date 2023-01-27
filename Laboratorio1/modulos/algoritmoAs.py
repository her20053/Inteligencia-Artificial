from progress.bar import Bar
from PIL import Image
from modulos.Pixel import Pixel

class AStarAlgorithm():
    
    def __init__(self, path_imagen):
        self.image = Image.open(path_imagen)
        self.width, self.height = self.image.size
        self.start = None
        self.goals = []
        self.colores = []
        self.walkable = set()
        self.recorridos = []
        
        self.c_camino = None
        self.c_actual = None
        
        self.matriz_pixeles = []
        
        self.cargar_imagen()
        
    def cargar_imagen(self):
        
        # Obtenemos el ancho y alto de la imagen:
        width, height = self.image.size
        # Creamos una lista de pixeles:
        matriz_pixeles = []
        # Iteramos sobre la imagen:
        for y in range(height):
            row = []
            for x in range(width):
                # Creamos un objeto Pixel con el color y la posicion:
                pixel = Pixel(self.image.getpixel((x, y))[:3], (x,y))
                row.append(pixel)
            matriz_pixeles.append(row)
        
        for fila in matriz_pixeles:
        
            for pixel in fila:
                
                # Esta condicion se cumple cuando el pixel es verde/goal
                if pixel.color == (0,255,0):
                    
                    self.goals.append(pixel)
                
                # Esta condicion se cumple cuando el pixel es rojo/start
                if pixel.color == (255,0,0):
                    
                    self.start = pixel
        
        # Declaramos la matriz de pixeles a la clase:
        self.matriz_pixeles = matriz_pixeles
    
    def heuristicaManhattan(self, actual, meta):
        x1, y1 = actual.position
        x2, y2 = meta.position
        # print("Heuristica",abs(x1 - x2) + abs(y1 - y2))
        return abs(x1 - x2) + abs(y1 - y2)
    
    def obtenerMenorValorF(self, lista):
        menor = lista[0]
        for pixel in lista:
            if pixel.f < menor.f:
                menor = pixel
        return menor
    
    def dibujar_solucion(self, nombre_imagen):

        # self.c_camino, self.c_actual

        path = []
        current = self.c_actual
        while current != None:
            path.append(current)
            current = self.c_camino[current]
        path.reverse()
        
        imagenCopia = Image.new("RGB", self.image.size)
        
        pixelesOriginales = self.image.load()
        
        pixelesCopia = imagenCopia.load()
        
        # print(path)
        
        for x in range(len(self.matriz_pixeles)):
            
            for y in range(len(self.matriz_pixeles[x])):
                
                pixel = pixelesOriginales[x,y]
                
                for p in path:
                    
                    if (x,y) == p.position:
                        
                        color = self.heuristicaManhattan(p, self.start)
                        
                        pixel = (100 + color, 0 , 200 + color)
                
                pixelesCopia[x,y] = pixel
                
        imagenCopia.save(nombre_imagen)        
        
    
    def acciones(self,pixel, matrix):
        
        posiblesPixeles = []

        posX = pixel.position[0]
        posY = pixel.position[1]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                
                #Arriba
                if matrix[row][col].position == (posX, posY - 1) and matrix[row][col].color != (0,0,0):
                    pixelTemp = matrix[row][col]
                    posiblesPixeles.append(pixelTemp)
                
                #Abajo
                if matrix[row][col].position == (posX, posY + 1) and matrix[row][col].color != (0,0,0):
                    pixelTemp = matrix[row][col]
                    posiblesPixeles.append(pixelTemp)
                
                #Derecha
                if matrix[row][col].position == (posX + 1, posY) and matrix[row][col].color != (0,0,0):
                    pixelTemp = matrix[row][col]
                    posiblesPixeles.append(pixelTemp)
                
                #Izquierda
                if matrix[row][col].position == (posX - 1, posY) and matrix[row][col].color != (0,0,0):
                    pixelTemp = matrix[row][col]
                    posiblesPixeles.append(pixelTemp)
        
        
        return posiblesPixeles
    
    def cost(self,current, next):
        return 1
    
    def start_search(self):
        
        # Definimos una lista de pixeles a visitar:
        open_list = []
        
        # Definimos una lista de pixeles visitados:
        closed_list = []
        
        # El diccionario con el path
        camino = {self.start: None}
        
        # El valor 'g' es el valor de la distancia entre el nodo actual y el nodo de inicio, por lo tanto es 0
        self.start.g = 0
        
        # El valor 'f' es el estimado de g + la heuristica, por lo tanto es 0 + la heuristica
        self.start.f = self.start.g + self.heuristicaManhattan(self.start, self.goals[0])
        
        # Agregamos el pixel de inicio a la lista abierta
        open_list.append(self.start)
            
        # Creamos una barra de progreso:
        barra_progreso = Bar(' [A*A] Analizando celdas...', max=self.height * self.width)
            
        while len(open_list) != 0:
            
            # Tomamos en nodo con el menor f-value de la lista abierta y lo movemos a la lista cerrada
            pixelActual = self.obtenerMenorValorF(open_list)
            
            # Lo removemos de la lista abierta:
            open_list.remove(pixelActual)
            
            # Lo agregamos a la lista cerrada:
            closed_list.append(pixelActual)
            
            # Revisamos que el pixel actual no sea el objetivo
            if pixelActual in self.goals:
                
                self.c_camino = camino
                self.c_actual = pixelActual
                
                barra_progreso.finish()
                
                return True
                # return self.construirPath(camino, pixelActual)
            
            # En caso de no haber hecho return, entonces el pixel actual no es el objetivo, por lo tanto
            # Obtenemos las acciones posibles desde este nodo actual:
            pixelesAcciones = self.acciones(pixelActual, self.matriz_pixeles)
            
            
            for accion in pixelesAcciones: 
                
                if accion in closed_list:
                    continue
                
                if accion not in open_list:
                    
                    open_list.append(accion)
        
                    accion.g = pixelActual.g + self.cost(pixelActual, accion)
                    
                    accion.f = accion.g + self.heuristicaManhattan(accion, self.goals[0])
                    
                    camino[accion] = pixelActual
                    
                    barra_progreso.next()
        
        # ----------------------------------------------------------------------------------------------------
        # [4] Si la lista abierta esta vacia, entonces no hay solucion
        barra_progreso.finish()
        return False