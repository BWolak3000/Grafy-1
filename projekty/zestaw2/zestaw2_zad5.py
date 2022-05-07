import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2
from zestaw2_zad3 import Zestaw2_zad3
from zestaw2_zad4 import Zestaw2_zad4
import random


class Zestaw2_zad5:

    @staticmethod
    def get_random_k_regular_graph(n, k):
        degree_seq = [k for x in range(n)]
        flag, adj_matrix = Zestaw2_zad1_zad2.isGraphical(degree_seq)
        if flag:
            print("Jest graficzny!")
            adj_matrix_np = np.matrix(adj_matrix)
            G = nx.from_numpy_matrix(adj_matrix_np)
            n = random.randint(0, 10)  # losuję ile razy graf zostanie zmodyfikowany (losowe zmienianie krawędzi)
            G = Zestaw2_zad1_zad2.randomizeGraphAdjMatrix(G, n)
            return G
        else:
            print("Nie jest graficzny!")
            return None

    @staticmethod
    def main(args):
        n = 7
        k = 2
        G = Zestaw2_zad5.get_random_k_regular_graph(n, k)
        if G != None:
            ax = plt.gca()
            ax.set_title('Zadanie 5 | Losowy graf ' + str(k) + "-regularny o " + str(n) + " wierzchołkach")
            nx.draw(G, pos=nx.circular_layout(G), node_color="red", with_labels=True, ax=ax)
            _ = ax.axis('off')
            plt.draw()
            plt.show()


if __name__ == "__main__":
    Zestaw2_zad5.main([])
