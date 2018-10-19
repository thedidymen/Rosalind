__author__ = 'Reijer'

def reversecomplement(s):
    sc = ""
    for i in s:
        nt = {"A": "T", "T": "A", "C": "G", "G": "C"}
        sc += nt.get(i)
    sc = sc[::-1]
    return sc

def test():
    s1 = "AAAACCCGGT"
    s = "CGCCCGTCGTTGTAAGCTAGCAGTCAGTCATCGAAAATGTGACCTCCTCACAGGTTTTACTGTTCCCAATCGCGGGAGGAGAGTCGTATGGGTCCGACGATCCGATTCATTAGCAGCCCATGCCCTGGACAAGCACGCCTTCGCAGTAGCACGTGCGGGGTCTTAAACAATTGTAGGTCGGTGAGGATATGTGAATATTGAACTGCGGGAGACAAGTGCGTACGAGAAACCAGATTAGGAGATGCCACTGACCCTTCGTCACTGACCGAGAATTTTCCTACACGTCCGTAAATCACAAGTGCCCGTCTCATATGAGTCTAACCGACCCTCTCGCCGGCTGATTGAATGGGCATCTGGAACGTGACTGTCTGTGGCCAGTGTAAACTATATGAAGCTTCCACTGCTGCGGAGTTCTCTGCGTGTTCTTTGTCAATCATTTCCTTTGCGTGTTTTAGAGTCTGACTTAAGGGCCTGTGTCGGAGCTAATAAGTGCTCCATCCCTCTCGAGAAAGGCAGGGGACACCATCGGTAAGCGGCACCTAGCCCGCGTTTGGAACTAGGGAATAGACACAATGAATGTATCAATCACCCCAATAGTGGCAAGACATTCGCCAGAACTCTCTCTATATTCAACCTCTAGTAGGATCGCACACTCTTACAGAACGCTTCTCACACTCATAAAGTCCCACATTAGAAGGATGTCACGTAGCGACCGCATATAAAGTGTCCCTCATTTTGCAGAGTGGAAAGACATTCGCGATCTGCATTAGTATTGTCCGCGTTCTGATGGTGAGACACATAGCACTTCCTCCGCTCGGTGGCCCCCGAGCCACGGTGAGATGCATTCATGATAAATCTTCTACATAATATGGTTATGTCATACTCCCCTAGCGATGAAGGTACTGGTGGCAGCTCACATCCTGACTCCAGCGCAGTATGCGACTGTA"
    sc = reversecomplement(s)
    print s
    print sc

if __name__ == '__main__':
    test()