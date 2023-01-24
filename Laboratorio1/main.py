from Modulos.GraphSearch import GraphSearchAlgorithm

# maze = GraphSearchAlgorithm('Laberintos/Maze20x20.bmp')

# resp = maze.beginSearch()

# if resp:
    
#     maze.drawSolution('Soluciones/Solucion20x20.bmp')
#     maze.mazeUnavailable()
    
# maze = GraphSearchAlgorithm('Laberintos/LaberintoComplejo1.bmp')

# resp = maze.beginSearch()

# if resp:
    
#     maze.drawSolution('Soluciones/SolucionLC1.bmp')
#     maze.mazeUnavailable()

# else:
    
#     print("No existe solucion al laberinto proporcionado.")
    
maze = GraphSearchAlgorithm('Laberintos/Maze20x20.bmp')

resp = maze.beginSearch()

if resp:
    
    maze.drawSolution('Soluciones/Solucion20x20.bmp')
    maze.mazeUnavailable()

else:
    
    print("No existe solucion al laberinto proporcionado.")