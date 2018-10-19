__author__ = 'Reijer'

import itertools


memo = [1,1]

def fact(n):
    if n == 1 or n == 0:
        return 1
    if len(memo)>n:
        return memo[n]
    else:
        memo.append(n*fact(n-1))
    return memo[n]


def main():
    n = 7
    print fact(n)
    l = list(itertools.permutations(range(1, n+1)))
    for i in l:
        for j in i:
            print j,
        print

if __name__ == '__main__':
    main()