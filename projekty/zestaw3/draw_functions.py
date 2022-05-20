import networkx as nx
import matplotlib.pyplot as plt

# funkcja rysująca graf z wagami
# @param G - graf, który ma być narysowany
def graph_with_weights(G):
  pos = nx.spring_layout(G) # na tym layoucie najlepiej widać wagi i drzewa rozpinające
  ax = plt.gca()
  ax.set_title('Wylosowany graf spójny losowy z wagami')
  nx.draw(G, pos, node_color="gold", with_labels=True, ax=ax)
  nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"), ax=ax, font_color='blue')
  _ = ax.axis('off')
  plt.draw()
  plt.show()


# funkcja rysująca graf wraz z jego drzewem rozpinającym
# @param G - główny graf
# @param T - drzewo rozpinające
def graph_with_spanning_tree(G, T):
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
