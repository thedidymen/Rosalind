__author__ = 'Reijer'

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
    n = 87
    m = 10
    som = 1
    for i in range(m):
        som *= n-i
        som %= 1000000
        print i, som
    print som



if __name__ == '__main__':
    main()
