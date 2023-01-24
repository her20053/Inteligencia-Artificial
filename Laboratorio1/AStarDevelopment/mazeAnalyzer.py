def heuristicaManhattan(actual, meta):
    x1, y1 = actual.position
    x2, y2 = meta.position
    return abs(x1 - x2) + abs(y1 - y2)

def obtenerMenorValorF(lista):
    menor = lista[0]
    for pixel in lista:
        if pixel.f < menor.f:
            menor = pixel
    return menor

def construirPath(camino, goal):
    
    # for k,v in camino.items():
    #     print(k, v)
    
    path = []
    current = goal
    while current != None:
        path.append(current)
        current = camino[current]
    path.reverse()
    
    # for i in path:
    #     print(i)
    
    return path

def cost(current, next):
    return 1

def obtenerAccionesPosibles(pixel, matrix):
    
    posiblesPixeles = []
    
    # Revisamos el pixel de arriba
    
    posX = pixel.position[0]
    posY = pixel.position[1]
    
    # print("Para el pixel x:", posX, "y:", posY)
    
    # PixelAbajo = None
    
    # for i in matrix:
    #     for p in i:
    #         print(p.position, end='|')
    #     print()
    
    # for row in range(len(matrix)):
    #     for col in range(len(matrix[row])):
    #         if matrix[row][col].position == (posX, posY - 1):
    #             PixelAbajo = matrix[row][col]
    #             break
    
    # Pos izquierda = posX - 1, posY
    # Pos derecha = posX + 1, posY
    # Pos arriba = posX, posY - 1
    # Pos abajo = posX, posY + 1
    
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
    
    # print("Para ", pixel)
    # for p in posiblesPixeles:
    #     print(p,end=' ')
    # print()
    # input()
    
    
    # try:
    #     if matrix[posX][posY + 1].color != (0,0,0):
    #         posiblesPixeles.append(matrix[posX][posY + 1])    
    #     print("Si existe arriba", matrix[posX][posY + 1])
    # except:
    #     # No existe tal pixel
    #     pass
    # # Revisamos el pixel de abajo
    # try:
    #     if matrix[posX][posY - 1].color != (0,0,0):
    #         posiblesPixeles.append(matrix[posX][posY - 1])
    #     print("Si existe abajo", matrix[posX][posY - 1])
        
    # except:
    #     # No existe tal pixel
    #     pass
    # # Revisamos el pixel de la izquierda
    # try:
    #     if matrix[posX - 1][posY].color != (0,0,0):
    #         posiblesPixeles.append(matrix[posX - 1][posY])
    #     print("Si existe izq", matrix[posX - 1][posY])
        
    # except:
    #     # No existe tal pixel
    #     pass
    # # Revisamos el pixel de la derecha
    # try:
    #     if matrix[posX + 1][posY].color != (0,0,0):
    #         posiblesPixeles.append(matrix[posX + 1][posY])
    #     print("Si existe der", matrix[posX + 1][posY])
        
    # except:
    #     # No existe tal pixel
    #     pass
    
    # print("Para el pixel", pixel, "sus posibles pixeles son:")
    # for p in posiblesPixeles:
    #     print(p,end=' ')
    # print()
    # input()
    
    return posiblesPixeles
    
def AStarAlgorithm(matrix):
    
    # A* is a search algorithm that is used to find the shortest path between two nodes in a graph. 
    # It combines the strengths of two other algorithms: Dijkstra's algorithm, which is used to find
    # the shortest path in a graph, and the Best-First Search algorithm, which is used to find the 
    # path that is most likely to lead to the goal.
    # ----------------------------------------------------------------------------------------------------
    # First of all, we need to define some key values
    
    # The start
    startPixel = None
    
    # The goal, or multiple goals
    goalPixels = []
        
    # Now we need to fill these variables with the information that comes from the matrix:
    
    for row in matrix:
        
        for pixel in row:
            
            # This condition is met when the pixel is green/goal
            if pixel.color == (0,255,0):
                
                goalPixels.append(pixel)
            
            # This condition is met when the pixel is red/start
            if pixel.color == (255,0,0):
                
                startPixel = pixel
    # ----------------------------------------------------------------------------------------------------
    # [1] Initialize the open and closed lists. The open list contains the nodes that have been discovered
    # but not yet evaluated, while the closed list contains the nodes that have been evaluated. 
    
    # We define the open list
    open_list = []
    
    # We define the closed list
    closed_list = []
    
    # El diccionario con el path
    camino = {startPixel: None}
    
    # ----------------------------------------------------------------------------------------------------
    # [2] Add the starting node to the open list and set its g-value (the cost of getting to that node from
    # start) to 0. The f-value (the estimated total cost of getting to the goal from that node) is also set
    # to the heuristic cost (an estimate of the cost of getting to the goal from that node).
    
    # El valor 'g' es el valor de la distancia entre el nodo actual y el nodo de inicio, por lo tanto es 0
    startPixel.g = 0
    
    # El valor 'f' es el estimado de g + la heuristica, por lo tanto es 0 + la heuristica
    startPixel.f = startPixel.g + heuristicaManhattan(startPixel, goalPixels[0])
    
    # Agregamos el pixel de inicio a la lista abierta
    open_list.append(startPixel)
    # ----------------------------------------------------------------------------------------------------
    # [3] Mientras la lista abierta no este vacia, hacer lo siguiente:
    
    while len(open_list) != 0:
        
        # Tomamos en nodo con el menor f-value de la lista abierta y lo movemos a la lista cerrada
        pixelActual = obtenerMenorValorF(open_list)
        
        # print('\nOpen list: ', end=" ")
        # for p in open_list:
        #     print(p, end=" ")
        # print()
        
        # print(pixelActual, " valores: g=", pixelActual.g, " f=", pixelActual.f)
        
        # Lo removemos de la lista abierta:
        open_list.remove(pixelActual)
        
        # Lo agregamos a la lista cerrada:
        closed_list.append(pixelActual)
        
        # Revisamos que el pixel actual no sea el objetivo
        if pixelActual in goalPixels:
            return construirPath(camino, pixelActual)
        
        # En caso de no haber hecho return, entonces el pixel actual no es el objetivo, por lo tanto
        # Obtenemos las acciones posibles desde este nodo actual:
        pixelesAcciones = obtenerAccionesPosibles(pixelActual, matrix)
        
        
        for accion in pixelesAcciones: 
            
            # print("Accion: ", accion)
            
            if accion in closed_list:
                # print("Accion en closed list")
                continue
            
            if accion not in open_list:
                # print("Accion no en open list")
                open_list.append(accion)
    
                accion.g = pixelActual.g + cost(pixelActual, accion)
                
                accion.f = accion.g + heuristicaManhattan(accion, goalPixels[0])
                
                camino[accion] = pixelActual
    
    # ----------------------------------------------------------------------------------------------------
    # [4] Si la lista abierta esta vacia, entonces no hay solucion
    return None