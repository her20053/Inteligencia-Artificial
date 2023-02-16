# RedBayesiana20053
## Inteligencia Artificial - Laboratorio 2 -

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Defina, arquitecte, documente e implemente una serie de funciones, objetos, métodos, etcétera, que permitirán al
usuario definir sus propias redes bayesianas. Tome en cuenta que su librería será usada por programadores con la
intención de implementar algoritmos que requieran dichas redes para operar, por lo tanto tome en cuenta la
ergonomía y experiencia del desarrollador

- Dada una red bayesiana (según sea la definición de su preferencia), devuelve si esta está completamente descrita (boolean)
- Dada una red bayesiana (según sea la definición de su preferencia), devuelve la representación compacta de la red bayesiana (string)
- Dada una red bayesiana (según sea la definición de su preferencia), devuelve los factores de la misma (hash maps / diccionarios / key-value)

> Esta libreria fue solamente implementada con el fin de crear una red bayesiana
> funcional, no se recomienda su uso para proyectos complejos debido a la incerteza
> que se puede dar. 

## Tecnologias usadas

Para el desarrollo de este proyecto se utilizo:

- [Python] - Para la creacion y manejo de la red Bayesiana

## Installation

Para instalar la libreria:

```sh
pip install RedBayesiana20053
```
## Metodos

RedBayesiana20053 incluye los siguientes metodos:

| Metodo | Descripcion |
| ------ | ------ |
| agregarNodo() | Agregar un nodo a la red|
| mostrarNodos() | Mostrar todos los nodos actuales en la red |
| revisarRed() | Metodo para dada una red bayesiana , devuelve si esta está completamente descrita (boolean) |
| representacionCompacta() | Metodo para mostrar la representación compacta de la red bayesiana|
| obtenerFactores() | Metodo para obtener los factores de la red bayesiana |

## Red Bayesiana

La red bayesiana fue creada como una clase, esta clase tiene un atributo llamado 'Nodos'. Los nodos son los que almacenan parametros como nombre, padres, matriz (cpt). Todos los metodos mencionados previamente son utilizados al momento de haber creado una red bayesiana de la siguiente manera:

```py
red = RedBayesiana()
```

Una vez creada la red bayesiana podemos agregar nodos de la siguiente manera:

```py
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
```

Ya fueron gregados nodos por lo que podemos hacer uso de nuestra libreria para obtener informacion sobre la red:
```
# Mostrar todos los nodos de la red bayesiana
red.mostrarNodos()

Mostrando todos los nodos de la red bayesiana actual:

╒══════════╤════════════╤════════════════════════════════════════════════════════════════════════════════════════════╕
│ Nombre   │ Padres     │ Matriz de probabilidades                                                                   │
╞══════════╪════════════╪════════════════════════════════════════════════════════════════════════════════════════════╡
│ R        │ []         │ {(): [0.999, 0.001]}                                                                       │
├──────────┼────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ T        │ []         │ {(): [0.998, 0.002]}                                                                       │
├──────────┼────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ A        │ ['R', 'T'] │ {(0, 0): [0.999, 0.001], (0, 1): [0.71, 0.29], (1, 0): [0.06, 0.94], (1, 1): [0.05, 0.95]} │
├──────────┼────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ J        │ ['A']      │ {(0,): [0.95, 0.05], (1,): [0.1, 0.9]}                                                     │
├──────────┼────────────┼────────────────────────────────────────────────────────────────────────────────────────────┤
│ M        │ ['A']      │ {(0,): [0.99, 0.01], (1,): [0.3, 0.7]}                                                     │
╘══════════╧════════════╧════════════════════════════════════════════════════════════════════════════════════════════╛

# Mostar si la red bayesiana está completamente descrita
red.revisarRed()

La red bayesiana actual está completamente descrita

╒══════════╤════════╤══════════════════╤════════╕
│ Nombre   │ Caso   │ Probabilidades   │   Suma │
╞══════════╪════════╪══════════════════╪════════╡
│ R        │ ()     │ [0.999, 0.001]   │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ T        │ ()     │ [0.998, 0.002]   │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ A        │ (0, 0) │ [0.999, 0.001]   │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ A        │ (0, 1) │ [0.71, 0.29]     │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ A        │ (1, 0) │ [0.06, 0.94]     │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ A        │ (1, 1) │ [0.05, 0.95]     │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ J        │ (0,)   │ [0.95, 0.05]     │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ J        │ (1,)   │ [0.1, 0.9]       │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ M        │ (0,)   │ [0.99, 0.01]     │      1 │
├──────────┼────────┼──────────────────┼────────┤
│ M        │ (1,)   │ [0.3, 0.7]       │      1 │
╘══════════╧════════╧══════════════════╧════════╛

# Mostrar la representación compacta de la red bayesiana
red.representacionCompacta()

╒══════════════════╤═════════════════════════════════════════════╕
│ Representacion   │ Forma compacta                              │
╞══════════════════╪═════════════════════════════════════════════╡
│ Red Bayesiana    │ P(R)P(T)P(A|R,T)P(J|A)P(M|A) = P(R,T,A,J,M) │
╘══════════════════╧═════════════════════════════════════════════╛

# Mostrar los factor de la red bayesiana
red.obtenerFactores()

La red bayesiana tiene los siguientes factores:

╒════════════╤═══════╤════════╤════════╕
│ Variable   │ Phi   │   P(0) │   P(1) │
╞════════════╪═══════╪════════╪════════╡
│ P(R|)      │       │  0.999 │  0.001 │
├────────────┼───────┼────────┼────────┤
│ P(T|)      │       │  0.998 │  0.002 │
├────────────┼───────┼────────┼────────┤
│ P(A|R, T)  │ 0, 0  │  0.999 │  0.001 │
├────────────┼───────┼────────┼────────┤
│ P(A|R, T)  │ 0, 1  │  0.71  │  0.29  │
├────────────┼───────┼────────┼────────┤
│ P(A|R, T)  │ 1, 0  │  0.06  │  0.94  │
├────────────┼───────┼────────┼────────┤
│ P(A|R, T)  │ 1, 1  │  0.05  │  0.95  │
├────────────┼───────┼────────┼────────┤
│ P(J|A)     │ 0     │  0.95  │  0.05  │
├────────────┼───────┼────────┼────────┤
│ P(J|A)     │ 1     │  0.1   │  0.9   │
├────────────┼───────┼────────┼────────┤
│ P(M|A)     │ 0     │  0.99  │  0.01  │
├────────────┼───────┼────────┼────────┤
│ P(M|A)     │ 1     │  0.3   │  0.7   │
╘════════════╧═══════╧════════╧════════╛

```


