import numpy as np
import random


class Node:#klasa odpowiedzialna za pojedynczy wieszcholek w grafie
    def __init__(self, label):
        self.label = str(label)
        self.edges = set()
        self.neibours = set()

    def __str__(self):# funkcja do debugowania pozwala wywolac print(n :Node) w wyniku czego otrzymujemy pritn(n.label)
        return self.label


class Edge:#klasa odpowiedzialna za pojedyncza krawedz w grafie
    def __init__(self, a, b):
        self.label = ""
        self.nodes = {a, b}
        self.start = a
        self.end = b

    def __str__(self):# funkcja do debugowania pozwala wywolac print(e :Edge)
        return str(self.start) + '-' + str(self.end)


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = set()
        self.adjastList = []
        self.adjastMatrix = []
        self.incyMatrix = []

    @staticmethod
    def from_adjastlist(adjastlist):#funkcja generuje obiekt Graph na podstawie przekazanej listy sasiedztwa
        G = Graph()
        G.nodes = [Node(_ + 1) for _ in range(len(adjastlist))]# generuje liste z odpowiedna liczba wierzcholkow
        for row in range(len(adjastlist)):
            for target in adjastlist[row]:# dla kazdej liczby w liscie sasiedztwa
                if G.nodes[row] in G.nodes[target - 1].neibours:# if target is already conected to row node
                    continue
                edge = Edge(G.nodes[row], G.nodes[target - 1])# tworze odpowiedna krawedz
                G.nodes[row].edges.add(edge)# przypisuje krawedz do jej poczatku
                G.nodes[row].neibours.add(G.nodes[target - 1])# dodaje do wieszcholka poczatkowego krawedzi informacje o nowym sasiedzie
                G.nodes[target - 1].edges.add(edge)# przypisuje krawedz do jej konca
                G.nodes[target - 1].neibours.add(G.nodes[row])# dodaje do wieszcholka koncowego krawedzi informacje o nowym sasiedzie
                G.edges.add(edge)# dodaje krawedz do zbioru wszystkich krawedzi grafu
        G.generate_representations()# generuje na podstawie formy obiektowej pozostale reprezentacje
        return G

    @staticmethod
    def from_adjastmatrix(adjastmatrix):# funkcja generuje obiekt Graph na podstawie przekazanej macierzy sasiedztwa
        G = Graph()
        G.nodes = [Node(_ + 1) for _ in range(len(adjastmatrix))]# generuje liste z odpowiedna liczba wierzcholkow
        for row in range(len(adjastmatrix)):
            start = G.nodes[row]
            for target in range(len(adjastmatrix[row])):
                if adjastmatrix[row][target] == 0:# if matrix value 0 then dont create edge between the nodes
                    continue
                end = G.nodes[target]
                if start in end.neibours:# if already connected then dont create edge between the nodes
                    continue
                edge = Edge(start, end)
                start.edges.add(edge)
                start.neibours.add(end)
                end.edges.add(edge)
                end.neibours.add(start)
                G.edges.add(edge)
        G.generate_representations()
        return G

    @staticmethod
    def from_incidencematrix(incimatrix):# funkcja generuje obiekt Graph na podstawie przekazanej macierzy incydencji
        G = Graph()
        G.nodes = [Node(_ + 1) for _ in range(len(incimatrix[0]))]# generuje liste z odpowiedna liczba wierzcholkow
        for edge_ in range(len(incimatrix)):
            startnum, endnum = [i for i, x in enumerate(incimatrix[edge_]) if x == 1]# z listy list macierzy incydencji pobiera indexy jedynek
            start = G.nodes[startnum]
            end = G.nodes[endnum]
            if start in end.neibours:  # if already connected then dont create edge between the nodes
                continue
            edge = Edge(start, end)
            start.edges.add(edge)
            start.neibours.add(end)
            end.edges.add(edge)
            end.neibours.add(start)
            G.edges.add(edge)
        G.generate_representations()
        return G

    def generate_adjast_list(self):# generuje liste sasiedztwa w formie list(list(int)) z formy obiektowej
        self.adjastList.clear()
        for node in self.nodes:# dla kazdego wierzcholka grafu
            self.adjastList.append([int(str(_)) for _ in node.neibours])# napisz liste jego sasiadow

    def generate_adjast_matrix(self):# generuje macierz sasiedztwa w formie np.array NxN z formy obiektowej
        number_of_nodes = len(self.nodes)
        self.adjastMatrix = np.zeros((number_of_nodes, number_of_nodes))
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):# dla kazdego pola w macierzy sasiedztwa
                if self.nodes[j] in self.nodes[i].neibours:# jezeli dane 2 wierzcholki sa polaczone
                    self.adjastMatrix[i][j] = 1# ustaw ta komurke na 1

    def generate_incidence_matrix(self):# generuje macierz incydencji w formie np.array NxN z formy obiektowej
        number_of_nodes = len(self.nodes)
        number_of_edges = len(self.edges)
        temp_edges_list = list(self.edges)
        self.incyMatrix = np.zeros((number_of_edges, number_of_nodes))
        iterator = 0
        for e in self.edges:#dla kazdej krawedzi w zbiorze krawedzi grafu
            index1 = self.nodes.index(e.start)
            index2 = self.nodes.index(e.end)
            self.incyMatrix[iterator][index1] = 1# ustaw 1 dla poczatku tej krawedzi
            self.incyMatrix[iterator][index2] = 1# ustaw 1 dla konca tej krawedzi
            iterator += 1

    def generate_representations(self):# dunkcja pomocnicza do wygenerowania wszystkich reprezentacji dla danego grafu
        self.generate_incidence_matrix()
        self.generate_adjast_list()
        self.generate_adjast_matrix()

    @staticmethod
    def generate_graph_nl(num_nodes, num_edges):# generuje graf losowy dla zadanej liczby wierzcholkow i liczby krawedzi
        if not isinstance(num_nodes, int):
            raise Exception("given number of nodes num_nodes={}, is not an integer".format(num_nodes))
        if not isinstance(num_edges, int):
            raise Exception("given number of edges num_deges={}, is not an integer".format(num_edges))
        if num_edges > num_nodes * (num_nodes - 1) / 2 or num_edges < 0:
            raise Exception("given number of edges num_edges={}, "
                            "is not a valid number of adges for a "
                            "graph with num_nodes={}, as it should "
                            "be in range <0, {}>".format(num_edges, num_nodes, num_nodes * (num_nodes - 1) / 2))

        # funkcja podzielona jest na dwie czesci, bezposrednio ponizej znajduje sie if ktory rodziela czesc
        # dla grafu z duza liczba krawedzi od grafu z mala

        if num_edges > num_nodes * (num_nodes - 1) / 4:# jezeli duzo krawedzi to latwiej z pelnego grafu usuwac krawedzie niz do pustego dodawac
            adjast_matrix = np.ones((num_nodes, num_nodes))#tworze plena macierz sasiedztwa
            _ = 0
            for __ in range(num_nodes):
                adjast_matrix[__][__] = 0# making sure not to connect node to itself

            while _ < num_nodes * (num_nodes - 1) / 2 - num_edges:
                i = random.randint(0, num_nodes)
                j = random.randint(0, num_nodes)
                if adjast_matrix[i][j] == 0:
                    continue
                else:
                    adjast_matrix[i][j] = 0
                    adjast_matrix[j][i] = 0
                    _ += 1# symetrycznie zamieniam odpowiednio duzo 1 na 0
            return Graph.from_adjastmatrix(adjast_matrix)

        # jezeli graf ma malo krawedzi generuje go na podstawie wylosowanej macierzy incydencji

        incidence_matrix = np.zeros((num_edges, num_nodes))
        nodes_connected = set()# zbior pomocniczy aby nie generowac duplikatow grawedzi
        _ = 0
        while _ < num_edges:
            a, b = random.sample(range(num_nodes), 2)# generuje 2 rozne indexy z przedzialu
            if (a, b) in nodes_connected or (b, a) in nodes_connected:
                continue
            incidence_matrix[_][a] = 1
            incidence_matrix[_][b] = 1
            nodes_connected.add((a, b))
            _ += 1
        return Graph.from_incidencematrix(incidence_matrix)

    @staticmethod
    def generate_graph_np(num_nodes, prob):# generuje graf losowy dla zadanej liczby wierzcholkow i prawdopodobienstwa stworzenia krawedzi
        if prob > 1 or prob < 0:
            raise Exception("probability prob = {} outside <0, 1> range".format(prob))
        # generuje przy pomocy macierzy sasiedztwa
        adjast_matrix = np.zeros((num_nodes, num_nodes))
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):# dla kazdej komorki w macierzy sasiedztwa ponizej przekatnej
                if random.random() < prob:# jak spelnie prawdopodobienstwo
                    adjast_matrix[i][j] = 1
                    adjast_matrix[j][i] = 1# dodaje symetrycznie wpis do macierzy
        return Graph.from_adjastmatrix(adjast_matrix)


def print_graf(G):# funkcja do debugowania, graf podaje na konsole
    for n in G.nodes:
        print(n)
        for e in n.edges:
            print(e, end=" ")
        print("")


if __name__ == '__main__':# main do gebugowania
    #adjlist = [[2, 5], [1, 3, 4], [5, 2, 4], [2, 3], [3, 1]]
    #G = Graph.from_adjastlist([[2, 5], [1, 3, 4], [5, 2, 4], [2, 3], [3, 1]])
    #G = Graph.from_adjastmatrix([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
    G = Graph.from_incidencematrix([[0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1]])
    G = Graph.generate_graph_nl(4, 3)
    G.generate_representations()
    G2 = Graph.from_adjastlist(G.adjastList)
    print_graf(G)
    print("==================")
    print_graf(G2)
    #print(G.adjastList)
    #print(G.adjastMatrix)
    #print(G.incyMatrix)
    #print_graf(G)

