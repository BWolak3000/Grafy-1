from math import inf

import draw_functions
import z3_zad1
import z3_zad2
import z3_zad3
import z3_zad4
import z3_zad5

def main():
  # wygenerowanie grafu losowego spójnego z wagami
  G = z3_zad1.generate_random_graph_with_weights()
  
  # ZADANIE 2
  s = 4 # wierzchołek, po którym wyszukuje się najkrótsze ścieżki
  print(f"Najkrótsze ścieżki dla s = {s}:")
  z3_zad2.print_shortest_paths(G, s)

  # ZADANIE 3
  distance_matrix = z3_zad3.distance_matrix_from_graph(G)
  print(f"Macierz odległości:\n {distance_matrix}")

  # ZADANIE 4
  center, center_sum = z3_zad4.graph_center(G)
  print(f"Centrum: {center} (suma odległości: {center_sum})")

  minimax, minimax_distance = z3_zad4.minimax_center(G)
  print(f"Centrum minimax: {minimax} (odległość od najdalszego: {minimax_distance})")

  # ZADANIE 5
  T = z3_zad5.minimal_spanning_tree(G)

  # rysowanie drzew
  draw_functions.graph_with_weights(G)
  draw_functions.graph_with_spanning_tree(G, T)


if __name__ == "__main__":
  main()
