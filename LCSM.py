__author__ = 'Reijer'

import time

def load_file():
    """
    Takes DNA strings in FASTA format in txt file
    Returns a strings.
    """
    print "Loading IDs and DNA strings from file..."
    # inFile: file
    inFile = open("rosalind_lcsm.txt", 'r')
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

def motif(s, t):
    """takes string s and search string t, returns list of hits 0-based"""
    if s.find(t) != -1:
        return True
    else:
        return False

def createmotif(s):
    for j in xrange(len(s), 1, -1):
        for i in xrange(len(s)-j):
            yield s[i:j+i]


def comparestring(string):
    id = list(string.keys())
    for k in createmotif(string.get(id[0])):
        motifs = ""
        for l in range(1, len(id)):
            if motif(string.get(id[l]), k):
                motifs = k
            else:
                motifs = ""
                break
        if len(motifs) != 0:
            return k

def main():
    start_time = time.time()
    string = load_file()
    motif = comparestring(string)
    print motif
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()