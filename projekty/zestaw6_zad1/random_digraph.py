import random
import string # pomocnicze - do generowania węzłów będących literami alfabetu
import networkx as nx
import matplotlib.pyplot as plt

def generate_adjacency_list(n):
  if n < 1 or n > 32:
    raise Exception('Niewłaściwa wartość liczby węzłów')

  # węzły to pierwsze n liter alfabetu ASCII
  nodes = list(string.ascii_uppercase[:n+1])

  adj_list = {} # lista sąsiedztwa

  for node in nodes:
    # aby uniknąć odwołań do siebie samego
    other_nodes = [nd for nd in nodes if nd != node]
    # losowanie listy sąsiedztwa na podstawie rozkładu normalnego
    # w ten sposób liczby sąsiadów są bardziej zróżnicowane
    num_of_neighbors = round(abs(random.gauss(2, n/5)))+1
    adj_list[node] = {random.choice(other_nodes) for _ in range(num_of_neighbors)}

  return adj_list


def generate_random_digraph(adj_list):
  G = nx.DiGraph()

  # tworzenie krawędzi na podstawie listy sąsiedztwa
  edges = [(u, v) for u, nbrs in adj_list.items() for v in nbrs]

  # tworzenie grafu na podstawie listy sąsiedztwa
  G.update(edges=edges, nodes=adj_list)

  return G
