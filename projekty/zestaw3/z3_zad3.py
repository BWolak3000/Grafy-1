import numpy as np
import z3_zad2

# ZADANIE 3 -------------------------------------------------------
# Wyznaczyc macierz odległosci miedzy wszystkimi parami wierzchołków
# na tym grafie.

def distance_matrix_from_graph(G):
  dist_m = np.zeros((len(G.nodes), len(G.nodes)), dtype=np.int32)

  for i, u in enumerate(G.nodes):
    dist_m[i] = z3_zad2.dijkstra(G, u)[0]

  return dist_m
