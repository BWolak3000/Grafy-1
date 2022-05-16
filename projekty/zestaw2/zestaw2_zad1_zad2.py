import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


class Zestaw2_zad1_zad2:

    # ZADANIE 1 ---------------------------------------------------------
    # Napisac program do sprawdzania, czy dana sekwencja liczb naturalnych
    # jest ciagiem graficznym, i do konstruowania grafu prostego o stopniach
    # wierzchołków zadanych przez ciag graficzny.

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
            if list_of_vertices[0][1] > size or any(list_of_vertices[i][1] < 0 for i in range(0, size)):
                return False, None

            # przed rozpoczęciem wewnętrznej pętli wybieramy wierzchołek o największym stopniu,
            # czyli pierwszy na liście posortowanej nierosnąco
            # current_degree zawiera stopień wierzchołka
            current_degree = list_of_vertices[0][1]

            # zaczynam od łączenia z kolejnym, czyli 1 (gdyby było 0 to by było połączone ze sobą)
            i = 1
            while i <= current_degree:
                # idx1 - numer wierzchołka pierwszego który jest łączony z wierzchołkiem drugim (idx2)
                idx1 = list_of_vertices[0][0]
                idx2 = list_of_vertices[i][0]

                # kolejne kolumny, wiersze reprezentują numer wierzchołka, dlatego posługuje się indexami
                # i odbijam względem diagonali, bo graf nieskierowany
                adj_matrix1[idx1][idx2] = 1
                adj_matrix1[idx2][idx1] = 1

                # obejmuję po jednym stopniu bo są wykorzystane

                # poniżej odpowiednik operacji: list_of_vertices[i][1] = list_of_vertices[i][1] - 1
                temp = list_of_vertices[i]  # muszę zrobić temp, bo niemodyfikowalne
                list_of_vertices[i] = (temp[0], temp[1] - 1)
                i = i + 1

            # ten sam efekt co odejmowanie po stopniu w pętli wyżej,
            # zamiast tego powykorzystaniu całej wartosci obecnego stopnia - przypisuję temu wierzchołkowi warotść 0
            temp = list_of_vertices[0]
            list_of_vertices[0] = (temp[0], 0)
            # sortowanie nierosnąc opo stopniu wierzcholka, bo powyżej zmieniliśmy tamten stopień na 0 (wykorzystany)
            list_of_vertices.sort(key=lambda x: int(x[1]), reverse=True)

    # ZADANIE 2 ---------------------------------------------------------
    # Napisac program do randomizacji grafów prostych o zadanych stopniach
    # wierzchołków. Do tego celu wielokrotnie powtórzyc operacje zamieniajaca
    # losowo wybrana pare krawedzi: ab i cd na pare ad i bc.

    # Funkcja pomocnicza, sprawdzająca czy krawędzie mogą być zamienione,
    # zwraca True/False
    # edge1 i edge2 to tablica [int,int] czyli pierwszy i drugi wierzchołek w krawędzi
    @staticmethod
    def can_edges_be_switched(G, edge1, edge2):
        # sprawdzenie czy żaden wierzchołek krawędzi nie jest taki sam
        if edge1[0] != edge2[0] and edge1[0] != edge2[1] and edge1[1] != edge2[0] and edge1[1] != edge2[1]:
            # sprawdzam w grafie G czy istnieje już któraś z dwóch krawędzi, którą zamierzamy dodać do grafu
            # ma to zapobiec dodaniu krawędzi wielokrotnych
            # sprawdzenie to jest zawsze dla dwóch przypadków, bo w grafie G przechowywane są krawędzie zawsze o posortowanej kolejności wierzchołków,
            # ( tzn. może istnieć krawędź [0,9], ale nie moze istnieć krawędź [9,0] )

            if edge1[0] < edge2[1] and G.has_edge(edge1[0], edge2[1]):
                return False
            elif edge1[0] > edge2[1] and G.has_edge(edge2[1], edge1[0]):
                return False

            if (edge1[1] < edge2[0]) and G.has_edge(edge1[1], edge2[0]):
                return False
            elif (edge1[1] > edge2[0]) and G.has_edge(edge2[0], edge1[1]):
                return False

            # jeżeli wierzchołek się nie powtarza, a krawędzie jeszcze nie isteniją w grafie - zwracamy True
            return True
        return False

    # Funkcja randomizująca grafy proste zadaną ilość razy
    @staticmethod
    def randomize_graph_adj_matrix(G, number):
        # ilość krawędzi w grafie
        number_of_edges = len(G.edges())

        # flaga dla upewnienia, że graf zostanie zmodyfikowany 'number' razy
        # iterator i zwiększa sę tylko w przypadku wykonania faktycznej zmiany na grafie
        has_been_change = False
        i = 0
        while i < number:
            has_been_change = False
            list_of_edges = list(G.edges())

            # losuję indeks pierwszej i drugiej krawędzi (od zera do (ilosć krawędzi - 1) )
            edge1_idx = random.randint(0, number_of_edges - 1)
            edge2_idx = random.randint(0, number_of_edges - 1)

            # sprawdzam czy nie jest to ta sama krawędź (tzn. krawędź o tym samym indeksie)
            if edge1_idx != edge2_idx:
                # pobieram krawędzie z listy krawędzi podając wylosowany index listy
                edge1 = list_of_edges[edge1_idx]
                edge2 = list_of_edges[edge2_idx]

                # sprawdzam czy krawędzie mogą być zamienione
                if Zestaw2_zad1_zad2.can_edges_be_switched(G, edge1, edge2):
                    # usuwam obie krawędzie istniejące
                    G.remove_edge(edge1[0], edge1[1])
                    G.remove_edge(edge2[0], edge2[1])

                    # porównuję indeksy wierzchołków, by dodać zamienione krawędzie o wierzchołkach w posortowanej kolejności
                    # (ze wzgledu na użytą bibliotekę)
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
        # zwracam graf po randomizacjach
        return G

    @staticmethod
    def main(args):
        # przyklad ciągu graficznego
        # list = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
        list = [5, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
        list = [6,6,6,6,6,6]

        # przyklad ciągu niegraficznego
        # list = [4, 4, 3, 1, 2]

        # przyklad z zajec BW
        # list = [4, 4, 4, 4, 2, 2]

        # Posortuj tablice nierosnąco
        list = sorted(list, reverse=True)

        # adj_matrix - macierz sąsiedztwa
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
