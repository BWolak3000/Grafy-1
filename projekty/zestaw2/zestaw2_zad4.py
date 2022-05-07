import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2
from zestaw2_zad3 import Zestaw2_zad3
import random


class Zestaw2_zad4:

    @staticmethod
    def is_graph_consistent(G):
        dictionary = Zestaw2_zad3.components(G)
        comp = []
        for key in dictionary:
            comp.append(dictionary[key][1])

        result = comp.count(comp[0]) == len(comp)
        if (result):
            return True
        return False

    @staticmethod
    def get_random_euler_graph():
        n = random.randint(3, 10)
        degree_seq = [0 for x in range(n)]
        n_half = n // 2
        flag = None
        adj_matrix = None
        while True:
            for idx in range(0, len(degree_seq)):
                degree_seq[idx] = random.randint(1, n_half)
                degree_seq[idx] = degree_seq[idx] * 2
            flag, adj_matrix = Zestaw2_zad1_zad2.isGraphical(degree_seq)
            if flag:
                break
        print("Wylosowane stopnie wierzcholkow " + str(degree_seq))
        adj_matrix_np = np.matrix(adj_matrix)
        G = nx.from_numpy_matrix(adj_matrix_np)
        while True:
            if Zestaw2_zad4.is_graph_consistent(G):
                break
            G = Zestaw2_zad1_zad2.randomizeGraphAdjMatrix(G, 1)
        return G

    @staticmethod
    def print_path_list(path_list):
        for idx in range(0,len(path_list)-1):
            print(path_list[idx], end=' - ')
        print(path_list[len(path_list)-1])

    @staticmethod
    def find_euler_path(G_origin):
        G = G_origin.copy()
        path_list = []
        list_of_nodes = list(G.nodes())
        current_node = list_of_nodes[0]

        while current_node != None:
            path_list.append(current_node)
            list_of_edges = list(G.edges(current_node))
            if len(list_of_edges) == 0:
                current_node = None
                break
            if len(list_of_edges) == 1:
                G.remove_node(current_node)
                edge = list_of_edges[0]
                current_node = edge[1]
                continue
            for edge in list_of_edges:
                flag_found = False
                G_copy = G.copy()
                G_copy.remove_edge(edge[0], edge[1])
                if Zestaw2_zad4.is_graph_consistent(G_copy):
                    current_node = edge[1]
                    G.remove_edge(edge[0], edge[1])
                    flag_found = True
                    break
                if flag_found:
                    break
            if flag_found is False:
                edge = list_of_edges[0]
                G.remove_edge(edge[0], edge[1])
                current_node = edge[1]
        Zestaw2_zad4.print_path_list(path_list)


    @staticmethod
    def main(args):
        G = Zestaw2_zad4.get_random_euler_graph()
        Zestaw2_zad4.find_euler_path(G)

        ax = plt.gca()
        ax.set_title('Zadanie 4 | Graf eulerowski')
        nx.draw(G, pos=nx.circular_layout(G), node_color="red", with_labels=True, ax=ax)
        _ = ax.axis('off')

        plt.draw()
        plt.show()


if __name__ == "__main__":
    Zestaw2_zad4.main([])
