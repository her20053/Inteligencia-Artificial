from BreadthFirstSearch import BFS

mapa = BFS('Maze.bmp')

# mapa.getMapColors()

path = mapa.performAlgorithm()

mapa.drawSolution(path, 'Solucion2.bmp')