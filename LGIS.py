__author__ = 'Reijer'

import time
import random

def loadprobs():
    file_lines = open("rosalind_lgis.txt", 'r')
    l = [line.strip() for line in file_lines]
    return int(l[0]), [int(n) for n in l[1].split(" ")]

def pot(a):
    for i in a:
        yield i




def main():
    start_time = time.time()
    # n, a = loadprobs()
    n = 10
    a = random.sample(range(1, n+1), n)
    for i in pot(a):
        print i,

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()