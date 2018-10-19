__author__ = 'Reijer'


def Pdominant(k, m, n):
    t = k + m + n
    pYyYy = (float(m)/t)*((float(m)-1)/(t-1))
    pYyyy = (float(m)/t)*(float(n)/(t-1))
    pyyYy = (float(m)/t)*(float(n)/(t-1))
    pyyyy = (float(m)/t)*((float(m)-1)/(t-1))
    pyyfromYyYy = (float(1)/2)*(float(1)/2)
    pyyfromYyyy = (float(1)/2)*(float(2)/2)
    pyyfromyyYy = (float(1)/2)*(float(2)/2)
    precessive = pyyfromYyyy*pYyyy + pyyyy + pyyfromYyYy*pYyYy + pyyfromyyYy*pyyYy
    # print (float(m)/t), ((float(m)-1)/(t-1)), (float(n)/(t-1)), float(m)-1, t-1
    # print "precessive, pYyyy, pyyyy, pYyYy, pyyYy"
    # print precessive, pYyyy, pyyyy, pYyYy, pyyYy
    return (1 - precessive)


    # return 1 - (.25*((float(m) / t) * ((float(m) - 1) / (t - 1)))) + \
    #        (2 * ((float(m) / t) * (float(n) / (t - 1)))) + \
    #        (((float(n) / t) * ((float(n) - 1) / (t - 1))))
    # p(dominant) = 1 - p(recessive)
    # Yy and Yy have 25% chance of p(recessive)
    # Yy and yy 50% but overall chance is twice as high because off different combinations
    # yy and Yy 50% but overall chance is twice as high because off different combinations
    #yy and yy 100%
    #p(yy and yy) = n(yy)/t(sum n(YY, Yy, yy)) * n-1(yy)/t-1(sum n(YY, Yy, yy)


def test():
    print Pdominant(2, 2, 2)


if __name__ == '__main__':
    test()