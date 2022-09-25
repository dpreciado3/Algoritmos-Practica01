from Grafica import Grafica


def main():
    grafica = parse_graph_from_txt()
    independiente = conjunto_independiente(grafica)
    print(independiente)


def parse_graph_from_txt():
    with open('graph.txt') as graph:
        lineas = graph.readlines()
    # Primer linea del archivo son los nodos
    nodos = lineas[0].split(",")
    # Lista de nodos en int
    nodos = list(map(int, nodos))
    lineas.pop(0)
    # Registramos nodos como llaves en diccionario
    dicc_adyacencias = {}
    for i in nodos:
        dicc_adyacencias[i] = []
    # Ahora obtenemos adyacencias
    for j in lineas:
        arista = j.split(",")
        arista = list(map(int, arista))
        dicc_adyacencias[arista[0]].append(arista[1])
    grafica = Grafica(dicc_adyacencias)
    return grafica


def conjunto_independiente(grafica):
    if grafica.get_orden() == 1:
        return grafica.get_vertices()
    # Quitamos algún nodo random
    subgrafica = grafica
    removido = subgrafica.quita_vertice(subgrafica.get_vertices()[0])
    independiente = conjunto_independiente(subgrafica)
    if independiente == None:
        independiente = []
    # Hay dos conjuntos independientes, el que ya teníamos y el nuevo uniendo el vértice que se removió
    independiente_u = independiente
    independiente_u.append(removido[0])
    if es_independiente(independiente_u, grafica):
        return independiente_u
    else:
        return independiente


def es_independiente(conjunto, grafica):
    if conjunto == None or conjunto == []:
        conjunto = []
        return True
    vertices = grafica.get_vertices()
    for i in conjunto:
        otros = [x for x in vertices if x != i]
        for j in otros:
            if i in grafica.get_vecinos(j):
                return False
    return True


if __name__ == "__main__":
    main()
