import random
import networkx as nx
import numpy as np

# a) Metoda polegajaca na przechodzeniu od wierzchołka do sasiedniego
# wierzchołka za pomoca bładzenia przypadkowego z prawdopodobienstwem
# 1-d i teleportacji z prawdopodobienstwem d. Przyjac d = 0.15.
# PageRank wyliczyc jako czestosc odwiedzin danego wierzchołka.

def random_walk(G, d, N) -> dict:
  '''
  Oblicza PageRank wykorzystując błądzenie przypadkowe

    Parameters:
      G (nx.DiGraph): digraf
      d (float): prawdopodobieństwo teleportacji
      N (int): liczba odwiedzeń węzłów

    Returns:
      posortowany słownik, gdzie klucze to węzły, a wartości to PageRank danego węzła
  '''
  page_rank_visits_ratio = {node: 0 for node in G.nodes()}

  current_node = random.choice(list(G.nodes()))
  
  for _ in range(N):
    # losowanie wartości z zakresu [0,1]
    # jeżeli wartość jest mniejsza od d - teleportacja,
    # czyli przejście do losowego wierzchołka w grafie
    if random.random() < d:
      other_nodes = [node for node in G.nodes() 
        if node not in list(G.neighbors(current_node)) and node != current_node]
      
      current_node = random.choice(other_nodes)
    # w przeciwnym razie przejście do losowego z sąsiadów
    else:
      current_node = random.choice(list(G.neighbors(current_node)))

    page_rank_visits_ratio[current_node] += 1

  # aby otrzymać PageRank należy podzielić liczbę odwiedzeń przez liczbę wszystkich iteracji
  for node in G.nodes():
    page_rank_visits_ratio[node] /= N
  
  return dict(sorted(page_rank_visits_ratio.items(), key=lambda x: -x[1]))


# b) Metoda iteracji wektora obsadzen (czyli metoda potęgowa)
def power_method(G, d, N) -> dict:
  '''
  Oblicza PageRank za pomocą metody potęgowej

    Parameters:
      G (nx.DiGraph): digraf
      d (float): prawdopodobieństwo 
      N (int): liczba iteracji 

    Returns:
      posortowany słownik, któego klucze to węzły, a wartości to PageRank danego węzła
  '''
  n = len(G.nodes)
  # początkowy wektor permutacji
  p_t = np.array([1/n] * n)
  # macierz sąsiedztwa
  A = nx.to_numpy_array(G)
  # stopnie wychodzące wierzchołków
  d_i = np.array([G.out_degree(node) for node in G.nodes])

  # macierz stochastyczna
  P = np.zeros((n, n))

  for i in range(n):
    for j in range(n):
      P[i][j] = (1-d) * A[i][j]/d_i[i] + d/n

  # mnożenie wektora p_t i macierzy P
  for _ in range(N):
    p_t = np.dot(p_t, P)
  
  page_rank_visits_ratio = {node: p for node, p in zip(G.nodes, p_t)}

  return dict(sorted(page_rank_visits_ratio.items(), key=lambda x: -x[1]))
