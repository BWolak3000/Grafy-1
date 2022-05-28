import networkx as nx
import matplotlib.pyplot as plt

def save_graph_to_file(G) -> None:
  '''
  Zapisuje graf do pliku
    
    Parameters:
      G (nx.DiGraph): graf, który ma być zapisany do pliku
  '''
  pos = nx.shell_layout(G)
  ax = plt.gca()
  ax.set_title('Wylosowany graf')
  nx.draw(G, pos, node_color="gold", with_labels=True, ax=ax)
  _ = ax.axis('off')
  plt.draw()
  plt.savefig(f'graph.png')
