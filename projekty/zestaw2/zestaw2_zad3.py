import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2


class Zestaw2_zad3:

    @staticmethod
    def components_R(nr, v,  G, dictionary):
        for edge in G.edges(v):
            u = edge[1]
            idx = None
            for temp_idx in dictionary:
                if dictionary[temp_idx][0] == u:
                    idx = temp_idx
                    break
            if dictionary[idx][1] == -1:
                temp = dictionary[idx][0]
                dictionary[idx] = (temp, nr)
                Zestaw2_zad3.components_R(nr, dictionary[idx][0], G, dictionary)

    @staticmethod
    def components(G):
        nr = 0
        size = len(G.nodes())
        keys = [i for i in range(0,size)]
        values = [ (v,0) for v in G.nodes()]
        dictionary = dict(zip(keys, values))

        for idx in keys:
            temp = dictionary[idx][0]
            dictionary[idx] = (temp, -1)
        for idx in keys:
            if dictionary[idx][1] == -1:
                nr = nr + 1
                temp= dictionary[idx][0]
                dictionary[idx] = (temp, nr)
                Zestaw2_zad3.components_R(nr, dictionary[idx][0], G, dictionary)
        return dictionary

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
        flag, adj_matrix = Zestaw2_zad1_zad2.is_graphical(list)
        if flag:
            print("Jest graficzny!")
            adj_matrix_np = np.matrix(adj_matrix)
            G = nx.from_numpy_matrix(adj_matrix_np)

            dictionary = Zestaw2_zad3.components(G)
            comp = []
            for key in dictionary:
                comp.append(dictionary[key][1])

            print(comp)
            Zestaw2_zad3.find_and_print_biggest_component(comp)

            ax = plt.gca()
            ax.set_title('Zadanie 3 | Spójne składowe na grafie')
            nx.draw(G, pos=nx.circular_layout(G), node_color=comp, with_labels=True, ax=ax)
            _ = ax.axis('off')
            plt.draw()
            plt.show()
        else:
            print("Nie jest graficzny!")


if __name__ == "__main__":
    Zestaw2_zad3.main([])
