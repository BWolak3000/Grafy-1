import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from zestaw2_zad1_zad2 import Zestaw2_zad1_zad2


class Zestaw2_zad3:

    # ZADANIE 3 ---------------------------------------------------------
    # Napisac program do znajdowania najwiekszej spójnej składowej na grafie.

    # Funkcja ma na celu przeszukanie w głab zaczynajac
    # od danego numeru wierzchołka v.
    @staticmethod
    def components_R(nr, v,  G, dictionary):
        # przechodzimy po każdej krawędzi wychodzącej z wierzchołka v
        for edge in G.edges(v):
            # u to sąsiad v
            u = edge[1]
            idx = None

            # pętla do znalezienia indeksu wierzchołka u w dictionary
            for temp_idx in dictionary:
                if dictionary[temp_idx][0] == u:
                    idx = temp_idx
                    break

            # komponent -1 oznacza ze ten wierzchołek nie był jeszcze odwiedzony,
            # zatem przyporządkoujemy mu numer komponentu i kontynuujemy rekurencyjnie przeszukiwanie dopóki nie są odwiedzone wszystkie wierzchołki
            if dictionary[idx][1] == -1:
                temp = dictionary[idx][0]
                dictionary[idx] = (temp, nr)
                Zestaw2_zad3.components_R(nr, dictionary[idx][0], G, dictionary)

    #Funkcja zwracająca wierzchołki z przyporządkowymi numerami komponentów (spójnych składowych do których należą)
    @staticmethod
    def components(G):
        nr = 0
        size = len(G.nodes())
        keys = [i for i in range(0,size)]
        values = [ (v,0) for v in G.nodes()]
        # dictionary przechowuje index(od 0 do n-1): [numer wierzchołka, numer komponentu]
        # w zadaniu 3 nie ma to znaczenia, ale funkcja jest użyta też w zadaniu 4 po usuwaniu wierzchołków (i w grafie jest np. 5 wierzchołków: [0,1,2,5,6])
        # Przykład --> 0:(0,1), 1:(1,1), 2:(2,2), 3:(5,2), 4:(6,2)
        dictionary = dict(zip(keys, values))

        #najpierw zaznaczamy wszystkie wierzchołki jako nieodwiedzone, czyli -1
        for idx in keys:
            temp = dictionary[idx][0]
            dictionary[idx] = (temp, -1)
        # przechodzimy po wszystkich wierzchołkach
        for idx in keys:
            # jeżeli wierzchołek nie jest jeszcze przyporządkowany, to przyporzadkowujemy mu nowy numer składowej
            if dictionary[idx][1] == -1:
                nr = nr + 1
                temp= dictionary[idx][0]
                dictionary[idx] = (temp, nr)
                # a następnie przeszukujemy w głąb zaczynając od tego wierzchołka,
                # aby oznaczyć wszystkie wierzchołki w spójnej składowej tym samym numerem komponentu
                Zestaw2_zad3.components_R(nr, dictionary[idx][0], G, dictionary)
        return dictionary

    #Funkcja znajdująca największy komponent i drukująca na konsolę listę wierzchołków należących do niego
    @staticmethod
    def find_and_print_biggest_component(comp):
        array = np.array(comp)
        # unique - tablica numerów komponentów
        # counts - tablica przechowująca liczbę wierzchołków komponentu o tym samym indeksie w tablicy (indeksie, nie wartości!)
        unique, counts = np.unique(array, return_counts=True)
        print('Lista wierzcholkow w najwiekszej spojnej skladowej: ', end=' ')

        # max_idx - pobieramy indeks komponentu, który ma najwięcej wierzchołków
        max_idx = np.argmax(counts)
        for idx_comp in range(0, len(comp)):
            # wypisujemy każdy wierzchołek, który należy do tego komponentu
            if comp[idx_comp] == unique[max_idx]:
                print(idx_comp, end=' ')

    @staticmethod
    def main(args):
        # input: sekwencja stopni wierzchołków
        # degree_sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
        degree_sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2, 2, 2, 2]

        # wykorzystanie funkcji z zadania 1, która zwraca macierz sąsiedztwa adj_matrix, jeżeli ciąg jest graficzny
        is_graph_sequence, adj_matrix = Zestaw2_zad1_zad2.is_graphical(degree_sequence)

        if is_graph_sequence:
            print("Jest graficzny!")

            # z macierzy sąsiedztwa tworzę graf
            adj_matrix_np = np.matrix(adj_matrix)
            G = nx.from_numpy_matrix(adj_matrix_np)

            # przyporządkowujemy każdemu wierzchołkowi numer komponentu do którego należy
            dictionary = Zestaw2_zad3.components(G)

            # do tabeli comp dodajemy numer komponentu, tak by indeksy w tabeli comp odpowiadały numerom wierzchołków,
            # które będziemy kolorować (bo key w dictionary są właśnie w takiej kolejnosci 0...n-1)
            comp = []
            for key in dictionary:
                comp.append(dictionary[key][1])

            # drukujemy największy komponent na konsolę
            Zestaw2_zad3.find_and_print_biggest_component(comp)

            ax = plt.gca()
            ax.set_title('Zadanie 3 | Spójne składowe na grafie')

            #rysujemy graf kolorując wierzchołki w spójnych składowych na jeden kolor
            nx.draw(G, pos=nx.circular_layout(G), node_color=comp, with_labels=True, ax=ax)
            _ = ax.axis('off')
            plt.draw()
            plt.show()
        else:
            print("Nie jest graficzny!")


if __name__ == "__main__":
    Zestaw2_zad3.main([])
