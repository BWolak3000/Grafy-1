from math import inf
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
import sys 
sys.path.append('..')

from zestaw2.zestaw2_zad1_zad2 import Zestaw2_zad1_zad2

# try:
#     import Graph
# except:
#     import projekty.Graph

class Z3Zad1:
  # ZADANIE 1 -------------------------------------------------------
  # Korzystajac z programów z poprzednich zestawów wygenerowac spójny
  # graf losowy. Przypisac kazdej krawedzi tego grafu losowa wage bedaca
  # liczba naturalna z zakresu 1 do 10.
  @staticmethod
  def generate_random_graph_with_weights() -> nx.Graph:
    # przyklad ciągu graficznego
    # TODO Ładniej to zrobić, np. wczytywać dane z pliku i na ich podstawie tworzyć graf
    # TODO sprawdzić w tej metodzie spójność generowanego grafu
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

    # dodawanie wag do krawędzi
    for u, v in G.edges:
      G[u][v]["weight"] = random.randint(1,10)

    return G

  # Nadanie wartosci poczatkowych atrybutów d oraz p dla wierzchołków grafu G
  # @param G - graf wejściowy
  # @param s - wybrany wierzchołek-źródło (numer wierzchołka jest jednocześnie indeksem w tablicy wierzchołków)
  @staticmethod
  def init_d_p(G, s):
    d_s = [inf for _ in range(len(G.nodes))]
    p_s = [None for _ in range(len(G.nodes))]
    
    d_s[s] = 0

    return d_s, p_s

  # Relaksacja krawędzi
  # @param u, v - wierzchołki połączone krawędzią
  # @param w - waga krawędzi (u, v)
  @staticmethod
  def relax(u, v, w, d_s, p_s):
    if d_s[v] > d_s[u] + w:
      d_s[v] = d_s[u] + w
      p_s[v] = u
    
    return d_s[v], p_s[v]

  # ZADANIE 2 -----------------------------------------------------------
  # Zaimplementowac algorytm Dijkstry do znajdowania najkrótszych sciezek
  # od zadanego wierzchołka do pozostałych wierzchołków i zastosowac
  # go do grafu z zadania pierwszego, w którym wagi krawedzi interpretowane
  # sa jako odległosci wierzchołków. Wypisac wszystkie najkrótsze
  # sciezki od danego wierzchołka i ich długosci.

  # Algorytm Dijkstry - Zadanie 2
  # @param G - graf
  # @param s - wierzchołek startowy 
  @staticmethod
  def dijkstra(G, s) -> None:
    d_s, p_s = Z3Zad1.init_d_p(G, s)
    
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
        d_s[v], p_s[v] = Z3Zad1.relax(u, v, G[u][v]["weight"], d_s, p_s)
        
        # parametr d sąsiadów węzła u się zmienia, dlatego też należy zmodyfikować wartość d niegotowego węzła
        uncompleted_nodes[uncompleted_nodes.index(old_node)] = (v, d_s[v])
    
    return d_s, p_s

  # metoda pomocnicza wypisująca najkrótsze ścieżki dla danego wierzchołka,
  # korzysta z algorytmu Dijkstry
  # @param G - graf
  # @param s - wierzchołek startowy 
  @staticmethod
  def print_shortest_paths(G, s):
    d_s, p_s = Z3Zad1.dijkstra(G, s)

    print(p_s)

    # pętla wszystkich najkrótszych ścieżek w grafie
    for u, i in enumerate(p_s):
      predecessors = [] # odwiedzone węzły w danej ścieżce
      current_node = u
      while current_node != None: # pierwszy element tablicy p to zawsze będzie None lub 0
        predecessors.insert(current_node, 0)
        current_node = p_s[current_node] # i-ty element w tablicy p wskazuje poprzednika i-tego węzła
      
      predecessors.insert(current_node, 0) # pętla while nie wstawi nam węzła początkowego - musimy to zrobić ręcznie

      print(f'd({i}) = d({d_s[i]}) ==> {predecessors}')

  @staticmethod
  def main():
    # wygenerowanie grafu losowego spójnego z wagami
    G = Z3Zad1.generate_random_graph_with_weights()
    # print(G.edges) # krotka z wierzchołkami połączonymi ze sobą
    
    # rysowanie grafu
    pos = nx.circular_layout(G)
    ax = plt.gca()
    ax.set_title('Zadanie 1 | Graf spójny losowy z wagami')
    nx.draw(G, pos, node_color="gold", with_labels=True, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"), ax=ax, font_color='blue')
    _ = ax.axis('off')
    plt.draw()
    plt.show()


if __name__ == "__main__":
    Z3Zad1.main()