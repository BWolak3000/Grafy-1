import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2
from zestaw2_zad3 import Zestaw2_zad3
import random


# ZADANIE 4 ---------------------------------------------------------
# Uzywajac powyzszych programów napisac program do tworzenia losowego
# grafu eulerowskiego i znajdowania na nim cyklu Eulera.

# Cykl Eulera to zamknieta sciezka zawierajaca kazda krawedz grafu dokładnie jeden raz.
class Zestaw2_zad4:

    # Funkcja pomocnicza sprawdzająca czy graf jest spójny, zwraca typ logiczny
    @staticmethod
    def is_graph_consistent(G):

        # funkcja z zadania 3 zwraca wierzchołki z przyporządkowanymi numerami komponentów do których należą
        dictionary = Zestaw2_zad3.components(G)

        # tworzę listę komponentów, przechodzę po wszystkich wierzchołkach i dodaję ich numer komponentu
        comp = []
        for key in dictionary:
            comp.append(dictionary[key][1])

        # jezeli ilosć wystąpień pierwszego elementu listy 'comp' jest równa długości listy
        # (czyli jeżeli w liscie są elementy tylko o jednej wartości)
        # oznacza to ze graf zawiera tylko jeden komponent, czylijest spójny i zwracamy True
        result = comp.count(comp[0]) == len(comp)
        return result

    # Funkcja zwracająca losowy graf Eulerowski
    @staticmethod
    def get_random_euler_graph():
        # stopień grafu będzie miał wartosć w zakresie [3,10]
        n = random.randint(3, 10)
        degree_seq = [0 for x in range(n)]

        # n_half to maksymalny stopień który będzie wylsoowany a następnie pomnożony przez dwa
        # odejmujemy najpierw 1, by zapobiec wylosowaniu wierzchołka o stopniu równym n (np. n=10; n_half=5; stopien_wierzcholka=n_half*2=10)
        n_half = (n - 1) // 2
        flag = None
        adj_matrix = None

        while True:
            # dla każdego wierzcholka losujemy
            for idx in range(0, len(degree_seq)):
                # losujemy najpierw liczbę całkowitą, a następnie mnożymy razy 2, aby uzyskać graf Eulerowski
                # maksymalny wylosowany stopień wierzchołka jest równy ilości wierzchołków w grafie minus 1
                degree_seq[idx] = random.randint(1, n_half)
                degree_seq[idx] = degree_seq[idx] * 2
            # upewniamy się, że ciąg jest graficzny i uzyskujemy macierz sąsiedztwa, jezeli tak - wychodzimy z pętli
            flag, adj_matrix = Zestaw2_zad1_zad2.is_graphical(degree_seq)
            if flag:
                break

        print("Wylosowane stopnie wierzcholkow " + str(degree_seq))
        # graf stworzony z macierzy sąsiedztwa
        adj_matrix_np = np.matrix(adj_matrix)
        G = nx.from_numpy_matrix(adj_matrix_np)

        while True:
            # warunek konieczny grafu Eulerowskiego - graf musi być spójny
            if Zestaw2_zad4.is_graph_consistent(G):
                break
            # jeżeli nie jest - wykonujemy jednokrotną randomizację krawędzi
            G = Zestaw2_zad1_zad2.randomize_graph_adj_matrix(G, 1)
        return G

    # Funkcja pomocnicza to zwracania ścieżki eulera w formie łańcucha znaków
    @staticmethod
    def print_path_list(path_list):
        s = ""
        for idx in range(0, len(path_list) - 1):
            s = s + str(path_list[idx]) + " - "
        s = s + str(path_list[len(path_list) - 1])
        return s

    # Funkcja szukajaca ścieżki Eulera w grafie Eulera
    @staticmethod
    def find_euler_path(G_origin):
        G = G_origin.copy()
        # lista do przechowywania kolejnych wierzcholkow w sciezce
        path_list = []
        list_of_nodes = list(G.nodes())
        current_node = list_of_nodes[0]

        while current_node != None:
            # dodajemy do scieżki obecny wierzchołek
            # (został on odpowiednio wybrany w poprzedniej iteracji, więc jesteśmy pewni, ze mozna go dodać)
            path_list.append(current_node)

            # lista krawędzi wychodzących z tego obecnego wierzchołka, bo będziemy szukać kolejnego wierzchołka w ścieżce
            list_of_edges = list(G.edges(current_node))

            # jeżeli nie ma już krawędzi wychodzących z wierzchołka to kończymy pętlę
            # (bo te, po których już przeszliśmy usuwamy z grafu)
            if len(list_of_edges) == 0:
                current_node = None
                break

            # jeżeli jest jedna krawędź to mamy tylko jedną możliwość wyboru kolejnego wierzchołka
            if len(list_of_edges) == 1:
                # usuwamy obecny wierzchołek z grafu oraz krawędź z niego wychodzącą
                G.remove_node(current_node)

                # pierwsza krawędź (jedyna)
                edge = list_of_edges[0]

                # metoda G.edges(current_node) zraca krawędzie w których na ideksie 0 znajduje się current_node,
                # a na indeksie 1 - drugi wierzchołek (nie są posortowane rosnąco),
                # dlatego możemy mieć pewnośc że następnie rozważany wierzchołek znajduje się na indeksie 1 krawędzi
                current_node = edge[1]

                # i kontynuuujemy dalej pętlę
                continue

            # przechodzimy po kazdej krawędzi wychodzącej z obecnego wierzchołka
            for edge in list_of_edges:
                flag_found = False

                # robimy kopię grafu, sprawdzamy na niej czy po usunięciu danej krawędzi graf będzie spójny
                #       1. jeżeli tak - przechodzimy przez tą krawędź, czyli usuwamy ją, ustawiamy kolejny wierzchołek
                #   i przerywamy przeszukiwanie tych krawędzi dla danego wierzchołka
                #       2. jeżeli nie - oznacza to, że dana krawędź jest mostem i mozemy wybrać ją w ostateczności
                #   (ze wzgledu na brak innych znalezionych krawędzi,które nie są mostem)
                G_copy = G.copy()
                G_copy.remove_edge(edge[0], edge[1])
                if Zestaw2_zad4.is_graph_consistent(G_copy):
                    current_node = edge[1]
                    G.remove_edge(edge[0], edge[1])
                    flag_found = True
                    break

            # nie została znaleziona inna krawędź, więc wybieramy krawędź, która jest mostem,
            # usuwamy ją i ustawiamy nowy "current_node"
            if flag_found is False:
                edge = list_of_edges[0]
                G.remove_edge(edge[0], edge[1])
                current_node = edge[1]
        #znaleziona ścieżka jest zwracana
        return Zestaw2_zad4.print_path_list(path_list)

    @staticmethod
    def main(args):
        G = Zestaw2_zad4.get_random_euler_graph()
        s = Zestaw2_zad4.find_euler_path(G)

        ax = plt.gca()
        ax.set_title('Zadanie 4 | Graf eulerowski \n' + s)
        nx.draw(G, pos=nx.circular_layout(G), node_color="red", with_labels=True, ax=ax)
        _ = ax.axis('off')

        plt.draw()
        plt.show()


if __name__ == "__main__":
    Zestaw2_zad4.main([])
