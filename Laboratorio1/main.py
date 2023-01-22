from BreadthFirstSearch import BFS

mapa = BFS('laberinto1.bmp')
path = mapa.performAlgorithm()

mapa.drawSolution(path, 'Solucion.bmp')