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
    def find_and_print_biggest_component(comp):
        array = np.array(comp)
        unique, counts = np.unique(array, return_counts=True)
        print('Lista wierzcholkow w najwiekszej spojnej skladowej: ', end=' ')
        max_idx = np.argmax(counts)
        for idx_comp in range(0, len(comp)):
            if comp[idx_comp] == unique[max_idx]:
                print(idx_comp, end=' ')

    @staticmethod
    def main(args):
        list = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

        if Zestaw2_zad1_zad2.isGraphical(list):
            print("Jest graficzny!")
            adj_matrix = Utils.degree_seq_to_adj_matrix(list)
            adj_matrix_np = np.matrix(adj_matrix)
            G = nx.from_numpy_matrix(adj_matrix_np)
            comp = Main.components(G)
            Main.find_and_print_biggest_component(comp)
            nx.draw(G, pos=nx.circular_layout(G), node_color=comp, with_labels=True)
            plt.draw()
            plt.show()
        else:
            print("Nie jest graficzny!")


if __name__ == "__main__":
    Main.main([])
