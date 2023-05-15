# Grupo: DENNYS PUCHA, ANGEL PESANTES Y LETTY ROJAS

import networkx as nx
import matplotlib.pyplot as plt
import heapq
import tkinter as tk

def ruta_mas_corta_dijkstra(grafo, nodo_inicial, nodo_final):
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[nodo_inicial] = 0
    anteriores = {nodo: None for nodo in grafo}
    nodo_visitado = {nodo: False for nodo in grafo}
    cola_verificadora = [(0, nodo_inicial)]

    while cola_verificadora:
        (dist, nodo) = heapq.heappop(cola_verificadora)
        if nodo == nodo_final:
            break
        if nodo_visitado[nodo]:
            continue
        nodo_visitado[nodo] = True

        for vecino, ancho in grafo[nodo].items():
            distancia = dist + ancho
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                anteriores[vecino] = nodo
                heapq.heappush(cola_verificadora, (distancia, vecino))

    ruta = [nodo_final]
    distancia = distancias[nodo_final]
    while ruta[-1] != nodo_inicial:
        ruta.append(anteriores[ruta[-1]])
    ruta.reverse()

    return ruta, distancia


grafo = {
    '1': {'2': 100, '3': 30},
    '2': {'3': 20},
    '3': {'5': 60, '4': 10},
    '4': {'2': 15,'5':50},
    '5': {},
}

G = nx.DiGraph()

for nodo in grafo:
    G.add_node(nodo)
    for vecino, peso in grafo[nodo].items():
        G.add_edge(nodo, vecino, weight=peso)

pos = nx.spring_layout(G)


ventana = tk.Tk()
ventana.title("Algortimo de dijkstra")
ventana.geometry("500x300")

label = tk.Label(ventana, text="Seleccione el nodo al que quiere detectar el camino minimo y la distancia")
label.pack(pady=10)


def accion_boton(number):
    ventanaMin = tk.Tk()
    ventanaMin.title(f"Eleccion NODO {number}")
    ventanaMin.geometry("400x100")
    ruta, distancia = ruta_mas_corta_dijkstra(grafo, '1', number)
    print()
    label = tk.Label(ventanaMin, text=f"La ruta más corta al nodo {number} es {ruta} con distancia {distancia}")
    label.pack(pady=10)
                                                                                          

boton_2 = tk.Button(ventana, text="2", width=10, height=2,command=lambda: accion_boton("2"))
boton_2.pack(pady=5)

boton_3 = tk.Button(ventana, text="3", width=10, height=2,command=lambda: accion_boton("3"))
boton_3.pack(pady=5)

boton_4 = tk.Button(ventana, text="4", width=10, height=2,command=lambda: accion_boton("4"))
boton_4.pack(pady=5)

boton_5 = tk.Button(ventana, text="5", width=10, height=2,command=lambda: accion_boton("5"))
boton_5.pack(pady=5)


def mostrar_grafo():
    fig, ax = plt.subplots(figsize=(6,6))
    nx.draw(G, pos, with_labels=True, ax=ax)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edges(G, pos, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    ax.set_xlim([0.9*x for x in ax.get_xlim()])
    ax.set_ylim([-1.2*y for y in ax.get_ylim()])
    plt.show()

boton_grafo = tk.Button(ventana, text="Mostrar grafo", bg="#ADD8E6", fg="#000000", width=20, height=3,command=lambda: mostrar_grafo())
boton_grafo.pack(pady=5)

ventana.mainloop()


