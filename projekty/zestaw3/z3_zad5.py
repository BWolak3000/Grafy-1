import networkx as nx 
  
# ZADANIE 5 -----------------------------------
# minimalne drzewo rozpinające (metoda Kruskala)

def minimal_spanning_tree(G):
  T = nx.Graph() # drzewo, które na początku jest pustym grafem 
  T.add_nodes_from(G) # będzie ono posiadało wszystkie wierzchołki pierwotnego grafu

  # krawędzie posortowane niemalejąco według wag
  sorted_edges_by_weight = sorted(G.edges, key=lambda edge: G[edge[0]][edge[1]]['weight'])
  
  for u, v in sorted_edges_by_weight:
    T.add_edge(u, v, weight=G[u][v]['weight'])

    # jeżeli dodanie krawędzi spowodowało cykle (czyli T nie jest już lasem),
    # to usuwamy dodaną krawędź
    if nx.is_forest(T) == False:
      T.remove_edge(u, v)

    # przerywamy wcześniej pętlę, gdy rozmiar drzewa rozpinającego wynosi liczba_węzłów-1
    if len(T.edges) == len(G.nodes)-1:
      break

  return T
