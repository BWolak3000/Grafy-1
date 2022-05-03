import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from utils import Utils

class Zestaw2_zad1_zad2:
    @staticmethod
    def isSumEvenWhenOddNumberOfVertices(list):
        sum = 0
        for i in list:
            sum += i
        return sum % 2 == 0

    @staticmethod
    def isGraphical(list):
        if len(list) == 0:
            print("Nie zostal podany ciag liczb!")
            return False

        if not Zestaw2_zad1_zad2.isSumEvenWhenOddNumberOfVertices(list):
            return False

        list = sorted(list, reverse=True)

        c = 0
        while True:
            c += 1
            if all(item == 0 for item in list):
                return True
            if list[0] >= len(list) or any(item < 0 for item in list):
                return False
            i = 1
            while i <= list[0]:
                list[i] = list[i] - 1
                i = i + 1

            list[0] = 0
            list = sorted(list, reverse=True)

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
        # listOfEdges = list(G.edges(data=True))
        # jeszcze dołożyć flagę czy byla zmiana bo chyba to skutku
        has_been_change = False
        i = 0
        while i < number:
            has_been_change = False
            listOfEdges = list(G.edges())
            print(listOfEdges)
            edge1Idx = random.randint(0, numberOfEdges - 1)
            edge2Idx = random.randint(0, numberOfEdges - 1)
            print(edge1Idx)
            print(edge2Idx)
            if edge1Idx != edge2Idx:
                edge1 = listOfEdges[edge1Idx]
                edge2 = listOfEdges[edge2Idx]
                if Zestaw2_zad1_zad2.can_edges_be_switched(G, edge1, edge2):
                    G.remove_edge(edge1[0], edge1[1])
                    G.remove_edge(edge2[0], edge2[1])
                    # print('edge ' +str(edge1) + ' ' +str(edge2))
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
        # list = sorted(list, reverse=True)

        if Zestaw2_zad1_zad2.isGraphical(list):
            # zad1
            print("Jest graficzny!")
            adj_matrix = Utils.degree_seq_to_adj_matrix(list)

            # plot zad1
            adj_matrix_np = np.matrix(adj_matrix)
            G = nx.from_numpy_matrix(adj_matrix_np)
            nx.draw(G, pos=nx.circular_layout(G), node_color="red", with_labels=True)
            plt.draw()
            plt.show()

            # zad2
            G2 = Zestaw2_zad1_zad2.randomizeGraphAdjMatrix(G, 10)
            nx.draw(G2, pos=nx.circular_layout(G2), node_color="red", with_labels=True)
            plt.draw()
            plt.show()
        else:
            print("Nie jest graficzny!")


if __name__ == "__main__":
    Zestaw2_zad1_zad2.main([])
