from PIL import Image

class GraphSearchAlgorithm():
    
    def __init__(self, ImagePath):
        self.image = Image.open(ImagePath)
        self.width, self.height = self.image.size
        self.start = None
        self.goals = set()
        self.colores = []
        self.walkable = set()
        self.recorridos = []
        self.puntosNoAlcanzados = 0
        self.load_image()
    
    def load_image(self):
        
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
                    self.start = (x,y)
                
                # Si el color del pixel es verde:
                elif pixel == (0, 255, 0):
                    self.goals.add((x, y))
    
    def mazeUnavailable(self):
        # Le dejamos saber si existen puntos que no se lograron alcanzar al usuario:
        if self.puntosNoAlcanzados > 0:
            print("No se han podido alcanzar los siguientes puntos: ", self.goals)
    
    def getMazeInfo(self):
        
        print("Posiciones walkable: ", self.walkable)
        print("Posiciones destino:  ", self.goals)
        print("Posicion de inicio:  ", self.start)
        print("")
        print("Colores que se presentan en la imagen:")
        print("")
        dicc = {}
        for c in self.colores:
            dicc[c] = 0
        for c in self.colores:
            dicc[c] = dicc[c] + 1
        for k,v in dicc.items():
            print("RGB " + str(k) + " | cantidad: " + str(v)) 
    
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
    
    def goalTest(self, celda):
        
        # Retornamos si la celda esta contenida en las casillas de meta o no:
        return (celda in self.goals)
    
    def obtenerCamino(self, celda, trazos):
        
        recorrido = {}
        posiciones = []
        
        while celda != self.start:
            
            recorrido[trazos[celda]] = celda
            celda = trazos[celda]
            
        for k,v in recorrido.items():
            posiciones.append(v)
            
        self.recorridos.append(posiciones)

    def drawSolution(self, fileName):
        
        imagenCopia = Image.new("RGB", self.image.size)
        
        pixelesOriginales = self.image.load()
        
        pixelesCopia = imagenCopia.load()
        
        for x in range(self.image.width):
            
            for y in range(self.image.height):
                
                pixel = pixelesOriginales[x,y]
                
                for solucion in self.recorridos:
                
                    for s in solucion:
                        
                        if (x,y) == s:
                            
                            pixel = (255,255,0)
            
                    pixelesCopia[x,y] = pixel
        
        imagenCopia.save(fileName)

    def beginSearch(self):
        
        # Comenzamos creando una frontera/queue con el punto de partida:
        queue = [self.start]
        
        # Creamos una lista de espacios que hemos explorado y le agregamos el punto de partida:
        celdasExploradas = [self.start]
        
        # Creamos un diccionario que nos indique los movimientos que se han tomado en el algoritmo:
        caminosRealizados = {}
        
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
                        
                        # Revisamos si existen varios goals, en caso de ser asi, eliminamos de la lista el alcanzado y comenzamos la busqueda del otro:
                        
                        if len(self.goals) > 1:
                            
                            self.goals.remove(movimiento)
                            
                            self.beginSearch()
                        
                        return True
            
                # Si se llego a este punto es que no se ha alcanzado una meta
                
                # Continuamos analizando las siguientes celdas:
                
                for movimiento in movimientos:
                    
                    # Si el mov no esta en lo explorado, lo agregamos al queue
                    
                    if movimiento not in celdasExploradas:
                        
                        queue.append(movimiento)
                        
                        # Declaramos en el camino hacia donde fue y de donde vino:
                        
                        caminosRealizados[movimiento] = celda
            
            else:
                # No tiene solucion el laberinto propuesto. Se retorna un falso:
                self.puntosNoAlcanzados += 1
                return False

        