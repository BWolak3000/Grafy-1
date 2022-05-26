import random

# a) Metoda polegajaca na przechodzeniu od wierzchołka do sasiedniego
# wierzchołka za pomoca bładzenia przypadkowego z prawdopodobienstwem
# 1-d i teleportacji z prawdopodobienstwem d. Przyjac d = 0.15.
# PageRank wyliczyc jako czestosc odwiedzin danego wierzchołka.

# funkcja odpowiedzialna za błądzenie przypadkowe
# @param G - digraf
# @param d - prawdopodobieństwo teleportacji
# @param N - liczba odwiedzeń węzłów
def random_walk(G, d, N):
  page_rank_visits_ratio = {node: 0 for node in G.nodes()}

  current_node = random.choice(list(G.nodes()))
  
  for _ in range(N):
    # losowanie wartości z zakresu [0,1]
    # jeżeli wartość jest mniejsza od d - teleportacja,
    # czyli przejście do losowego wierzchołka w grafie
    if random.random() < d:
      other_nodes = [node for node in G.nodes() if node != current_node]
      current_node = random.choice(other_nodes)
    # w przeciwnym razie przejście do losowego z sąsiadów
    else:
      current_node = random.choice(list(G.neighbors(current_node)))

    page_rank_visits_ratio[current_node] += 1

  for node in G.nodes():
    page_rank_visits_ratio[node] /= N
  
  return page_rank_visits_ratio
