__author__ = 'Reijer'

def load_file():
    """
    Takes DNA strings in FASTA format in txt file
    Returns a dictionary of ID(wihtout >) with DNA strings.
    """
    print "Loading IDs and DNA strings from file..."
    # inFile: file
    inFile = open("rosalind_cons.txt", 'r')
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
    return file, len(item)

def strip(file):
    paralelstring = ""
    for id in file.keys():
        tmp = file.get(id)
        paralelstring += tmp[0:1]
        file[id] = tmp[1:]
    return get_frequency_dict(paralelstring)


def get_frequency_dict(sequence):
    freq = {"A": 0, "C": 0, "T": 0, "G":0}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def freqlist(strings, length):
    A, T, C, G = [], [], [], []
    for i in range(length):
        freq = strip(strings)
        A.append(freq.get("A"))
        T.append(freq.get("T"))
        G.append(freq.get("G"))
        C.append(freq.get("C"))
    return [A, C, G, T]

def display(listoflist, supremestring):
    letters = ["A:", "C:", "G:", "T:"]
    print supremestring
    for item in listoflist:
        print letters[listoflist.index(item)],
        for i in item:
            print i,
        print

def superstring(listoflist, length):
    letters = ["A", "C", "G", "T"]
    string = ""
    for i in range(length):
        l = []
        for j in listoflist:
            l.append(j[i])
        string += letters[l.index(max(l))]
    return string

def main():
    strings, length = load_file()
    l = freqlist(strings, length)
    display(l, superstring(l, length))

if __name__ == '__main__':
    main()