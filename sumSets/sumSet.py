import itertools
import re


def s(x, y):
    return tuple([w + z for w, z in zip(x, y)])

# tuple([item1 + item2 for item1, item2 in zip(a, b)])

def newfile(list1, file):
    f = open(file + ".txt", 'w')
    for x in list1:
        write(f, x[0], x[1])


def write(f, S1, color):  # hardcoded!! :(
    for x in S1:
        f.write(repr(x[0]) + ' ' + repr(x[1]) + ' ' + repr(color) + '\n')
    f.write('\n')


def sumSets(S1, S2):
    return {s(x, y) for x in S1 for y in S2}


def main():


    bound = 100
    l = 3
    k = 6

    L1 = {(x, y) for x in range(100) for y in range(100) if
          ((x % (3 * k - 1) in range(k, 2 * k)) and y < l) or ((y % (3 * l - 1) in range(l, 2 * l)) and x < k)}

    L2 = {s(x, (2 * k - 1, 2 * l - 1)) for x in L1}

    L3 = {(x, y) for x in range(100) for y in range(100) if
          ((x % (3 * k - 1) in range(k, 2 * k)) and y < 1) or ((y % (3 * l - 1) in range(l, 2 * l)) and x < 1)}
    # print("T: (", x, ',',y , ')')


    L3 = {s(x, (4 * k - 2, 4 * l - 2)) for x in L3}

    L4 = {(x, y) for x in range(100) for y in range(100) if
          ((x % (3 * k - 1) == 0) and y % (3 * l - 1) == l) or ((y % (3 * l - 1) == 0) and x % (3 * k - 1) == k)}
    # print("T: (", x, ',',y , ')')

    L4 = {s(x, (6 * k - 3, 6 * l - 3)) for x in L4}

    Comb = {0: L1, 1: L2, 2: L3, 3: L4}
    d = {}
    for i in range(4):
        for j in range(i, 4):
            # write(sumSets(Comb[i],Comb[j]),1)
            d[(i, j)] = sumSets(Comb[i], Comb[j])

    for x in d:
        f = open(str(x) + ".txt", 'w')
        write(f, d[x], 1)
        write(f, Comb[x[0]], 0)
        write(f, Comb[x[1]], 0)

    f = open("minimal2.txt", 'w')
    write(f, Comb[0], 0)
    write(f, Comb[1], 0)
    write(f, sumSets(Comb[0], Comb[1]), 1)
    write(f, sumSets(Comb[0], Comb[0]), 1)
    write(f, sumSets(Comb[1], Comb[1]), 1)
    write(f, sumSets(Comb[1], Comb[2]), 1)
    write(f, Comb[2], 0)

if __name__ == '__main__':
    main()

    # LR = {x for x in L1 if (x[0] < 18 and x[1] < 6)}


    #L1V = {x for x in L1 if x[0] < k}
    #L1H = {x for x in L1 if x[1] < l}
    #
    # L1H1 = {x for x in L1H if x[0] < 2 * k}
    # L1V1 = {x for x in L1V if x[1] < 2 * l}
    #
    # L2V = {x for x in L2 if x[0] < 3 * k - 1}
    # L2H = {x for x in L2 if x[1] < 3 * l - 1}

    # write(L2, 0)
    # write(L1, 0)
    # write(sumSets(L2V, L1V), 1)
    # write(sumSets(L2H, L1H), 1)
    # write(sumSets(L1H, L1H), 1)
    # write(sumSets(L1V, L1V), 1)
    # write(sumSets(L1V, L1H1), 1)
    # write(sumSets(L1H, L1V1), 1)

    # write(L2, 0)
    # write(L3, 0)
    # write(L4, 0)

    # NL1 = sumSets(L3,L4)
    # write(NL1,1)

    # NL2 = sumSets(L1,L2)
    # write(NL2,1)

    # NL3 = sumSets(L1,L3) Redundant!
    # write(NL3,1)

    # NL4 = sumSets(L1,L4) Redundant!
    # write(NL4,1)

    # NL5 = sumSets(L4,L2)
    # write(NL5,1)

    # NL6 = sumSets(L3,L2)
    # write(NL6,1)

    # S1 = sumSets(L1,LR)
    # write(S1,1)

    # S2 = sumSets(L2,L2)
    # write(S2,1)

    # S3 = sumSets(L3,L3) #redundant!
    # write(S3,1)

    # S4 = sumSets(L4,L4) #redundant
    # write(S4,1)

    # print("Size of L1: ",len(L1))
    # print("Size of NL1: ",len(NL1))
