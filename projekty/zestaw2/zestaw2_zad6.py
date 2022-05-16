import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2
from zestaw2_zad3 import Zestaw2_zad3
from zestaw2_zad4 import Zestaw2_zad4
import random


# ZADANIE 6 ---------------------------------------------------------
# Napisac program do sprawdzania (dla małych grafów), czy graf jest
# hamiltonowski.
class Zestaw2_zad6:

    #Funkcja sprawdzająca czy pierwszy wierzchołek ma połączenie z ostatnim
    @staticmethod
    def is_first_connected_with_last(G, path):
        edges = G.edges(path[0])
        for edge in edges:
            if edge[1] == path[len(path) - 1]:
                return True
        return False

    #Funkcja sprawdzajaca czy wszystkie wierzchołki są odwiedzone (czy w tablicy visited jest tylko wartość True)
    @staticmethod
    def have_all_vertices(visited):
        if all(visited[i] == True for i in range(0, len(visited))):
            return True
        return False

    #Funkcja rekurencyjnie wyszukująca cyklu hamiltona
    @staticmethod
    def hamilton_method(current, G, path, visited):
        # odwiedzamy wierzchołek dla którego jest wywołana metoda
        path.append(current)
        visited[current] = True

        if Zestaw2_zad6.have_all_vertices(visited):
            # jeżeli wszystkie wierzchołki są odwiedzone to sprawdzamy czy pierwszy element ze scieżki łączy się z ostatnim (czyli czy tworzy cykl hamiltona).
            # Jezeli tak - znaleźliźmy cykl.
            # Jeżeli nie- cofamy się o poziom wyżej w rekurencji.
            if Zestaw2_zad6.is_first_connected_with_last(G, path):
                path.append(path[0])  # teraz jest cyklem
                return True, path, visited
            else:
                path.pop()
                visited[current] = False
                return False, path, visited
        else:
            # jeżeli jeszcze nie wszystkie wierzchołki są odwiedzone to iterujemy po sąsiadach
            # i dla nieodwiedzonych wywołujemy rekurencyjnie metodę hamilton_method
            for edge in G.edges(current):
                if visited[edge[1]]:
                    continue
                is_hamilton, path, visited = Zestaw2_zad6.hamilton_method(edge[1], G, path, visited)
                # jeżeli już został znaleziony cykl hamiltona to przerywany pętlę zwracając is_hamilton(True) i ścieżkę
                if is_hamilton:
                    return is_hamilton, path, visited
        # jezeli nie zwróciliśmy nic w 'for loop' oznacza to że nie został znaleziony cykl hamiltona.
        # Oznaczamy wierzchołek jako nieodwiedzony i cofamy się na wyższy poziom rekurencji
        path.pop()
        visited[current] = False
        return False, path, visited

    # Funkcja sprawdzająca czy G jest grafem Hamiltona, zwraca True/False oraz ścieżkę (lub None jeżeli nie jest grafem Hamiltona)
    @staticmethod
    def is_hamilton_graph(G):
        # Jezeli stopień jakiegoś wierzchołka jest mniejszy niz 1 to zwracamy False (graf musi być spójny, a graf wejściowy ma więcej niż jeden wierzchołek)
        if any(G.degree[node] <= 1 for node in G.nodes()):
            return False, None

        # Sprawdzenie czy graf Hamiltona jest spójny
        if Zestaw2_zad4.is_graph_consistent(G):
            # ścieżkę rozpoczynamu zawsze od wierzchołka 0 (miejsce rozpoczęcia jest dowolne, ale ten wierzchołek zawsze istanieje w generowanych grafach)
            current = 0
            #tablica visited - jezeli w zadanym indeksie jest True to znaczy że wierzchołek o tym numerze był już odwiedzony (i nie będziemy go odwiedzać ponownie)
            visited = [False for x in range(0, len(G.nodes()))]
            #tablica przechowjąca ścieżkę
            path = []

            # odwiedzamy pierwszy wierzchołek
            path.append(current)  # pierwszy wierzcholek
            visited[current] = True

            # iterujemy po wszystkich krawędziach wychodzących z wierzchołka, by wywołać hamilton_method dla kazdego sąsiedniego wierzchołka
            for edge in G.edges(current):
                # print("CURRENT " + str(current) + " EDGE " + str(edge) + " VISITED " + str(visited) + " PATH " + str(
                #     path))

                is_hamilton, path, visited = Zestaw2_zad6.hamilton_method(edge[1], G, path, visited)
                #jeżeli już został znaleziony cykl hamiltona to przerywany pętlę zwracając is_hamilton(True) i ścieżkę
                if is_hamilton:
                    return is_hamilton, path
            return is_hamilton, path
        return False, None

    # Funkcja zwracająca losowy graf o liczbie wierzchołków [3,8]
    @staticmethod
    def get_random_graph():
        adj_matrix = []
        while True:
            number_of_v = random.randint(3, 8)
            print(number_of_v)
            # random degree sequence
            degree_sequence = []
            # losujemy stopień każdego wierzchołka od 1 do n-1
            for i in range(0, number_of_v):
                degree_sequence.append(random.randint(1, number_of_v - 1))
            print(degree_sequence)

            # ponizsza metoda sprawdza czy degree sequence jest graficzny jak i czy jest realizowalny przy pomocą grafu prostego, spojnego
            is_graph_sequence, adj_matrix = Zestaw2_zad1_zad2.is_graphical(degree_sequence)
            if is_graph_sequence:
                break
        adj_matrix_np = np.matrix(adj_matrix)
        return nx.from_numpy_matrix(adj_matrix_np)

    @staticmethod
    def main(args):
        # G = Zestaw2_zad6.get_random_graph()

        #Test dla grafu hamiltonowskiego
        # adj_matrix = [[0, 1, 0, 1, 0],
        #             [1, 0, 1, 1, 1],
        #             [0, 1, 0, 0, 1],
        #             [1, 1, 0, 0, 1],
        #             [0, 1, 1, 1, 0], ]
        adj_matrix = [[0,1,1,1,0,0,0,0],
                      [1,0,1,0,1,1,0,0],
                      [0,1,0,1,0,0,1,0],
                      [1,0,1,0,0,1,1,0],
                      [1,1,0,0,0,0,0,1],
                      [0,1,0,1,0,0,0,1],
                      [0,0,1,1,0,0,0,1],
                      [0,0,0,0,1,1,1,0]]
        adj_matrix_np = np.matrix(adj_matrix)
        G = nx.from_numpy_matrix(adj_matrix_np)

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
