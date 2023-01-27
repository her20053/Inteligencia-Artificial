from progress.bar import Bar
from PIL import Image

class BreadthFirstAlgorithm():
    
    def __init__(self, path_imagen):
        self.image = Image.open(path_imagen)
        self.width, self.height = self.image.size
        self.start = None
        self.goals = set()
        self.colores = []
        self.walkable = set()
        self.recorridos = []
        
        self.cargar_imagen()
    
    def dibujar_solucion(self, nombre_imagen):
        
        imagenCopia = Image.new("RGB", self.image.size)
        
        pixelesOriginales = self.image.load()
        
        pixelesCopia = imagenCopia.load()
        
        for x in range(self.image.width):
            
            for y in range(self.image.height):
                
                pixel = pixelesOriginales[x,y]
                
                for s in self.recorridos:

                    if (x,y) == s:
                        
                        # pixel = ((x + y),255,0)
                        pixel = (0, 100 + x + y, 75 + x + y)
        
                pixelesCopia[x,y] = pixel
        
        imagenCopia.save(nombre_imagen)
    
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
    
    def obtenerCamino(self, celda, trazos):
        
        recorrido = {}
        posiciones = []
        
        while celda != self.start:
            
            recorrido[trazos[celda]] = celda
            celda = trazos[celda]
            
        for k,v in recorrido.items():
            posiciones.append(v)
        
        # Retornamos el recorrido que realizo el algoritmo:    
        self.recorridos = posiciones
    
    def start_search(self):
        
        # Comenzamos creando una frontera/queue con el punto de partida:
        queue = [self.start]
        
        # Creamos una lista de espacios que hemos explorado y le agregamos el punto de partida:
        celdasExploradas = [self.start]

        # Creamos un diccionario que nos indique los movimientos que se han tomado en el algoritmo:
        caminosRealizados = {}

        # Creamos una barra de progreso:
        barra_progreso = Bar(' [BFA] Analizando celdas...', max=len(self.walkable))

        # Creamos un ciclo infinito hasta que encontremos una solucion o la frontera este vacia:
        while True:
            
            # La frontera aun tiene celdas que explorar
            if len(queue):
                
                # Localizamos una celda del queue para analizar
                celda = queue.pop(0)
                
                # Agregamos la celda a la lista de celdas ya explorada:
                celdasExploradas.append(celda)
                
                # Verificamos a que celdas nos podemos mover desde la posicion actual (s):
                
                movimientos = self.actions(celda)
                
                # Verificamos que uno de los siguientes movimientos no sean ya la meta:
                
                for movimiento in movimientos:
                    
                    if self.goalTest(movimiento):
                        
                        # Se ha llegado al destino:
                        self.obtenerCamino(celda, caminosRealizados)
                        
                        barra_progreso.finish()
                        
                        return True
            
                # Si se llego a este punto es que no se ha alcanzado una meta
                
                # Continuamos analizando las siguientes celdas:
                
                for movimiento in movimientos:
                    
                    # Si el mov no esta en lo explorado, lo agregamos al queue
                    
                    if movimiento not in celdasExploradas:
                        
                        queue.append(movimiento)
                        
                        celdasExploradas.append(movimiento)
                        
                        # Declaramos en el camino hacia donde fue y de donde vino:
                        
                        caminosRealizados[movimiento] = celda
                        
                        barra_progreso.next()
            
            else:
                
                barra_progreso.finish()
                # No tiene solucion el laberinto propuesto. Se retorna un falso:
                return False