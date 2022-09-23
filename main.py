from Grafica import Grafica


def main():
    grafica = parse_graph_from_txt()
    print(grafica)

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
        return grafica.get_nodos()
    # Quitamos algún nodo random  
    subgrafica = grafica
    removido = subgrafica.quita_vertice(subgrafica.get_vertices[0])
    independiente = conjunto_independiente(subgrafica)

if __name__ == "__main__":
    main()