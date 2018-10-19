__author__ = 'Reijer'

import time

amino ={
"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
"UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
"UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
"UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
"UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
"UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
"UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
"UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
"UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
"UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
"UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
"UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
"UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
"UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
"UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
"UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"
}

def load_file():
    """
    Takes DNA strings in FASTA format in txt file
    Returns a strings.
    """
    print "Loading IDs and DNA strings from file..."
    # inFile: file
    inFile = open("rosalind_splc.txt", 'r')
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

def longstring(s):
    print "...selecting longest string..."
    counter = 0
    string = ""
    for i in s.keys():
        if len(s.get(i)) > counter:
            string = s.get(i)
            counter = len(string)
            idlong = i
    ids = s.keys()
    ids.pop(ids.index(idlong))
    return string, idlong, ids

def intronsexit(s, i):
    print "...removing introns..."
    return s.replace(i, "")

def convert(s):
    print "...converting to RNA..."
    return s.replace("T", "U")

def translate(s):
    """takes RNA string, translate to protein string"""
    if len(s)==3:
        if amino.get(s) == "Stop":
            return ""
        else:
            return amino.get(s)
    else:
        print "error: expect 3 chars string"
        return ""

def product(s):
    print "...translanting RNA to protein..."
    protein = ""
    while len(s) > 0:
        protein += translate(s[0:3])
        s = s[3:]
    return protein

def main():
    start_time = time.time()
    strings = load_file()
    string, idlong, ids = longstring(strings)
    for i in ids:
        string = intronsexit(string, strings.get(i))
    rna = convert(string)
    protein = product(rna)
    print protein
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()