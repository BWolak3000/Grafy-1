import draw_functions
import z3_zad1
import z3_zad2
import z3_zad3
import z3_zad4
import z3_zad5

def main():
  list_of_node_degrees = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
  # list_of_node_degrees = [5, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
  # list_of_node_degrees = [6, 6, 6, 6, 6, 4]

  # przyklad ciągu niegraficznego
  # list_of_node_degrees = [4, 4, 3, 1, 2]

  # przyklad z zajec BW
  # list = [4, 4, 4, 4, 2, 2]

  if max(list_of_node_degrees) >= len(list_of_node_degrees):
    print("Co najmniej jeden ze stopni wierzchołka jest większy bądź równy liczbie wierzchołków")
    return
  
  # ZADANIE 1
  # wygenerowanie grafu losowego spójnego z wagami
  try:
    G = z3_zad1.generate_random_graph_with_weights(list_of_node_degrees)
  except ValueError as err:
    print(err)
    return
  except:
    print("Nie podano ciągu graficznego lub ciąg graficzny jest pusty")
    return
  
  # ZADANIE 2
  s = 1 # wierzchołek, po którym wyszukuje się najkrótsze ścieżki
  print(f"Najkrótsze ścieżki dla s = {s}:")

  try:
    z3_zad2.print_shortest_paths(G, s)
  except:
    print("Podany wierzchołek nie znajduje się w grafie")

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

  # rysowanie grafów
  draw_functions.graph_with_weights(G)
  draw_functions.graph_with_spanning_tree(G, T)


if __name__ == "__main__":
  main()
