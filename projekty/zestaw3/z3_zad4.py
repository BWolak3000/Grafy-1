import numpy as np
import z3_zad3

# ZADANIE 4 ------------------------------------------------------------
# Wyznaczyc centrum grafu, to znaczy wierzchołek, którego suma odległosci
# do pozostałych wierzchołków jest minimalna. Wyznaczyc centrum
# minimax, to znaczy wierzchołek, którego odległosc do najdalszego
# wierzchołka jest minimalna.

def graph_center(G):
  distance_matrix = z3_zad3.distance_matrix_from_graph(G)

  row_sums = np.array([np.sum(node_distances) for node_distances in distance_matrix], dtype=np.int32)

  min_sum = np.min(row_sums)
  #  węzeł o minimalnej sumie oraz minimalna suma
  return list(row_sums).index(min_sum), min_sum


def minimax_center(G):
  distance_matrix = z3_zad3.distance_matrix_from_graph(G)

  min_max_distances = np.array([np.max(distances_from_node) for distances_from_node in distance_matrix], dtype=np.int32)

  minimax_distance = np.min(min_max_distances)
  # węzeł o minimalnej największej odległości oraz minimalna największa odległość
  return list(min_max_distances).index(minimax_distance), minimax_distance
