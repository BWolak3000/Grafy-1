import networkx as nx
import matplotlib.pyplot as plt
import random_digraph
import random_walk
import utils

def draw_graph(G):
  pos = nx.shell_layout(G)
  ax = plt.gca()
  ax.set_title('Wylosowany graf')
  nx.draw(G, pos, node_color="gold", with_labels=True, ax=ax)
  _ = ax.axis('off')
  plt.draw()
  plt.show()


def main():
  adj_list = random_digraph.generate_adjacency_list(10)

  print("Lista sąsiedztwa:")
  utils.print_adjacency_list(adj_list)

  G = random_digraph.generate_random_digraph(adj_list)
  d = 0.15
  N = 1000000

  print("Algorytm PageRank - błądzenie przypadkowe:")
  random_walk_probabilities = random_walk.random_walk(G,d,N)
  utils.print_page_rank(random_walk_probabilities)
  
  draw_graph(G)

if __name__ == '__main__':
  main()
