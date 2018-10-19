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

def convert(s):
    return s.replace("T", "U")

def translate(s):
    """takes RNA string, generates corresponding protein string"""
    while len(s) > 2:
        yield amino.get(s[len(s)-3:])
        s = s[:len(s)-3]
    yield "Uberstop"



def ofsetstart(s):
    proteincollection = []
    for j in range(0, 3):
        protein = ""
        start = False
        for i in translate(s[:len(s)-j]):
            if i == "Uberstop":
                break
            elif i == "Stop":
                protein = ""
                start = True
            elif i == "M" and start == True:
                protein += i
                proteincollection.append(protein[::-1])
            else:
                protein += i
    return proteincollection

def reversecomplement(s):
    sc = ""
    nt = {"A": "T", "T": "A", "C": "G", "G": "C"}
    for i in s:
        sc += nt.get(i)
    sc = sc[::-1]
    return sc

def main():
    start_time = time.time()
    s2 = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    s = "TCGAAAACCTTACGGATCCATTATCTGAAAAGCGGCCCGAGACCTGGATGATCCGGGCCCTCGAACTACCCTTGAGATTATACAAAAAGATTTCAGTGACCATAATAGAGGCGCCTGACCTTGCCCAACGGCAGCGAATGGCCGTCTAGTTGTGTTCCACGAGCAGTAAAAACCTCTCCTTCCTGAAGACATTATTGCAATCCGCTATTTGGAAGTGGCTTACCCTGGAGGCATTTGGTACTTCCAGTCGCTCTTCGTAGGCTTGGATATGCTGTACTTTACGCGCACAGGGCCGCGTCACGCCAGAATGGAAATGCTATGCCCAAATGACGCCACATATTGCATTAAATAAGCGTGTTTAGGAATCGGTCGCGTTTCATGTGGTCGTAGCCGGAGCTCTCTTGAGGCTGATGTCGTGGCTCCGGGGGCCCCATATCGTGTAGCTACACGATATGGGGCCCCCGGAGCCACGACATAGTCCCGCAGAACTTCGAGAACTTAGGTCCATAGGAAGATTCAGAGAACCTGTCGCTTCTTTTACCCCTGACTCTCAGCAATCGTTCTTACCACACCTGCGTTAGATGGTAGGATCTCAGGAAGTACTTCACCAAGCTCTTAGCATCGCACTCTTATAGCGACTCCGAGGCAGCGCGTTTTCCGCTACCAGCGTTGTGAGACCGGCTAACCGGAGTAAAGTGTCGATACGTCATCTAGTTCAATACGTATAAATATCCGCCTTTTCGTCGAGCCCCAGAAACTATTCTGCGGAGAGGCACCAACCCCGTCAGGCAACCTAAAATGCATACTTCTTATAGGAGCCAAGGAATGGCCGTACACATATCTGAATATACTACCAAGTTGAACACCCTTTATTCCCAGTCTGAGT"
    rna = convert(s)
    rrna = convert(reversecomplement(s))
    total = list(set(ofsetstart(rna) + ofsetstart(rrna)))
    for i in total:
        print i
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()