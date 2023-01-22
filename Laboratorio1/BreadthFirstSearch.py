from PIL import Image
class BFS():
    
    def __init__(self, sharpImagePath):
        self.image = Image.open(sharpImagePath)
        self.width, self.height = self.image.size
        self.start = None
        self.goals = []
        self.walkable = set()
        self.todosColores = []
        self.load_image()
    
    def actions(self, state):
        
        # print(state)
        x,y = state
        acciones = []
        
        #Norte
        if (x,y+1) in self.walkable or (x,y+1) in self.goals:
            acciones.append((x,y+1))
        #Sur
        if (x,y-1) in self.walkable or (x,y-1) in self.goals:
            acciones.append((x,y-1))
        #Este
        if (x+1,y) in self.walkable or (x+1,y) in self.goals:
            acciones.append((x+1,y))
        #Oeste
        if (x-1,y) in self.walkable or (x-1,y) in self.goals:
            acciones.append((x-1,y))
        
        return acciones  
        # Implementation of method to return possible actions from the given state

    def result(self, state, action):
        pass  # Implementation of method to return the resulting state after taking the given action from the given state

    def goalTest(self, state):
        return (state in self.goals)
        # Implementation of method to check if the given state is the goal state

    def stepCost(self, state, action, next_state):
        pass  # Implementation of method to return the cost of taking the given action from the given state to the next state

    def pathCost(self, states):
        pass  # Implementation of method to return the total cost of the path represented by the given sequence of states
    
    def load_image(self):
        for x in range(self.width):
            for y in range(self.height):
                pixel = self.image.getpixel((x, y))
                if len(pixel) == 4:
                    pixel = pixel[:3]
                self.todosColores.append(pixel)
                if pixel == (255, 255, 255):
                    self.walkable.add((x, y))
                elif pixel == (255, 0, 0) or pixel == (254, 0, 0):
                    self.start = (x,y)
                elif pixel == (0, 255, 0):
                    self.goals.append((x, y))
    
    def getMapColors(self):
        dicc = {}
        for c in self.todosColores:
            dicc[c] = 0
        for c in self.todosColores:
            dicc[c] = dicc[c] + 1
        for k,v in dicc.items():
            print(str(k) + " cantidad: " + str(v))   
                
    def performAlgorithm(self):
        
        frontera = [self.start]
        
        espaciosExplorados = [self.start]
        
        pathBFS = {}
        
        while len(frontera) > 0:
            
            celdaActual = frontera.pop(0)
            
            # print(celdaActual)
            
            # Se revisa si la celda en la que estamos es una de meta.
            if self.goalTest(celdaActual):
                # Se acaba la iteracion porque hemos llegado al destino.
                print("Si se encontro solucion")
                break
            
            # Se revisa que acciones son posibles desde la celda en la que estamos
            posiblesAcciones = self.actions(celdaActual)
            
            for accion in posiblesAcciones:
                
                if accion not in espaciosExplorados:
                    
                    frontera.append(accion)
                    espaciosExplorados.append(accion)
                    
                    pathBFS[accion] = celdaActual
        
        pathRecorrido = {}
        
        celda = self.goals[0]
        # print(self.goals)
        
        while celda != self.start:
            
            pathRecorrido[pathBFS[celda]] = celda
            celda = pathBFS[celda]
            
            
        # print(pathRecorrido)
        
        return pathRecorrido

    def drawSolution(self, pathUsed, fileName):
        
        imagenCopia = Image.new("RGB", self.image.size)
        
        pixelesOriginales = self.image.load()
        
        pixelesCopia = imagenCopia.load()
        
        for x in range(self.image.width):
            
            for y in range(self.image.height):
                
                pixel = pixelesOriginales[x,y]
                
                for k,v in pathUsed.items():
                    
                    if (x,y) == k and pixel != (255,0,0):
                        
                        pixel = (255,255,0)
        
                pixelesCopia[x,y] = pixel
        
        imagenCopia.save(fileName)
        
         