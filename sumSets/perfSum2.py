import timeit

C = {0,1,2,3,4}
D = {5,6,7,8,9}

c = [0,1,2,3,4]
d = [5,6,7,8,9]

def Sumset1(A = {0,1,2,3,4},B = {5,6,7,8,9}):
  C = { x + y for x in A for y in B }
  return C

def Sumset2(A = [0,1,2,3,4],B = [5,6,7,8,9]):
  C = []
  for x in A:
    for y in B:
      C.append(x+y)
  C = list(set(C)) 
  return C

def Sumset3(A = [0,1,2,3,4],B = [5,6,7,8,9]):
  C = [ x + y for x in A for y in B ]
  C = list(set(C))
  return C 
  
  
 
print(Sumset1())     
print(timeit.timeit("Sumset1()", setup="from __main__ import Sumset1", number = 1000000))

print(Sumset2())
print(timeit.timeit("Sumset2()", setup="from __main__ import Sumset2", number = 1000000))

print(Sumset3())
print(timeit.timeit("Sumset3()", setup="from __main__ import Sumset3", number = 1000000))

