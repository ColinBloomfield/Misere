import timeit

def Add(t1 = (1,5,4,9,10,11,101),t2 = (2,3,4,9,10,13,101)):
  temp = []
  for x in range(len(t1)):
    temp.append(t1[x]+t2[x])
  return tuple(temp)

def s(x = (1,5,4,9,10,11,101),y = (2,3,4,9,10,13,101)):
  return tuple([w + z for w,z in zip(x,y)])

print("Add()")   
print(Add())  
print(timeit.timeit("Add()", setup="from __main__ import Add", number = 1000000))

print("s()")
print(s())
print(timeit.timeit("s()", setup="from __main__ import s", number = 1000000))
