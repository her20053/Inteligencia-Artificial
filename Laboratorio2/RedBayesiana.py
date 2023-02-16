from Nodo import Nodo
from tabulate import tabulate


class RedBayesiana:

    # Metodo constructor, inicializa la lista de nodos
    def __init__(self):
        self.nodos = []

    # Metodo para agregar un nodo a la red bayesiana
    def agregarNodo(self, nombre, padres, matriz):
        self.nodos.append(Nodo(nombre=nombre, padres=padres, matriz=matriz))

    # Metodo para mostrar todos los nodos de la red bayesiana
    def mostrarNodos(self):

        tabla = []
        tabla.append(['Nombre', 'Padres', 'Matriz de probabilidades'])

        for nodo in self.nodos:
            tabla.append([nodo.nombre, nodo.padres, nodo.matriz])

        print("\nMostrando todos los nodos de la red bayesiana actual:\n")
        print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))

    # Metodo para dada una red bayesiana , devuelve si esta está completamente descrita (boolean)
    def revisarRed(self):

        redCompleta = True

        tabla = []
        tabla.append(['Nombre', 'Caso', 'Probabilidades', 'Suma'])

        for nodo in self.nodos:

            for entrada, valores in nodo.matriz.items():

                if sum(valores) != 1:

                    redCompleta = False

                tabla.append(
                    [nodo.nombre, entrada, valores, sum(valores)]
                )

        if redCompleta:
            print("\nLa red bayesiana actual está completamente descrita\n")
        else:
            print("\nLa red bayesiana actual NO está completamente descrita\n")

        print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))

    # Metodo para mostrar la representación compacta de la red bayesiana
    def representacionCompacta(self):

        resultado = ""
        resultadP = "P("

        for nodo in self.nodos:

            nombre = nodo.nombre

            resultadP += nombre + ","

            padres = nodo.padres

            if not padres:
                resultado += "P(" + nombre + ")"
            else:
                resultado += "P(" + nombre + "|" + ",".join(padres) + ")"

        resultado += " = " + resultadP[:-1] + ")"

        tabla = []

        tabla.append(['Representacion', 'Forma compacta'])
        tabla.append(["Red Bayesiana", resultado])

        print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))

    # Metodo para obtener los factores de la red bayesiana

    def obtenerFactores(self):

        resultado = []

        for nodo in self.nodos:

            if not nodo.matriz:

                resultado.append(
                    ("P(" + nodo.nombre + ")", "", "", "")
                )

                for estado, (phi, omg) in nodo.matriz.items():

                    resultado.append(
                        ("", nodo.nombre + "[0]", phi, "")
                    )
                    resultado.append(
                        ("", nodo.nombre + "[1]", omg, "")
                    )
                    resultado.append(
                        ("", "", "", "")
                    )

            else:

                resultado.append(
                    ("P(" + nodo.nombre + "|" + ", ".join(nodo.padres) + ")", "", "", "")
                )

                for estado, (phi, omg) in nodo.matriz.items():

                    resultado.append(
                        (
                            "",
                            ", ".join(str(caracter) for caracter in estado),
                            phi,
                            omg
                        )
                    )

        print("\nLa red bayesiana tiene los siguientes factores:\n")

        tabla = []
        tabla.append(["Variable", "Phi", "P(0)", "P(1)"])

        variable = ''

        for entrada in resultado:

            if entrada[0] != '':

                variable = entrada[0]

            else:
                temp = list(entrada)
                temp[0] = variable
                tabla.append(tuple(temp))

        print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))
