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
        self.nodes = set()
        self.edges = set()
        self.list_representation = []
        self.matrix_representation = []
        self.matrix_incy = []

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
        return G


def print_graf(G):
    for n in G.nodes:
        print(n)
        for e in n.edges:
            print(e, end=" ")
        print("")


if __name__ == '__main__':
    #adjlist = [[2, 5], [1, 3, 4], [5, 2, 4], [2, 3], [3, 1]]
    G = Graph.from_adjastlist([[2, 5], [1, 3, 4], [5, 2, 4], [2, 3], [3, 1]])
    G = Graph.from_adjastmatrix([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
    G = Graph.from_incidencematrix([[0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1]])
    print_graf(G)

