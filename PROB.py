__author__ = 'Reijer'

import time
import math

def loadprobs():
    file_lines = open("rosalind_prob.txt", 'r')
    l = [line.strip() for line in file_lines]
    return l[0], [float(n) for n in l[1].split(" ")]

def probs(cgcontent):
    return cgcontent/2, (1-cgcontent)/2

def ps(nt, pcg, pat):
    if nt == "A" or nt == "T":
        return pat
    else:
        return pcg

def main():
    start_time = time.time()
    s, a = loadprobs()
    for i in range(len(a)):
        p = 0
        pcg, pat = probs(a[i])
        for n in s:
            p += math.log10(ps(n, pcg, pat))
        print round(p, 3),
    print
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()