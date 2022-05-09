import numpy as np
import random


class Node:
    def __init__(self, label):
        self.label = str(label)
        self.edges = set()
        self.neibours = set()

    def __str__(self):
        return self.label


class Edge:
    def __init__(self, a, b):
        self.label = ""
        self.nodes = {a, b}
        self.start = a
        self.end = b

    def __str__(self):
        return str(self.start) + '-' + str(self.end)


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = set()
        self.adjastList = []
        self.adjastMatrix = []
        self.incyMatrix = []

    @staticmethod
    def from_adjastlist(adjastlist):
        G = Graph()
        G.nodes = [Node(_ + 1) for _ in range(len(adjastlist))]
        for row in range(len(adjastlist)):
            for target in adjastlist[row]:
                if G.nodes[row] in G.nodes[target - 1].neibours:# if target is already conected to row node
                    continue
                edge = Edge(G.nodes[row], G.nodes[target - 1])
                G.nodes[row].edges.add(edge)
                G.nodes[row].neibours.add(G.nodes[target - 1])
                G.nodes[target - 1].edges.add(edge)
                G.nodes[target - 1].neibours.add(G.nodes[row])
                G.edges.add(edge)
        G.generate_representations()
        return G

    @staticmethod
    def from_adjastmatrix(adjastmatrix):
        G = Graph()
        G.nodes = [Node(_ + 1) for _ in range(len(adjastmatrix))]
        for row in range(len(adjastmatrix)):
            start = G.nodes[row]
            for target in range(len(adjastmatrix[row])):
                if adjastmatrix[row][target] == 0:# if matrix value 1
                    continue
                end = G.nodes[target]
                if start in end.neibours:# if not already connected
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
    def from_incidencematrix(incimatrix):
        G = Graph()
        G.nodes = [Node(_ + 1) for _ in range(len(incimatrix[0]))]
        for edge_ in range(len(incimatrix)):
            startnum, endnum = [i for i, x in enumerate(incimatrix[edge_]) if x == 1]
            start = G.nodes[startnum]
            end = G.nodes[endnum]
            if start in end.neibours:  # if not already connected
                continue
            edge = Edge(start, end)
            start.edges.add(edge)
            start.neibours.add(end)
            end.edges.add(edge)
            end.neibours.add(start)
            G.edges.add(edge)
        G.generate_representations()
        return G

    def generate_adjast_list(self):
        self.adjastList.clear()
        for node in self.nodes:
            self.adjastList.append([int(str(_)) for _ in node.neibours])

    def generate_adjast_matrix(self):
        number_of_nodes = len(self.nodes)
        self.adjastMatrix = np.zeros((number_of_nodes, number_of_nodes))
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                if self.nodes[j] in self.nodes[i].neibours:
                    self.adjastMatrix[i][j] = 1

    def generate_incidence_matrix(self):
        number_of_nodes = len(self.nodes)
        number_of_edges = len(self.edges)
        temp_edges_list = list(self.edges)
        self.incyMatrix = np.zeros((number_of_edges, number_of_nodes))
        iterator = 0
        for e in self.edges:
            index1 = self.nodes.index(e.start)
            index2 = self.nodes.index(e.end)
            self.incyMatrix[iterator][index1] = 1
            self.incyMatrix[iterator][index2] = 1
            iterator += 1

    def generate_representations(self):
        self.generate_incidence_matrix()
        self.generate_adjast_list()
        self.generate_adjast_matrix()

    @staticmethod
    def generate_graph_nl(num_nodes, num_edges):
        if not isinstance(num_nodes, int):
            raise Exception("given number of nodes num_nodes={}, is not an integer".format(num_nodes))
        if not isinstance(num_edges, int):
            raise Exception("given number of edges num_deges={}, is not an integer".format(num_edges))
        if num_edges > num_nodes * (num_nodes - 1) / 2 or num_edges < 0:
            raise Exception("given number of edges num_edges={}, "
                            "is not a valid number of adges for a "
                            "graph with num_nodes={}, as it should "
                            "be in range <0, {}>".format(num_edges, num_nodes, num_nodes * (num_nodes - 1) / 2))
        incidence_matrix = np.zeros((num_edges, num_nodes))
        nodes_connected = set()
        _ = 0
        while _ < num_edges:
            a, b = random.sample(range(num_nodes), 2)
            if (a, b) in nodes_connected or (b, a) in nodes_connected:
                continue
            incidence_matrix[_][a] = 1
            incidence_matrix[_][b] = 1
            nodes_connected.add((a, b))
            _ += 1
        return Graph.from_incidencematrix(incidence_matrix)

    @staticmethod
    def generate_graph_np(num_nodes, prob):
        if prob > 1 or prob < 0:
            raise Exception("probability prob = {} outside <0, 1> range".format(prob))
        adjast_matrix = np.zeros((num_nodes, num_nodes))
        for i in range(num_nodes):
            for j in range(i, num_nodes):
                if random.random() < prob:
                    adjast_matrix[i][j] = 1
                    adjast_matrix[j][i] = 1
        return Graph.from_adjastmatrix(adjast_matrix)


def print_graf(G):
    for n in G.nodes:
        print(n)
        for e in n.edges:
            print(e, end=" ")
        print("")


if __name__ == '__main__':
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

