__author__ = 'Reijer'

import requests
import re
import time

def load_protein(code):
    """
    Takes DNA strings in FASTA format in txt file
    Returns a strings.
    """
    file_lines = content(code)
    header = file_lines.pop(0)
    return "".join(file_lines)

def load_proteincodes():
    infile = open("rosalind_mprt.txt", 'r')
    return [line.strip() for line in infile]

def content(code):
    r = requests.get('http://uniprot.org/uniprot/%s.fasta' % code)
    if not r:
        raise Exception
    return r.text.split('\n')

def Nglycosylation(s):
    return [m.start(0) for m in re.finditer(r"(?=(N[^P](S|T)[^P]))", s)]

def main():
    start_time = time.time()
    proteincodes = load_proteincodes()
    for i in proteincodes:
        print i
        for j in Nglycosylation(load_protein(i)):
            print j+1,
        print
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
