Instrucciones para utilizar las librerias de los algoritmos

El usuario tiene que asegurarse de estar en el directorio donde se encuentra el main.py. Al estarlo ejecutando desde otros
directorios puede ocurrir un error como 'No such file or directory'.

Una vez adentro del main puede importat cualquiera de los tres algoritmos de la siguiente manera:

from modulos.algoritmoBF import BreadthFirstAlgorithm
from modulos.algoritmoAs import AStarAlgorithm
from modulos.algoritmoDF import DepthFirstAlgorithm

Si se desea reducir una imagen deseada se tendra que importar el modulo de procesador de imagen:

from modulos.procesadorDeImagen import disminuir_imagen_original


Una vez importado el modulo de procesador de imagen, para reducir una imagen deseada se tiene que llamar a su metodo principal de la siguiente manera:

disminuir_imagen_original(path_del_archivo, factor_de_reduccion)

Por ejemplo: 

disminuir_imagen_original("laberintos/Laberinto2.bmp", 5)

Este algoritmo reducira su laberinto y el resultado lo almacenara en una imagen bmp dentro de /laberintos/ nombrada como 'imagen_reescalada.bmp'

Para utilizar cualquiera de los tres algoritmos tiene que seguir estos pasos:

[1] Crear un objeto del tipo del algoritmo deaseado y de parametro enviarle la imagen que desea analizar

[2] Alamacenar la respuesta (True/False) que retorna su objeto al momento de empezar la busqueda

[3] Si la respuesta es True significa que el algoritmo si encontro solucion. Por lo que puede acceder a su metodo dibujar solucion

Ejemplos escritos se encuentran en el main.