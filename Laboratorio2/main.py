from RedBayesiana import RedBayesiana

# Crear una red bayesiana
red = RedBayesiana()

# Agregar nodos a la red bayesiana
red.agregarNodo(
    nombre="R",
    padres=[],
    matriz={(): [0.999, 0.001]})

red.agregarNodo(
    nombre="T",
    padres=[],
    matriz={(): [0.998, 0.002]}
)

red.agregarNodo(
    nombre="A",
    padres=["R", "T"],
    matriz={(0, 0): [0.999, 0.001], (0, 1): [0.71, 0.29],
            (1, 0): [0.06, 0.94], (1, 1): [0.05, 0.95]}
)

red.agregarNodo(
    nombre="J",
    padres=["A"],
    matriz={(0,): [0.95, 0.05], (1,): [0.1, 0.9]}
)

red.agregarNodo(
    nombre="M",
    padres=["A"],
    matriz={(0,): [0.99, 0.01], (1,): [0.3, 0.7]}
)

# Mostrar todos los nodos de la red bayesiana
red.mostrarNodos()

# Mostar si la red bayesiana está completamente descrita
red.revisarRed()

# Mostrar la representación compacta de la red bayesiana
red.representacionCompacta()

# Mostrar los factor de la red bayesiana
red.obtenerFactores()
