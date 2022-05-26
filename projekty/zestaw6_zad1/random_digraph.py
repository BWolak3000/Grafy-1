import random
import string # do generowania węzłów będących literami alfabetu
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
    # losowanie listy sąsiedztwa
    # każdy węzeł może mieć od jednego do n-1 sąsiadów
    # TODO wymyślić lepszy sposób generowania listy sąsiedztwa - obecnie lista sąsiadów jest zbyt równomierna
    adj_list[node] = {random.choice(other_nodes) for _ in range(1,len(nodes))}

  return adj_list


def generate_random_digraph(n):
  G = nx.DiGraph()
  adj_list = generate_adjacency_list(n)

  # tworzenie krawędzi na podstawie listy sąsiedztwa
  edges = [(u, v) for u, nbrs in adj_list.items() for v in nbrs]

  # tworzenie grafu na podstawie listy sąsiedztwa
  G.update(edges=edges, nodes=adj_list)

  return G
