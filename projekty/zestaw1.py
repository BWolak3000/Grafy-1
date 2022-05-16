import networkx as nx
import matplotlib.pyplot as plt

try:
    import Graph
except:
    import projekty.Graph


def main():
    converting_demo()
    generating_demo()


def converting_demo():
    adjlist = read_adjust_list_from_file("testadjlist.txt")# wczytuje liste sasiedztwa z pliku do formu list(list(int))
    G = Graph.Graph.from_adjastlist(adjlist)# tworze obiekt typu graph generowany z listy sasiedztwa
    print('macierz sasiedztwa\n \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print(G.adjastMatrix)
    print('macierz incydencji\n \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print(G.incyMatrix)
    show_graph(G)


def generating_demo():
    G = Graph.Graph.generate_graph_np(8, 1)
    show_graph(G)

    G = Graph.Graph.generate_graph_nl(5, 9)
    show_graph(G)


# funkcja kazda linie w pliku interpretuje jako wieszcholki na liscie sasiedztwa
# pusta linia jest interpretowana jako wieszcholek stopnia 0
def read_adjust_list_from_file(file_name):
    f = open(file_name, 'r')
    lines = f.read().split('\n')
    result = []
    for line in lines:
        l = line.split(' ')
        result.append([int(_) for _ in l])
    f.close()
    return result


#z uzyciem networkx wizualizuje graf
def show_graph(G):
    temp = list_of_lists_to_str(G.adjastList)
    G = nx.parse_adjlist(temp)
    pos = nx.circular_layout(G)
    nx.draw(G, pos=pos, node_color="white", with_labels=True)
    plt.draw()  # pyplot draw()
    plt.show()


#funkcja konwertuje format uzywany przezemnie do reprezentacji listy sasiedztwa list(list(int)) na
# uzywana przez networkx list(str) gdzie str to string zaczynajacy sie od numeru wierzcholka a nastepnie jego zasiadow
def list_of_lists_to_str(data):
    result = []
    for i in range(len(data)):
        temp = str(i + 1)
        if len(data[i]) != 0:
            temp += " "
        for ele in data[i]:
            if ele == data[i][-1]:
                temp += str(ele)
            else:
                temp = temp + str(ele) + " "
        result.append(temp)
    return result


if __name__ == '__main__':
    main()
