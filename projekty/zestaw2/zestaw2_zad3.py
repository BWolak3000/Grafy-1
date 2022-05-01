import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from utils import Utils

class Main:

    # @staticmethod
    # def components_R(nr, v, G, comp):
    #     for
    #
    # @staticmethod
    # def components(G):
    #     for

    @staticmethod
    def main(args):
        list = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
        # list = sorted(list, reverse=True)

        if Main.isGraphical(list):
            print("Jest graficzny!")

        else:
            print("Nie jest graficzny!")

if __name__ == "__main__":
    Main.main([])
