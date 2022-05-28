import random
import string # pomocnicze - do generowania węzłów będących literami alfabetu
import networkx as nx
import matplotlib.pyplot as plt

def generate_adjacency_list(n) -> dict:
  '''
  Generuje losową listę sąsiedztwa

    Parameters:
      n (int): liczba węzłów
  
    Returns:
      słownik będący listą sąsiedztwa - klucze to węzły, wartości to zbiór sąsiadów
  '''
  # węzły to pierwsze n liter alfabetu ASCII
  nodes = list(string.ascii_uppercase[:n])

  adj_list = {} 

  for node in nodes:
    # aby uniknąć odwołań do siebie samego
    other_nodes = [nd for nd in nodes if nd != node]
    # losowanie listy sąsiedztwa na podstawie rozkładu normalnego
    # w ten sposób liczby sąsiadów są bardziej zróżnicowane
    num_of_neighbors = round(abs(random.gauss(0, 2)))+1
    adj_list[node] = {random.choice(other_nodes) for _ in range(num_of_neighbors)}

  return adj_list


def generate_random_digraph(adj_list) -> nx.DiGraph:
  '''
  Tworzy losowy digraf
    
    Parameters:
      adj_list (dict): lista sąsiedztwa na podstawie której tworzony jest digraf
  '''
  G = nx.DiGraph()

  # tworzenie krawędzi na podstawie listy sąsiedztwa
  edges = [(u, v) for u, nbrs in adj_list.items() for v in nbrs]

  # tworzenie grafu na podstawie listy sąsiedztwa i wcześniej wygenerowanych krawędzi
  G.update(edges=edges, nodes=adj_list)

  return G
