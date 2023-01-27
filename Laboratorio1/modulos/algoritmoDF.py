from progress.bar import Bar
from PIL import Image

class DepthFirstAlgorithm():
    
    def __init__(self, path_imagen):
        self.image = Image.open(path_imagen)
        self.width, self.height = self.image.size
        self.start = None
        self.goals = set()
        self.colores = []
        self.walkable = set()
        self.recorridos = []
        
        self.cargar_imagen()
    
    def cargar_imagen(self):
        
        for x in range(self.width):
            
            for y in range(self.height):
                
                # Obtenemos el color del pixel en la pos x,y:
                pixel = self.image.getpixel((x, y))
                
                # Revisamos que los rgba se vuelvan puramente rgb:
                if len(pixel) == 4:
                    pixel = pixel[:3]
                
                # Agregamos el color a la lista de colores:    
                self.colores.append(pixel)
                
                # Si el color del pixel es blanco:    
                if pixel == (255, 255, 255):
                    self.walkable.add((x, y))
                    
                # Si el color del pixel es rojo:     
                elif pixel == (255, 0, 0):
                    self.walkable.add((x, y))
                    self.start = (x,y)
                
                # Si el color del pixel es verde:
                elif pixel == (0, 255, 0):
                    self.goals.add((x, y))
    
    def goalTest(self, celda):
        # Retornamos si la celda esta contenida en las casillas de meta o no:
        return (celda in self.goals)
    
    def dibujar_solucion(self, nombre_imagen):
        
        imagenCopia = Image.new("RGB", self.image.size)
        
        pixelesOriginales = self.image.load()
        
        pixelesCopia = imagenCopia.load()
        
        for x in range(self.image.width):
            
            for y in range(self.image.height):
                
                pixel = pixelesOriginales[x,y]
                
                for s in self.recorridos:

                    if (x,y) == s:
                        
                        pixel = (255,  x + y ,0)
        
                pixelesCopia[x,y] = pixel
        
        imagenCopia.save(nombre_imagen)
    
    def actions(self, celda):
        
        # Retraemos las posiciones indiviuales de la celda:
        posX, posY = celda
        
        # Creamos una lista de acciones donde almacenamos los posibles movimientos
        movimientosPosibles = []
        
        # Revisamos cada posicion adyacente a la celda:
        # Celda de arriba:
        if ((posX,posY+1) in self.walkable) or ((posX,posY+1) in self.goals):
            # Si existe un psoible movimiento hacia arriba:
            movimientosPosibles.append((posX,posY+1))
        # Celda de abajo:
        if ((posX,posY-1) in self.walkable) or ((posX,posY-1) in self.goals):
            # Si existe un psoible movimiento hacia abajo:
            movimientosPosibles.append((posX,posY-1))
        # Celda de la derecha:
        if ((posX+1,posY) in self.walkable) or ((posX+1,posY) in self.goals):
            # Si existe un posible movimiento hacia la derecha:
            movimientosPosibles.append((posX+1,posY))
        # Celda de la izquierda:
        if ((posX-1,posY) in self.walkable) or ((posX-1,posY) in self.goals):
            # Si existe un posible movimiento hacia la izquierda:
            movimientosPosibles.append((posX-1,posY))
        
        # Retornamos los movimientos que ubicamos:
        return movimientosPosibles
    
    def start_search(self):
        
        stack = [self.start]
        
        visited = set()
        
        # Creamos una barra de progreso:
        barra_progreso = Bar(' [DFA] Analizando celdas...', max=len(self.walkable))
        
        while stack:
            
            celda_actual = stack.pop()
            
            # print("Celda actual: ", celda_actual)
            
            if celda_actual not in visited:
                
                visited.add(celda_actual)
                
                for hijo in self.actions(celda_actual):
                    
                    if hijo not in visited:
                        self.recorridos.append(hijo)
                        stack.append(hijo)
                        barra_progreso.next()
                    
                    if self.goalTest(hijo):
                        self.recorridos.append(hijo)
                        barra_progreso.finish()
                        return True
        
        barra_progreso.finish()
        return False