__author__ = 'Reijer'

def converttorna(s):
    t = ""
    for i in range(len(s)):
        if s[i] == "T":
            t += "U"
        else:
            t += s[i]
    return t

def convertoneline(s):
    return s.replace("T", "U")


def test():
    s1 = "GATGGAACTTGACTACGTAAATT"
    s = "ACGAGTTTCTACATACGCTCGAGGTTCTGAGTACATTCGACCTTAGGGCATGCTTGCTACTCATTTATGTCGGTCTATTTCACATTGTACGTAGATGTTAGGACATGGTGTTTGCATCTGTCATGCATCGGTCGTACCCTGGGCTACACGTCTGAGACTTAGCTTCATTACCGACGCAAGGTAAATCTACGGCCGTAGTGCTTATTAGCACTCATTAATAGTACTGTAATGATACACCAGGTACAGCCAGCCTTCGATGTCGTGGCAAGAGATCTTCTTGACCCTAACTAGATAAATATCGCATGTGTCGCGGATCGGGAACTTGGATAAGGTTAATCTCAACTTTTATTTCCGTCGGCAATGCGACACGCCTGGCGTCGACAGCACCGTAGCAAGCTCCACTTACTTCTGGTAAACCTGTGGGTTAGGGGGCAGTTGGGTATCGGGATGTAGTTCACGGACCATCCTAGAGTCCCGAACACGAACTTTTGGCCGTCAAGAACACACGGTGCTTAAGGGCTGATACATTAATCTAGTACAGCCAAACTAAAATTACCCCGGATTGAGACCACTTTGAAGTTTTCGGGCTTACCAGAACGCACATGGCCGGTATAGGATGATTCAATACCCTTTGTCGAGAGGTCTTCCATGCAATCATCTGGATAGCGGGAGTTACGGATCGGGATCGTTGTCAAGAATAAGGCACCCAGCGGAGCGTAATACATCTGGTCGGGGCTTATCAGTTACGCCTTATTTTTGCGGTCGACCATTTAGCCATAGGTAGAGTGTCCCGCAGGGCAGGCGACCCGCGTAACTCCTGTTTGTAAGTCTACCGGTGGATGCAACCTCTTGGTAATATCCCAAATGGCGCAGTATGTCGAAAACGATTGGGTAAAAGGCGAATCTCAAGTACGCCCTGGGTAAGAGACATTTCTGGACTACTGACTTTCTCTACTAGGTCGTAGTCGTGAG"
    t = converttorna(s)
    print convertoneline(s)
    print t

if __name__ == '__main__':
    test()