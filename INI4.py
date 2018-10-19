__author__ = 'Reijer'

def sumodd(a,b):
    if a % 2 == 0:
        start = a +1
    else:
        start = a
    sum = 0
    while start <= b:
        sum += start
        start += 2
    return sum

def test():
    print sumodd(4145, 8187)

if __name__ == '__main__':
    test()