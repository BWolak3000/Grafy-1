class Utils:
    @staticmethod
    def degree_seq_to_adj_matrix(list):
        size = len(list)
        adj_matrix1 = [[0 for x in range(size)] for y in range(size)]
        print(list)
        for i in range(0, size):
            for j in range(i + 1, size):
                if list[i] > 0 and list[j] > 0:
                    adj_matrix1[i][j] = 1
                    adj_matrix1[j][i] = 1
                    list[i] = list[i] - 1
                    list[j] = list[j] - 1
        return adj_matrix1
