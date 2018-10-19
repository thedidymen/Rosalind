__author__ = 'Reijer'



def loadfile(genotypes):
    """
    Loads couples form rosalind_iev.txt, returns dict {"AA-AA":##, ..., "aa-aa":##}
    """
    print "Loading couples from file..."
    # inFile: file
    inFile = open("rosalind_iev.txt", 'r')
    for line in inFile:
        ncouples = map(int, line.split())
    print sum(ncouples), "couples loaded"
    return {genotypes[n]: ncouples[n] for n in range(len(genotypes))}

def offspring(f0):
    """takes 2 couples (XX-XX), returns list of possible ofspring [xx, ..., XX]
    """
    p1, p2 =  f0.split("-")
    # f1 = []
    # for n in p1:
    #     for o in p2:
    #         f1.append(n+o)
    # return f1
    return [n+o for n in p1 for o in p2]

def pdominant(f1):
    """ takes list of offspring [xx, ..., XX] returns fraction for presence of dominant trait"""
    nf1 =  len(f1)
    ndominant = 0
    for n in f1:
        if (any(x.isupper() for x in n)):
            ndominant += 1.0
    return ndominant/nf1


def EDf1(couples, genotypes):
    total = 0
    ntotal = 0
    # print "total, pD, couples.get(couple), couple, f1"
    for couple in genotypes:
        f1 = offspring(couple)
        pD = pdominant(f1)
        total += 2 * pD * couples.get(couple)
        # print total, pD, couples.get(couple), couple, f1
    return total

def test():
    genotypes = ["AA-AA", "AA-Aa", "AA-aa", "Aa-Aa", "Aa-aa", "aa-aa"]
    couples = loadfile(genotypes)
    ED =  EDf1(couples, genotypes)
    print ED




if __name__ == '__main__':
    test()