__author__ = 'Reijer'

def load_file():
    """
    Takes DNA strings in FASTA format in txt file
    Returns a dictionary of ID(wihtout >) with DNA strings.
    """
    print "Loading IDs and DNA strings from file..."
    # inFile: file
    inFile = open("rosalind_gc.txt", 'r')
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

def pcg(s):
    """Takes a DNA string. Returns fraction of C and G of string."""
    counter = 0
    for i in s:
        if i == "C" or i == "G":
            counter += 1
    return float(counter)/len(s)

def idpcg(file):
    """Takes dict. of IDs and DNA strings. Returns IDs and percentages as dict."""
    p = {}
    for id in file.keys():
        p[id] = pcg(file[id])
    return p

def highestidp(p, y = 0.001):
    """Takes p (IDs and percentages as dict) and y (default absolute error). Returns highest percentage and ID. as dict"""
    highestp = ["", 0]
    for id in p.keys():
        if p[id] > highestp[1]:
            highestp = [id, p[id]]
    collect = checkinterval(p, y, highestp)
    return collect

def checkinterval(p, y, highestp):
    """Takes p(IDs and percentage as dict), y (default absolute error) and highest (hightest found pecentage and id as list)
    returns dict of ids and percentage of all values within absolute error of highest found
    """
    collect = {}
    for id in p.keys():
        if id == highestp[0]:
            collect[highestp[0]] = highestp[1]
        elif abs(p[id] - highestp[1]) < y:
            collect[id] = p[id]
    return collect

def test():
    file = load_file()
    # for id in file.keys():
    #     print id, file[id]
    p = idpcg(file)
    top = highestidp(p)
    for id in top.keys():
        print id
        print top[id]*100

if __name__ == '__main__':
    test()