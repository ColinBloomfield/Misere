#This program performs generalized tests on the behaviour of adding two periodic rectangular sets.

import itertools
import re

def s(x, y):
    return tuple([w + z for w, z in zip(x, y)])


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



S = input("Enter the period for Set 1 (x,y): ")
a = S.strip('()')
b = a.split(',')
p1 = [ int(d) for d in b]
w1 = int(input("Enter the width for Set 1: "))
l1 = int(input("Enter the length for Set 1: "))
S = input("Enter a shift for Set 1 (x,y): ")
a = S.strip('()')
b = a.split(',')
s1 = tuple([ int(d) for d in b])

S = input("Enter the period for Set 2 (x,y): ")
a = S.strip('()')
b = a.split(',')
p2 = [ int(d) for d in b]
w2 = int(input("Enter the width for Set 2: "))
l2 = int(input("Enter the length for Set 2: "))
S = input("Enter a shift for Set 2 (x,y): ")
a = S.strip('()')
b = a.split(',')
s2 = tuple([int(d) for d in b])

S = input("Enter a Max Value to Calculate (x,y): ")
a = S.strip('()')
b = a.split(',')
M = [ int(d) for d in b]



S11 = {(x,y) for x in range(w1) for y in range(l1)}
if p1[0] != 0:
  X12 = [ x for x in range(M[0]) if x % p1[0] == 0]
else:
  X12 = [0 for x in range(M[0])]
if p1[1] != 0:
  Y12 = [ y for y in range(M[1]) if y % p1[1] == 0] 
else:
  Y12 = [ 0 for y in range(M[1]) ]
S12 = {(X12[i],Y12[i]) for i in range(min([len(X12),len(Y12)]))}
S12 = { s(s1,x) for x in S12 }
 
S1 = sumSets(S11,S12)

S21 = {(x,y) for x in range(w2) for y in range(l2)}
if p2[0] != 0:
  X22 = [ x for x in range(M[0]) if x % p2[0] == 0]
else:
  X22 = [ 0 for x in range(M[0]) ]
if p2[1] != 0:
  Y22 = [ y for y in range(M[1]) if y % p2[1] == 0] 
else:
  Y22 = [ 0 for y in range(M[1]) ]
S22 = {(X22[i],Y22[i]) for i in range(min([len(X22),len(Y22)]))}
S22 = { s(s2,x) for x in S22}
 
S2 = sumSets(S21,S22)

f = open("minimal2.txt", 'w')
write(f, S1, 0)
write(f, S2, 0)
write(f, sumSets(S1, S2), 1)


