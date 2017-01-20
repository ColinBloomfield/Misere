import numpy as np
import timeit


def nSum(): # Fourth!
  x = np.array([0,1,2,3,4])
  y = np.array([5,6,7,8,9])
  XX, YY = np.meshgrid(x,y)
  ZZ = XX + YY
  ZZ = np.unique(ZZ)
  return ZZ

def nSum2(): # Third!
  x = np.array([0,1,2,3,4])
  y = np.array([5,6,7,8,9])
  XX, YY = np.atleast_2d(x,y)
  YY = YY.T
  ZZ = XX + YY
  ZZ = np.unique(ZZ)
  return ZZ  

#Not Lim to 2dim?

def nSum3(): # Second!
  #YY, XX = np.mgrid[10:40:10, 1:4]
  #YY, XX = np.ogrid[4:7:1, 1:4]
  XX = np.array([0,1,2,3,4])
  YY = np.array([5,6,7,8,9])
  ZZ = XX + YY # T
  ZZ = np.unique(ZZ)
  return ZZ

def nSum4(): # FIRST!
  #YY, XX = np.ogrid[10:40:10, 1:4]
  #YY, XX = np.ogrid[4:7:1, 1:4]
  XX = np.array([0,1,2,3,4])
  YY = np.array([5,6,7,8,9])
  ZZ = XX + YY
  ZZ = np.unique(ZZ)
  return ZZ

print(nSum())
print(timeit.timeit("nSum()", setup="from __main__ import nSum", number = 100000))

print(nSum2())
print(timeit.timeit("nSum2()", setup="from __main__ import nSum2", number = 100000))

print(nSum3())
print(timeit.timeit("nSum3()", setup="from __main__ import nSum3", number = 100000))

print(nSum4())
print(timeit.timeit("nSum4()", setup="from __main__ import nSum4", number = 100000))


