from math import inf


# ZADANIE 2 -----------------------------------------------------------
# Zaimplementowac algorytm Dijkstry do znajdowania najkrótszych sciezek
# od zadanego wierzchołka do pozostałych wierzchołków i zastosowac
# go do grafu z zadania pierwszego, w którym wagi krawedzi interpretowane
# sa jako odległosci wierzchołków. Wypisac wszystkie najkrótsze
# sciezki od danego wierzchołka i ich długosci.


# Nadanie wartosci poczatkowych atrybutów d oraz p dla wierzchołków grafu G
# @param G - graf wejściowy
# @param s - wybrany wierzchołek-źródło (numer wierzchołka jest jednocześnie indeksem w tablicy wierzchołków)
def init_d_p(G, s):
  d_s = [inf for _ in range(len(G.nodes))]
  p_s = [None for _ in range(len(G.nodes))]
  
  d_s[s] = 0

  return d_s, p_s


# Relaksacja krawędzi
# @param u, v - wierzchołki połączone krawędzią
# @param w - waga krawędzi (u, v)
def relax(u, v, w, d_s, p_s):
  if d_s[v] > d_s[u] + w:
    d_s[v] = d_s[u] + w
    p_s[v] = u
  
  return d_s[v], p_s[v]

# Algorytm Dijkstry - Zadanie 2
# @param G - graf
# @param s - wierzchołek startowy 
def dijkstra(G, s):
  d_s, p_s = init_d_p(G, s)
  
  # zbiór "sprawdzonych" wierzchołków; początkowo pusty
  S = []

  # niegotowe węzły - pierwszy element krotki to numer węzła
  # drugi element to d danego węzła
  uncompleted_nodes = list(zip(G.nodes, d_s))

  # dopóki nie zostały sprawdzone wszystkie wierzchołki
  while len(S) != len(G.nodes):
    node_with_min_d = min(uncompleted_nodes, key=lambda node: node[1])
    # wierzchołek o najmniejszym d_s(u) spośród niesprawdzonych wierzchołków
    u = node_with_min_d[0]
    uncompleted_nodes.remove(node_with_min_d)
    S.append(u)
    # wybieramy tych sąsiadów u, którzy nie znajdują się w S
    u_neighbors_not_in_S = list(filter(lambda v: v not in S, list(G.neighbors(u))))

    for v in u_neighbors_not_in_S:
      old_node = (v, d_s[v])
      d_s[v], p_s[v] = relax(u, v, G[u][v]["weight"], d_s, p_s)
      
      # parametr d sąsiadów węzła u się zmienia, dlatego też należy zmodyfikować wartość d niegotowego węzła
      uncompleted_nodes[uncompleted_nodes.index(old_node)] = (v, d_s[v])
  
  return d_s, p_s


# metoda pomocnicza wypisująca najkrótsze ścieżki dla danego wierzchołka,
# korzysta z algorytmu Dijkstry
# @param G - graf
# @param s - wierzchołek startowy 
def print_shortest_paths(G, s):
  d_s, p_s = dijkstra(G, s)

  # pętla wszystkich najkrótszych ścieżek w grafie
  for i, u in enumerate(p_s):
    # odwiedzone węzły w danej ścieżce, na początku iteracji i jest węzłem końcowym, 
    # więc można go wstawić na początek tablicy poprzedników
    predecessors = [i]
    current_node = u
    # element tablicy p odpowiadający wierzchołkowi startowemu to zawsze będzie None
    while current_node != None: 
      predecessors.insert(0, current_node)
      # i-ty element w tablicy p wskazuje poprzednika i-tego węzła
      current_node = p_s[current_node] 
    
    print(f'd({i}) = {d_s[i]} ==> {predecessors}')
