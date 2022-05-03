import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from utils import Utils
from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2

class Main:

    @staticmethod
    def components_R(nr, v, G, comp):
        for edge in G.edges(v):
            u = edge[1]
            if comp[u] == -1:
                comp[u] = nr
                Main.components_R(nr, u, G, comp)

    @staticmethod
    def components(G):
        nr = 0
        size = len(G.nodes())
        comp = [0 for x in range(size)]
        for v in G.nodes():
            comp[v] = -1
        for v in G.nodes():
            if comp[v] == -1:
                nr = nr + 1
                comp[v] = nr
                Main.components_R(nr, v, G, comp)
        return comp

    @staticmethod
    def main(args):
        list = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

        if Zestaw2_zad1_zad2.isGraphical(list):
            print("Jest graficzny!")
            adj_matrix = Utils.degree_seq_to_adj_matrix(list)
            adj_matrix_np = np.matrix(adj_matrix)
            G = nx.from_numpy_matrix(adj_matrix_np)
            comp_colors = Main.components(G)
            nx.draw(G, pos=nx.circular_layout(G), node_color=comp_colors, with_labels=True)
            plt.draw()
            plt.show()
        else:
            print("Nie jest graficzny!")

if __name__ == "__main__":
    Main.main([])
