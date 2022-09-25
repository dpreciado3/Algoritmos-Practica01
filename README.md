# Práctica 01: Conjunto independiente
25 de septiembre de 2022

David Salvador Preciado Márquez 421091670
### Ejecución
Para poder ejecutar el programa basta con introducir desde la consola, en el directorio /src, el siguiente comando:
```
python3 main.py
```
### Entrada
El programa recibe como entrada una gráfica representada en un archivo de texto.
Dicho archivo de texto debe tener el nombre "graph.txt" y debe estar contenido en 
la misma carpeta que "main.py" y "Grafica.py".
### Salida
El programa imprime en pantalla la lista con los nodos del conjunto independiente 
que cumple con el teorema.
### Notas
- El programa hace uso de la paquetería "copy", la cual solo nos ayuda a hacer
copias de objetos y no ayuda en la implementación del algoritmo de ninguna forma.
- La implementación se realizó aprovechando la estructura diccionario de Phyton 3,
donde cada nodo es una llave en el diccionario que representa la gráfica y cada llave
tiene asociada su lista de vecinos, que en este caso sería su exvecindad.
