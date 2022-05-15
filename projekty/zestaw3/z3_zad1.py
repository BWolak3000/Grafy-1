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
  def dijkstra(G, s):
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

  # ZADANIE 3 -------------------------------------------------------
  # Wyznaczyc macierz odległosci miedzy wszystkimi parami wierzchołków
  # na tym grafie.
  @staticmethod
  def distance_matrix_from_graph(G):
    dist_m = np.zeros((len(G.nodes), len(G.nodes)), dtype=np.int32)

    for i, u in enumerate(G.nodes):
      dist_m[i] = Z3Zad1.dijkstra(G, u)[0]

    return dist_m

  # ZADANIE 4 ------------------------------------------------------------
  # Wyznaczyc centrum grafu, to znaczy wierzchołek, którego suma odległosci
  # do pozostałych wierzchołków jest minimalna. Wyznaczyc centrum
  # minimax, to znaczy wierzchołek, którego odległosc do najdalszego
  # wierzchołka jest minimalna.
  @staticmethod
  def graph_center(G):
    distance_matrix = Z3Zad1.distance_matrix_from_graph(G)

    row_sums = np.array([np.sum(node_distances) for node_distances in distance_matrix], dtype=np.int32)

    min_sum = np.min(row_sums)
    #  węzeł o minimalnej sumie oraz minimalna suma
    return list(row_sums).index(min_sum), min_sum

  @staticmethod
  def minimax_center(G):
    distance_matrix = Z3Zad1.distance_matrix_from_graph(G)

    min_max_distances = np.array([np.max(distances_from_node) for distances_from_node in distance_matrix], dtype=np.int32)

    minimax_distance = np.min(min_max_distances)
    # węzeł o minimalnej największej odległości oraz minimalna największa odległość
    return list(min_max_distances).index(minimax_distance), minimax_distance

  # ZADANIE 5 -----------------------------------
  # minimalne drzewo rozpinające (metoda Kruskala)
  @staticmethod
  def minimal_spining_tree(G):
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

  @staticmethod
  def main():
    # wygenerowanie grafu losowego spójnego z wagami
    G = Z3Zad1.generate_random_graph_with_weights()
    
    # ZADANIE 2
    s = 4 # wierzchołek, po którym wyszukuje się najkrótsze ścieżki
    print(f"Najkrótsze ścieżki dla s = {s}:")
    Z3Zad1.print_shortest_paths(G, s)

    # ZADANIE 3
    distance_matrix = Z3Zad1.distance_matrix_from_graph(G)
    print(f"Macierz odległości:\n {distance_matrix}")

    # ZADANIE 4
    center, center_sum = Z3Zad1.graph_center(G)
    print(f"Centrum: {center} (suma odległości: {center_sum})")

    minimax, minimax_distance = Z3Zad1.minimax_center(G)
    print(f"Centrum minimax: {minimax} (odległość od najdalszego: {minimax_distance})")

    # ZADANIE 5
    T = Z3Zad1.minimal_spining_tree(G)

    # rysowanie oryginalnego grafu
    pos = nx.spring_layout(G) # na tym layoucie najlepiej widać wagi i drzewa rozpinające
    ax = plt.gca()
    ax.set_title('Wylosowany graf spójny losowy z wagami')
    nx.draw(G, pos, node_color="gold", with_labels=True, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"), ax=ax, font_color='blue')
    _ = ax.axis('off')
    plt.draw()
    plt.show()

    # rysowanie drzewa rozpinającego
    pos = nx.spring_layout(G)
    ax = plt.gca()
    ax.set_title('Minimalne drzewo rozpinające wylosowanego grafu')
    
    nx.draw_networkx_nodes(G, pos, node_color='gold', ax=ax)
    nx.draw_networkx_edges(T, pos, edge_color="red", ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=list(filter(lambda e: e not in T.edges, G.edges)), ax=ax)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"), ax=ax, font_color='blue')
    _ = ax.axis('off')
    plt.draw()
    plt.show()



if __name__ == "__main__":
    Z3Zad1.main()