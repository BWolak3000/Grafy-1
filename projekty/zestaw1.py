import networkx as nx
import matplotlib.pyplot as plt


def main():
    adjlist = [[2, 5], [1, 3, 4], [5, 2, 4], [2, 3], [3, 1]]
    #adjlist = [[2], [3], [4, 5], [4], []]

    temp = list_of_lists_to_str(adjlist)
    #temp = ["1 2 5", "2 1 3 4", "3 5", "4", "5"]
    print(temp)
    # G = nx.complete_graph(5).subgraph([0, 1, 4])
    #
    # nx.write_adjlist(G, "test.adjlist")
    # f = open("test.adjlist", 'w')
    # f.write(temp)

    G = nx.parse_adjlist(temp)

    pos = nx.circular_layout(G)
    nx.draw(G, pos=pos, node_color="red", with_labels=True)
    plt.draw()  # pyplot draw()
    plt.show()


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
