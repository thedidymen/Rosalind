__author__ = 'Reijer'

import time

def load_file():
    """
    Takes DNA strings in FASTA format in txt file
    Returns a strings.
    """
    print "Loading IDs and DNA strings from file..."
    # inFile: file
    inFile = open("rosalind_grph.txt", 'r')
    file = {}
    key = ""
    for line in inFile:
        if line[0] == ">":
            if key != "":
                file[key[1:]] = item
            key = line.strip()
            item = ""
        else:
            item += line.strip()
    file[key[1:]] = item
    print "  ", len(file), "DNA strings loaded."
    return file

def cutfrontback(strings, k):
    front, back = {}, {}
    for i in strings.keys():
        front[i] = strings.get(i)[0:k]
        back[i] = strings.get(i)[-1:-1-k:-1]
        back[i] = back.get(i)[::-1]
    return front, back

def check(graph1, graph2):
    for j in graph1.keys():
        for i in graph2.keys():
            if graph1.get(i) == graph2.get(j) and i != j:
                print j, i

def main():
    start_time = time.time()
    strings = load_file()
    front, back = cutfrontback(strings, 3)
    check(front, back)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()