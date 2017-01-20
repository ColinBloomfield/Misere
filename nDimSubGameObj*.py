#The algorithm works by marking the terminal position P, then labeling each square N from which the terminal position is reachable. Thus the next empty position cannot reach the terminal position, nor can it reach any other P positions since all other previous spots are N positions hence the current spot is a P. The algorithm continues by labeling every position from which the current P position is reachable N, and the Next empty square must again be a P position.


class Pos(char = 'N'):
  v = char


#### MAIN FUNCTION #####################################
def getGame(S,n):
  Nim = ['P' for x in range(n+1)]
  if gameType == 'm':
    for x in range(S[0]):
      Nim[x] = 'N'

  for x in range(len(Nim)):
    if Nim[x] != 'N':
      for y in S:
        if x + y < len(Nim):
          Nim[x+y] = 'N'
  S1 = []
  for x in range(len(Nim)):
    if Nim[x] == 'P':
      S1.append(x)   
  return(S1)


#### Generates Sequence #######################
def getSequence(iter = 5, n = 10, S = [4,9]):
  Sequence = [S]
  for y in range(iter):
    S1 = getGame(S,n)
    Sequence.append(S1)
    S = S1
  return(Sequence)


def printSeq(Sequence, base = 11):
  b = base-1
  for x in Sequence:
    print('\n','\n', 'M',Sequence.index(x))
    print('\n',x)
    z = 0
    for y in range(n):
      if y == x[z]: 
        print('P', end=" ")
        if z < len(x)-1:
          z = z+1      
      else:
        print('N', end=" ")
      if (y % base) == b:
        print() 
  print('\n','\n')
  


#Return number corresponding to period length. Takes optional argument corresponding to upper bound on its length
def getPeriod(Nim, UpperBound = 0):
  pattern = []
  Plen = 0
  for x in range(len(Nim)):
    pattern = Nim[0:x+1]
    for y in range(len(Nim)-len(pattern)):
      if pattern[y % len(pattern)] != Nim[y+len(pattern)]:
        break
      print(y,len(Nim)-len(pattern))
      if y+1 == len(Nim)-len(pattern):
        print(pattern)
        return len(pattern)   
  return len(pattern)

#Seq = getSequence(11,[4,9,13])
#printSeq(Seq)

#Seq = getSequence(7,[4])
#printSeq(Seq, 8)

#Seq = getSequence(6,[4,7])
#printSeq(Seq,11)


gameType = input("Enter the type of subtraction game. 'n' for normal, 'm' for misere: ")
cont = 'y'
while cont != ('n' or 'N'): #continues while cont is not equal to 'n' or 'N'.

  S1 = input("Enter subtraction set as comma separated integers: ")
  S2 = S1.split(",")
  S = [int(e) for e in S2]
 
  n = int(input("Enter integer value of the stack height to calculate. "))
  iter = int(input("Enter a number of iterations: "))

  base = int(input("Enter a base to display in: "))

  Sequence = getSequence(iter,n,S)
  printSeq(Sequence,base)
  
  cont = input("Calculate the P-positions of another game? y/n: ")

