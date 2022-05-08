import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


class Zestaw2_zad1_zad2:
    @staticmethod
    def isSumEvenWhenOddNumberOfVertices(list):
        size = len(list)
        if size % 2 == 0:
            return True

        sum = 0
        for i in list:
            sum += i
        return sum % 2 == 0

    @staticmethod
    def isGraphical(degree_sequence):
        # lista wierzcholkow z ich stopniami
        size = len(degree_sequence)

        if size == 0:
            print("Nie zostal podany ciag liczb!")
            return False, None

        adj_matrix1 = [[0 for x in range(size)] for y in range(size)]
        list_of_vertices = [(i, degree_sequence[i]) for i in range(0, size)]
        if not Zestaw2_zad1_zad2.isSumEvenWhenOddNumberOfVertices(degree_sequence):
            return False, None
        list_of_vertices.sort(key=lambda x: int(x[1]), reverse=True)
        while True:
            if all(list_of_vertices[i][1] == 0 for i in range(0, size)):
                return True, adj_matrix1
            if list_of_vertices[0][1] >= size or any(list_of_vertices[i][1] < 0 for i in range(0, size)):
                return False, None

            current_degree = list_of_vertices[0][1]  # bo będzie największy stopień

            #zaczynam od łaczenia z kolejnym, gdyby było 0 to by było połączone ze sobą
            i = 1
            while i <= current_degree:
                # idx1 - numer wierzcholka pierwszego który jest łączony z wiezchołkiem drugim (idx2)
                idx1 = list_of_vertices[0][0]
                idx2 = list_of_vertices[i][0]

                # kolejne kolumny, wiersze reprezentują numer wierzchołka, latego posługuje się indexami
                adj_matrix1[idx1][idx2] = 1
                adj_matrix1[idx2][idx1] = 1

                # obejmuję po jednym stopniu bo są wykorzystane
                # list_of_vertices[0][1] = list_of_vertices[0][1] - 1 #to będzie już niżej = 0
                temp = list_of_vertices[i]
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

    @staticmethod
    def randomizeGraphAdjMatrix(G, number):
        numberOfEdges = len(G.edges())
        has_been_change = False
        i = 0
        while i < number:
            has_been_change = False
            listOfEdges = list(G.edges())
            edge1Idx = random.randint(0, numberOfEdges - 1)
            edge2Idx = random.randint(0, numberOfEdges - 1)
            if edge1Idx != edge2Idx:
                edge1 = listOfEdges[edge1Idx]
                edge2 = listOfEdges[edge2Idx]
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
        list = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
        # list = [4, 2, 4, 2, 4, 2]
        list = sorted(list, reverse=True)
        flag, adj_matrix = Zestaw2_zad1_zad2.isGraphical(list)
        if flag:
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
            G = Zestaw2_zad1_zad2.randomizeGraphAdjMatrix(G, 10)
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
