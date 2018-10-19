__author__ = 'Reijer'

import time
import itertools

def load_alphabet():
    """
    Takes DNA strings in FASTA format in txt file
    Returns a strings.
    """

    file_lines = open("rosalind_lexf.txt", 'r')
    l = [line.strip() for line in file_lines]
    return "".join(l[0].split()), int(l[-1])



def main():
    start_time = time.time()
    alphabet, length = load_alphabet()
    print alphabet, length
    # dict = list(itertools.product(alphabet, repeat=length))
    # for i in dict:
    #     word = ""
    #     for j in i:
    #         word += j
    #     print word
    for p in itertools.product(alphabet,repeat=length):
        print ''.join(p)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()