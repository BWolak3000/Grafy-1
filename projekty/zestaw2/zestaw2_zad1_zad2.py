import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


class Zestaw2_zad1_zad2:

    # ZADANIE 1

    # Funkcja sprawdzająca czy suma stopni wierzchołków jest parzysta
    # jest to warunek konieczny by graf był graficzny
    @staticmethod
    def is_sum_even(list):
        sum = 0
        for i in list:
            sum += i
        return sum % 2 == 0

    # Funkcja przyjmuje ciąg stopni wierzchołków
    # zwraca flagę informującą czy zadany ciąg jest graficzny
    # oraz macierz sąsiedztwa, jeżeli jest graficzny (jeżeli nie jest - zwraca None)
    @staticmethod
    def is_graphical(degree_sequence):

        size = len(degree_sequence)

        # zabezpieczenie przed podaniem pustego ciągu
        if size == 0:
            print("Nie zostal podany ciag liczb!")
            return False, None

        # wypełnienie macierzy sasiedztwa zerami
        adj_matrix1 = [[0 for x in range(size)] for y in range(size)]

        # lista wierzchołków wraz ze stopniem (przyporządkowanie stopnia do indeksu/numeru wierzołka
        list_of_vertices = [(i, degree_sequence[i]) for i in range(0, size)]

        # jeżeli nie spełniony warunek "suma stopni parzysta" zwróć False
        if not Zestaw2_zad1_zad2.is_sum_even(degree_sequence):
            return False, None

        # sortowanie nierosnąco
        list_of_vertices.sort(key=lambda x: int(x[1]), reverse=True)
        while True:
            # jeżeli wszystkie wierzchołki mają stopień 0 - jest graficzny
            if all(list_of_vertices[i][1] == 0 for i in range(0, size)):
                return True, adj_matrix1

            # implementacja kroku 5 zadanego algoytmu
            # jeżeli stopień wierzchołka o największym stopniu jest większy niż ilość wierzchołków
            # lub stopień dowolnego wierzchołka jest ujemny
            # to ciąg nie jest graficzny
            if list_of_vertices[0][1] >= size or any(list_of_vertices[i][1] < 0 for i in range(0, size)):
                return False, None

            # przed rozpoczęciem pętli wybieramy wierzchołek o największym stopniu, czyli pierwszy na liście posortowanej nierosnąco
            # current_degree zawiera stopień wierzchołka
            current_degree = list_of_vertices[0][1]

            # zaczynam od łączenia z kolejnym, czyli 1 (gdyby było 0 to by było połączone ze sobą)
            i = 1
            while i <= current_degree:
                # idx1 - numer wierzchołka pierwszego który jest łączony z wierzchołkiem drugim (idx2)
                idx1 = list_of_vertices[0][0]
                idx2 = list_of_vertices[i][0]

                # kolejne kolumny, wiersze reprezentują numer wierzchołka, dlatego posługuje się indexami
                # i odbijam względem diagonali
                adj_matrix1[idx1][idx2] = 1
                adj_matrix1[idx2][idx1] = 1

                # obejmuję po jednym stopniu bo są wykorzystane

                # list_of_vertices[0][1] = list_of_vertices[0][1] - 1 #to będzie już niżej = 0
                temp = list_of_vertices[i]  # muszę zrobić temp, bo to tuple (niemodyfikowalne)
                list_of_vertices[i] = (temp[0], temp[1] - 1)
                i = i + 1
            temp = list_of_vertices[0]
            list_of_vertices[0] = (temp[0], 0)
            list_of_vertices.sort(key=lambda x: int(x[1]), reverse=True)  # sortowanie po stopniu wierzcholka

    @staticmethod
    def can_edges_be_switched(G, edge1, edge2):
        if edge1[0] != edge2[0] and edge1[0] != edge2[1] and edge1[1] != edge2[0] and edge1[1] != edge2[1]:
            if edge1[0] < edge2[1] and G.has_edge(edge1[0], edge2[1]):
                return False
            elif edge1[0] > edge2[1] and G.has_edge(edge2[1], edge1[0]):
                return False
            if (edge1[1] < edge2[0]) and G.has_edge(edge1[1], edge2[0]):
                return False
            elif (edge1[1] > edge2[0]) and G.has_edge(edge2[0], edge1[1]):
                return False
            return True
        return False

    # ZADANIE 2

    @staticmethod
    def randomize_graph_adj_matrix(G, number):
        number_of_edges = len(G.edges())

        # flaga dla upewnienia, że graf zostanie zmodyfikowany 'number' razy
        # iterator i zwiększa sę tylko w przypadku wykonania faktycznej zmiany na grafie
        has_been_change = False
        i = 0
        while i < number:
            has_been_change = False
            list_of_edges = list(G.edges())
            #indeksy krawędzi, czyli numery wierzchołka pierwszego i drugiego
            edge1_idx = random.randint(0, number_of_edges - 1)
            edge2_idx = random.randint(0, number_of_edges - 1)
            if edge1_idx != edge2_idx:
                edge1 = list_of_edges[edge1_idx]
                edge2 = list_of_edges[edge2_idx]
                if Zestaw2_zad1_zad2.can_edges_be_switched(G, edge1, edge2):
                    G.remove_edge(edge1[0], edge1[1])
                    G.remove_edge(edge2[0], edge2[1])
                    if edge1[0] < edge2[1]:
                        G.add_edge(edge1[0], edge2[1])
                    else:
                        G.add_edge(edge2[1], edge1[0])
                    if edge1[1] < edge2[0]:
                        G.add_edge(edge1[1], edge2[0])
                    else:
                        G.add_edge(edge2[0], edge1[1])
                    has_been_change = True
            if has_been_change:
                i = i + 1
        return G

    @staticmethod
    def main(args):
        # przyklad ciągu graficznego
        list = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]

        # przyklad ciągu niegraficznego
        # list = [4, 4, 3, 1, 2]

        # Posortuj tablice nierosnąco
        list = sorted(list, reverse=True)

        #
        is_graph_sequence, adj_matrix = Zestaw2_zad1_zad2.is_graphical(list)
        if is_graph_sequence:
            # zad1
            print("Jest graficzny!")

            # plot zad1
            adj_matrix_np = np.matrix(adj_matrix)
            G = nx.from_numpy_matrix(adj_matrix_np)
            ax = plt.gca()
            ax.set_title('Zadanie 1 | Graf prosty o podanych stopniach wierzchołków')
            nx.draw(G, pos=nx.circular_layout(G), node_color="red", with_labels=True)
            _ = ax.axis('off')
            plt.draw()
            plt.show()

            # zad2
            G = Zestaw2_zad1_zad2.randomize_graph_adj_matrix(G, 10)
            ax = plt.gca()
            ax.set_title('Zadanie 2 | Graf po 10 modyfikacjach')
            nx.draw(G, pos=nx.circular_layout(G), node_color="red", with_labels=True, ax=ax)
            _ = ax.axis('off')
            plt.draw()
            plt.show()
        else:
            print("Nie jest graficzny!")


if __name__ == "__main__":
    Zestaw2_zad1_zad2.main([])
