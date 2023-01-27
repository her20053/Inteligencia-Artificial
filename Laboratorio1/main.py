from modulos.procesadorDeImagen import disminuir_imagen_original
from modulos.algoritmoBF import BreadthFirstAlgorithm
from modulos.algoritmoAs import AStarAlgorithm
from modulos.algoritmoDF import DepthFirstAlgorithm

def programa():
    
    # Realizamos la disminucion del laberinto:
    disminuir_imagen_original("laberintos/Laberinto2.bmp", 5) 
    
    # Aplicamos el algoritmo Breadth First a la imagen reescalada:
    bfs = BreadthFirstAlgorithm("laberintos/imagen_reescalada.bmp")
    res = bfs.start_search()
    bfs.dibujar_solucion("laberintos/solucion_laberintoBF.bmp") if res else print("No se encontro solucion!")
    
    # Aplicamos el algoritmo A* a la imagen reescalada:
    asa = AStarAlgorithm("laberintos/imagen_reescalada.bmp")
    res = asa.start_search()
    asa.dibujar_solucion("laberintos/solcuion_laberintoAS.bmp") if res else print("No se encontro solucion!")
    
    # Aplicamos el algoritmo Depth First a la imagen reescalada:
    dfs = DepthFirstAlgorithm("laberintos/imagen_reescalada.bmp")
    res = dfs.start_search()
    dfs.dibujar_solucion("laberintos/solucion_laberintoDF.bmp") if res else print("No se encontro solucion!")

if __name__ == '__main__':
    programa()