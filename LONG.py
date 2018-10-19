__author__ = 'Reijer'

import time

def loadproteins():
    print "Loading IDs and DNA strings from file..."
    # inFile: file
    inFile = open("rosalind_long.txt", 'r')
    proteins = {}
    rosalind_id = ""
    for line in inFile:
        if line[0] == ">":
            if rosalind_id != "":
                proteins[rosalind_id[1:]] = protein
            rosalind_id = line.strip()
            protein = ""
        else:
            protein += line.strip()
    proteins[rosalind_id[1:]] = protein
    print "  ", len(proteins), "DNA strings loaded."
    return proteins


def nextstring(keylist, proteins):
    for id in keylist:
        yield proteins.get(id)

def main():
    start_time = time.time()
    proteins = loadproteins()
    keylist = [i for i in proteins.keys()]
    superstring = proteins.get(keylist[0])
    keylist.pop(0)
    for j in range(len(keylist)):
        for i in nextstring(keylist, proteins):
            for max in range(len(i), len(i)/2, -1):
                if i[len(i)-max:] == superstring[:max]:
                    superstring = i[:len(i)-max] + superstring
                    break
                if i[:max] == superstring[len(superstring)-max:]:
                    superstring += i[max:]
                    break
    print superstring
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()