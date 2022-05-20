import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

try:
  from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2
  from zestaw2_zad3 import Zestaw2_zad3
  from zestaw2_zad4 import Zestaw2_zad4
except:
  from zestaw2.zestaw2_zad1_zad2 import Zestaw2_zad1_zad2
  from zestaw2.zestaw2_zad3 import Zestaw2_zad3
  from zestaw2.zestaw2_zad4 import Zestaw2_zad4

# ZADANIE 5 ---------------------------------------------------------
# 5. Napisac program do generowania losowych grafów k-regularnych.

class Zestaw2_zad5:

    # Funkcja zwracająca k-regularny graf o zadanej liczbie wierzchołków n i k
    @staticmethod
    def get_random_k_regular_graph(n, k):
        # k-regularność oznacza, że ciąg stopni wierzchołków to liczba k powtórzona n razy w tablicy o długości n
        degree_seq = [k for x in range(n)]

        #korzystamy z programu napisanego w zadaniu 1 i zwracanej macierzy sąsiedztwa
        flag, adj_matrix = Zestaw2_zad1_zad2.is_graphical(degree_seq)
        if flag:
            print("Jest graficzny!")
            adj_matrix_np = np.matrix(adj_matrix)
            G = nx.from_numpy_matrix(adj_matrix_np)

            # ze wzgledu na to, ze metoda z zadania 1 zwraca zawsze tą samą macierz dla zadanego ciągu,
            # wykonana zostaje randomizacja krawędzi losową ilość razy (maksymalnie n)
            number = random.randint(0, n)  # losuję ile razy graf zostanie zmodyfikowany (losowe zmienianie krawędzi)
            G = Zestaw2_zad1_zad2.randomize_graph_adj_matrix(G, number)
            return G
        else:
            print("Nie jest graficzny!")
            return None


    @staticmethod
    def main(args):
        # n - liczba wierzchołków w grafie
        # k - regularnośc
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
