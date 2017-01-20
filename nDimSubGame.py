import numpy as np
import re
import copy


# Def Less than for tuples
# Is this even used? Does not appear to work for tuples or numpy arrays.
def Leq(t1, t2):
    for x in range(len(t1)):
        if t1(x) > t2(x):
            return False
    return True


def Sub(t1, t2):
    return tuple([w - z for w, z in zip(t1, t2)])


def Add(t1, t2):
    return tuple([w + z for w, z in zip(t1, t2)])


def isPos(t1):
    for x in range(len(t1)):
        if t1[x] < 0:
            return False
    return True


def getTerm(gameType, S=[(6, 0), (0, 3)], n=100, dim=2):
    # Constructs np.array and sets Terminal positions to 1 and everything else to 0.
    # np.ndarray(shape=tuple(n for i in range(dim)), dtype=int, order='C')
    Nim = np.zeros(shape=tuple(n for i in range(dim)), dtype=np.int, order='C')
    # Nim = ['P' for x in range(n+1)]
    it = np.nditer(Nim, flags=['multi_index'])
    if gameType == 'm':
        while not it.finished:
            isterm = 0
            for y in S:
                if isPos(Sub(it.multi_index, y)):
                    isterm = 1
                    break
            if isterm == 0:
                Nim[it.multi_index] = 1
            it.iternext()
    it.reset()
    return Nim, it


# MAIN FUNCTION
def get_game(n, Nim, it, S, dim):
    maxi = tuple([n - 1] * dim)
    # print(Nim)
    print(S)
    while not it.finished:
        if Nim[it.multi_index] != 1:
            for y in S:
                if isPos(Sub(maxi, Add(it.multi_index, y))):
                    # print(it.multi_index,y)
                    # print(Add(it.multi_index,y))
                    # print(maxi)
                    # print(Sub(maxi,Add(it.multi_index,y)))
                    Nim[Add(it.multi_index, y)] = 1
        it.iternext()
    S1 = []
    it.reset()
    while not it.finished:
        if Nim[it.multi_index] != 1:
            S1.append(it.multi_index)
        it.iternext()
    return S1


# Generates Sequence
def get_sequence(gameType, iter1=5, n=100, S=[(6, 0), (0, 3)], dim=2):
    Nim1, it = copy.copy(getTerm(gameType, S, n, dim))
    sequence = [S]
    s0 = copy.copy(S)
    for y in range(iter1):
        nim = np.array(Nim1, copy=True)
        it = np.nditer(nim, flags=['multi_index'])
        S1 = get_game(n, nim, it, s0, dim)
        sequence.append(S1)
        s0 = copy.copy(S1)
    return sequence


def printSeq(Sequence, base=11):
    for x in range(len(Sequence)):
        f = open('MisereSeq' + str(x) + '.txt', 'w')
        for y in Sequence[x]:
            for z in range(len(y)):
                f.write(repr(y[z]) + ' ')
            f.write('\n')


def main():
    gameType = input("Enter the type of subtraction game. 'n' for normal, 'm' for misere: ")
    cont = 'y'
    while cont != ('n' or 'N'):  # continues while cont is not equal to 'n' or 'N'.
        # HAVEN't HANDLED NORMAL PLAY
        S = []
        S1 = input("Enter subtraction set as comma separated tuples or enter a .txt file: ")
        if S1[-1] == 't':
            with open(S1, 'r', encoding='utf-8') as a_file:
                S = [tuple(int(x) for x in line.split()) for line in a_file]

        else:
            a = re.findall('\([^)]*\)', S1)
            b = [x1.strip('()') for x1 in a]
            c = [x1.split(',') for x1 in b]
            S = [tuple(int(x2) for x2 in x1) for x1 in c]

        n = int(input("Enter integer value of the stack height to calculate. "))
        iter1 = int(input("Enter a number of iterations: "))

        dim = len(S[0])

        Sequence = get_sequence(gameType, iter1, n, S, dim)

        # for x in range(len(Sequence)):
        # print(Sequence[x])
        # print()

        printSeq(Sequence)

        for x in range(len(Sequence) - 1):
            if Sequence[x] == Sequence[x + 1]:
                print("fuck")

        cont = input("Calculate the P-positions of another game? y/n: ")


if __name__ == '__main__':
    main()
