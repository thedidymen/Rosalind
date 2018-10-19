__author__ = 'Reijer'

import time

def load_nodesandedges():
    fromfile = loadfromfile()
    nodes = fromfile.pop(0)
    return nodes, [tuple(edge.split()) for edge in fromfile]

def loadfromfile():
    infile = open("rosalind_tree.txt", 'r')
    return [line.strip() for line in infile]


def main():
    start_time = time.time()
    nodes, edges = load_nodesandedges()
    print nodes, edges
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()