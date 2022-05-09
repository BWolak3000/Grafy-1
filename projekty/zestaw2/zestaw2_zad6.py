import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2
from zestaw2_zad3 import Zestaw2_zad3
from zestaw2_zad4 import Zestaw2_zad4
import random


class Zestaw2_zad6:

    @staticmethod
    def is_first_connected_with_last(G, path):
        # sprawdzam czy pierwszy node na path ma połączenie z ostatnim
        edges = G.edges(path[0])
        for edge in edges:
            if edge[1] == path[len(path) - 1]:
                return True
        return False

    @staticmethod
    def have_all_vertices(visited):
        if all(visited[i] == True for i in range(0, len(visited))):
            return True
        return False

    @staticmethod
    def hamilton_method(current, G, path, visited):
        # is_hamilton = False
        path.append(current)  # pierwszy wierzcholek
        visited[current] = True
        print("CURRENT " + str(current) + " VISITED " + str(visited) + " PATH " + str(path))
        if Zestaw2_zad6.have_all_vertices(visited):
            if Zestaw2_zad6.is_first_connected_with_last(G, path):
                path.append(path[0])  # teraz jest cyklem
                return True, path, visited
            else:
                path.pop()
                visited[current] = False
                return False, path, visited
        else:

            for edge in G.edges(current):
                if visited[edge[1]]:
                    continue
                print("EDGE " + str(edge))
                is_hamilton, path, visited = Zestaw2_zad6.hamilton_method(edge[1], G, path, visited)
                if is_hamilton:
                    return is_hamilton, path, visited
        path.pop()
        visited[current] = False
        return False, path, visited

    @staticmethod
    def is_hamilton_graph(G):
        if any(G.degree[node] <= 1 for node in G.nodes()):
            return False, None
        if Zestaw2_zad4.is_graph_consistent(G):
            current = 0
            visited = [False for x in range(0, len(G.nodes()))]
            path = []
            path.append(current)  # pierwszy wierzcholek
            visited[current] = True
            print(G.edges(current))
            for edge in G.edges(current):
                print("CURRENT " + str(current) + " EDGE " + str(edge) + " VISITED " + str(visited) + " PATH " + str(
                    path))
                is_hamilton, path, visited = Zestaw2_zad6.hamilton_method(edge[1], G, path, visited)
                if is_hamilton:
                    return is_hamilton, path
            return is_hamilton, path
        return False, None

    @staticmethod
    def get_random_graph():
        while True:
            number_of_v = random.randint(3, 8)
            print(number_of_v)
            # random degree sequence
            degree_sequence = []
            for i in range(0, number_of_v):
                degree_sequence.append(random.randint(1, number_of_v))
            print(degree_sequence)
            # ponizsza metoda sprawdza czy degree sequence jest graficzny jak i czy jest realizowalny przy pomocą grafu prostego, spojnego
            if nx.is_valid_degree_sequence_havel_hakimi(degree_sequence):
                break
        return nx.havel_hakimi_graph(degree_sequence)

    @staticmethod
    def main(args):
        G = Zestaw2_zad6.get_random_graph()

        # #Test dla grafu hamiltonowskiego
        # adj_matrix = [[0, 1, 0, 1, 0],
        #             [1, 0, 1, 1, 1],
        #             [0, 1, 0, 0, 1],
        #             [1, 1, 0, 0, 1],
        #             [0, 1, 1, 1, 0], ]
        # adj_matrix_np = np.matrix(adj_matrix)
        # G = nx.from_numpy_matrix(adj_matrix_np)

        ax = plt.gca()
        is_hamilton, path = Zestaw2_zad6.is_hamilton_graph(G)
        if is_hamilton:
            ax.set_title('Zadanie 6 | Graf losowy hamiltonowski o cyklu ' + str(path))
        else:
            ax.set_title('Zadanie 6 | Graf losowy nie hamiltonowski')
        nx.draw(G, pos=nx.circular_layout(G), node_color="red", with_labels=True, ax=ax)
        _ = ax.axis('off')
        plt.draw()
        plt.show()


if __name__ == "__main__":
    Zestaw2_zad6.main([])
