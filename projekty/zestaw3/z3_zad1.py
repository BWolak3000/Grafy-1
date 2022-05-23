import numpy as np
import random
import networkx as nx
import sys

sys.path.append('..')
from zestaw2.zestaw2_zad1_zad2 import Zestaw2_zad1_zad2

# ZADANIE 1 -------------------------------------------------------
# Korzystajac z programów z poprzednich zestawów wygenerowac spójny
# graf losowy. Przypisac kazdej krawedzi tego grafu losowa wage bedaca
# liczba naturalna z zakresu 1 do 10.

# funkcja generująca graf losowy z wagami
def generate_random_graph_with_weights(list_of_node_degrees):
  
  # generowanie grafu losowego wg. zadania 2 z zestawu 2
  list_of_node_degrees = sorted(list_of_node_degrees, reverse=True)

  is_graph_sequence, adj_matrix = Zestaw2_zad1_zad2.is_graphical(list_of_node_degrees)
  
  print(f"Podany ciąg {list_of_node_degrees} jest graficzny: {is_graph_sequence}")

  # sprawdzamy czy wygenerowany ciąg jest ciągiem graficznym
  # jeśli nie jest, przerywamy działanie programu
  if is_graph_sequence == False:
    raise ValueError('Podany ciąg nie jest ciągiem graficznym!')
  
  adj_matrix_np = np.matrix(adj_matrix)
  G = nx.from_numpy_matrix(adj_matrix_np)
  
  # jeśli nie jest możliwe uzyskanie grafu spójnego, przerwij program
  if len(G.edges) < len(list_of_node_degrees) - 1:
    raise ValueError("Utworzony graf ma zbyt małą liczbę krawędzi, aby mógł być on spójny")

  # warunek zapobiegający nieskończonej pętli przy grafach
  # z wierzchołkiem o stopniu o 1 mniejszym od liczby wierzchołków
  if max(list_of_node_degrees) != len(list_of_node_degrees) - 1:
    G = Zestaw2_zad1_zad2.randomize_graph_adj_matrix(G, 10)
    
    # losujemy taki graf, aby był spójny (jeśli uzyskanie spójności jest możliwe)
    # ale tylko wtedy, kiedy wylosowany graf nie jest spójny
    # zapobiega to nieskończonej pętli w funkcji randomize_graph_adj_matrix, 
    # która wystąpiła na przykładzie z zajęć
    if nx.is_connected(G) == False: # bez tej linijki - nieskończona pętla dla przykładu z zajęć
      while nx.is_connected(G) == False:
        G = Zestaw2_zad1_zad2.randomize_graph_adj_matrix(G, 10)

  # dodawanie wag do krawędzi
  for u, v in G.edges:
    G[u][v]["weight"] = random.randint(1,10)

  return G
