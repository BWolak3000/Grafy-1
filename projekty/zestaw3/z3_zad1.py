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

def generate_random_graph_with_weights():
  # przyklad ciągu graficznego
  list = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

  # generowanie grafu losowego wg. zadania 2 z zestawu 2
  list = sorted(list, reverse=True)

  is_graph_sequence, adj_matrix = Zestaw2_zad1_zad2.is_graphical(list)
  
  # sprawdzamy czy wygenerowany ciąg jest ciągiem graficznym
  # jeśli nie jest, przerywamy działanie programu
  if is_graph_sequence == False:
    raise Exception('Podany ciąg nie jest ciągiem graficznym!')
  
  adj_matrix_np = np.matrix(adj_matrix)
  G = nx.from_numpy_matrix(adj_matrix_np)
  G = Zestaw2_zad1_zad2.randomize_graph_adj_matrix(G, 10)
  
  # losujemy taki graf, aby był spójny
  while not nx.is_connected(G):
    G = Zestaw2_zad1_zad2.randomize_graph_adj_matrix(G, 10)

  # dodawanie wag do krawędzi
  for u, v in G.edges:
    G[u][v]["weight"] = random.randint(1,10)

  return G
