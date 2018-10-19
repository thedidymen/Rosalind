__author__ = 'Reijer'

memo = {0:0, 1:1}

def fib(n, k):
    global memo
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        if not n in memo:
            memo[n] = fib(n-1, k) + k*fib(n-2, k)
        return memo[n]


def test():
    n = 29
    k = 4
    print fib(n, k)


if __name__ == '__main__':
    test()