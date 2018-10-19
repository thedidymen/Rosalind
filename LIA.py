__author__ = 'Reijer'

import time
import math

# def offspring_old(f0):
#     """takes 2 couples (XX-XX), returns list of possible offspring [xx, ..., XX]
#     """
#     p1, p2 =  f0.split("-")
#     return [n+o for n in p1 for o in p2]
#
# def offspring(parent1, parent2 = "Aa-Bb"):
#     parent1gen1, parent1gen2 = parent1.split("-")
#     parent2gen1, parent2gen2 = parent2.split("-")
#     gen1 = [n+o if n.isupper() and o.islower() else o+n for n in parent1gen1 for o in parent2gen1]
#     gen2 = [n+o if n.isupper() and o.islower() else o+n for n in parent1gen2 for o in parent2gen2]
#     # print gen1, gen2
#     # print parent1gen1, parent1gen2, parent2gen1, parent2gen2
#     return [m + "-" + l for m in gen1 for l in gen2]

memo = [1,1]

def fact(n):
    if n == 1 or n == 0:
        return 1
    if len(memo)>n:
        return memo[n]
    else:
        memo.append(n*fact(n-1))
    return memo[n]

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def main():
    k = 5
    n = 7
    prob = 0.0
    i = n
    print 2**k
    while i <= (2**k):
        prob += Ber(k,i)
        i += 1
        print i, prob
    print prob

def Ber(gen,num_offspring):
    return (math.factorial(2**gen)/(math.factorial(num_offspring) * math.factorial((2**gen) - num_offspring)))*(0.25**num_offspring) * (1-0.25)**((2**gen) - num_offspring)



    # f1 = offspring(parent)
    # f2 = []
    # for i in f1:
    #     f2.append(offspring(i))
    # freq = get_frequency_dict(f1)
    # print freq.get("Aa-Bb"), sum(freq.values())
    # for j in f2:
    #     freqf2 = get_frequency_dict(j)
    #     print j
    #     print freqf2.get("Aa-Bb"), sum(freqf2.values())

    # f3 = []
    # for i in f2:
    #     for j in i:
    #         f3.append(offspring(j))
    # f4 = []
    # for i in f3:
    #     for j in i:
    #         f4.append(offspring(j))
    # f5 = []
    # for i in f4:
    #     for j in i:
    #         f5.append(offspring(j))
    # f6 = []
    # for i in f5:
    #     for j in i:
    #         f6.append(offspring(j))
    # counter = 0
    # print f1
    # for j in f2:
    #     for k in j:
    #         print k,
            # if k == "Aa-Bb":
            #     counter += 1
        # print
    # print counter, counter / (len(f2)*16.0)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()