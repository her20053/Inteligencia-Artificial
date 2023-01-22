from Modulos.GraphSearch import GraphSearchAlgorithm

maze = GraphSearchAlgorithm('Laberintos/Maze20x20.bmp')

resp = maze.beginSearch()

if resp:
    
    maze.drawSolution('Soluciones/Solucion20x20.bmp')