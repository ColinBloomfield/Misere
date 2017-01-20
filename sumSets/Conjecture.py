# Various tests of the conjecture that the sum of two periodic sets A and B is periodic.
import itertools
import re
import math
import random


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

def test1():
  bound = 100
  l = 3
  k = 6
  L4 = {(x, y) for x in range(100) for y in range(100) if
          ((x % (3 * k - 1) == 0) and y % (3 * l - 1) == l) or ((y % (3 * l - 1) == 0) and x % (3 * k - 1) == k)}
  f = open("minimal2.txt", 'w')
  #write(f, sumSets(L4, L4), 1)
  write(f, L4, 0)

def test2():
  bound = 100
  A = {(x,y) for x in range(100) for y in range(100) if (x+y)%16 == 15 }
  #B = {(x,y) for x in range(100) for y in range(100) if (x%4 == 1 and y<=x) or (y%4 == 1 and x<y)}
  #L = [x for x in range(100) if random.randint(0,1) == 1]
  #D = {(x,y) for x in L for y in range(100) if y%4 ==3}
  E = { (x,y) for x in range(100) for y in range(100) if (x%8 < 3 and y%8 < 3)}
  #C = {(0,0)}
  f = open("minimal2.txt", 'w')
  write(f, E, 0)
  write(f, A, 0)
  write(f, sumSets(E, A), 1)
  write(f, {(101,101)}, 1) #handles unused color error with gnuplot

def main():
  test2()


if __name__ == '__main__':
  main()
