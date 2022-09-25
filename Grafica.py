class Grafica:

    def __init__(self, dicc_adyacencias):
        self.dicc_adyacencias = dicc_adyacencias

    def __str__(self):
        return str(self.dicc_adyacencias)

    def get_vecinos(self, i):
        return self.dicc_adyacencias[i]

    def get_vertices(self):
        return list(self.dicc_adyacencias.keys())

    def get_orden(self):
        return len(self.dicc_adyacencias.keys())

    # Regresa una tupla donde el primer elemento es el vértice removido, el segundo su exvecindad y el tercero su invecindad
    def quita_vertice(self, vertice):
        exvecindad = self.dicc_adyacencias[vertice]
        invecindad = []
        self.dicc_adyacencias.pop(vertice)
        for x in self.dicc_adyacencias:
            if vertice in self.dicc_adyacencias[x]:
                self.dicc_adyacencias[x].remove(vertice)
                invecindad.append(x)
        return (vertice, exvecindad, invecindad)

    # Agregamos vértice con su exvecindad y su invecindad
    def agrega_vertice(self, tupla):
        self.dicc_adyacencias[tupla[0]] = tupla[1]
        for i in tupla[2]:
            self.dicc_adyacencias[i].append(tupla[0])

    # Agrega una arista que va del vértice a al b
    def agrega_arista(self, a, b):
        self.dicc_adyacencias[a].append([b])
