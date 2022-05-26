import networkx as nx
import matplotlib.pyplot as plt
import random_digraph
import random_walk

def draw_graph(G):
  pos = nx.shell_layout(G)
  ax = plt.gca()
  ax.set_title('Wylosowany graf')
  nx.draw(G, pos, node_color="gold", with_labels=True, ax=ax)
  _ = ax.axis('off')
  plt.draw()
  plt.show()


def main():
  G = random_digraph.generate_random_digraph(7)
  d = 0.15
  N = 100000
  print(random_walk.random_walk(G,d,N))
  draw_graph(G)

if __name__ == '__main__':
  main()
