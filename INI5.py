__author__ = 'Reijer'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading line list from file..."
    # inFile: file
    inFile = open("INI5.txt", 'r')
    # wordlist: list of strings
    file = []
    for line in inFile:
        file.append(line.strip())
    print "  ", len(file), "lines loaded."
    return file

def reductionfile(file):
    reducedfile = []
    #f = open('INI5output.txt', 'w')
    for i in range(1, len(file), 2):
        #f.write(file[i])
        reducedfile.append(file[i])
    return reducedfile

def test():
    filelist = load_words()
    reduction = reductionfile(filelist)
    for i in reduction:
        print i

if __name__ == '__main__':
    test()