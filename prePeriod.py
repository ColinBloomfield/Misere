A = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
B = [1, 3, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]


def sumseq(s1, s2):
    s3 = [ x + y for x in s1 for y in s2]
    return sorted(list(set(s3)))

def printseq(s):
    y = 0
    for x in s:
        while y < x:
            print(0, end=" ")
            y += 1
        print(1, end=" ")
        y += 1


# A = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
# B = [1, 3, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
#
# C = sumseq(A, B)
#
# print()
# print(A)
# printseq(A)
# print()
# print()
# printseq(B)
# print()
# print()
# printseq(C)

# print()
# A1 = [1, 3, 5, 10, 11, 15, 16, 20, 21, 25, 26]
# printseq(A1)
# print('\n'+'\n')
# B1 = [0, 2, 4, 6, 8, 13, 18, 23, 28, 33, 38]
# printseq(B1)
# print('\n'+'\n')
#
# C1 = sumseq(A1,B1)
# printseq(C1)
# print('\n'+'\n')

# print()
# A1 = [0, 1, 2, 10, 11, 15, 16, 20, 21, 25, 26]
# printseq(A1)
# print('\n'+'\n')
# B1 = [0, 2, 4, 6, 8, 13, 18, 23, 28, 33, 38]
# printseq(B1)
# print('\n'+'\n')
#
# C1 = sumseq(A1,B1)
# printseq(C1)
# print('\n'+'\n')

print()
A1 = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61]
printseq(A1)
print('\n'+'\n')
B1 = [0, 7, 14, 21, 28, 35, 42, 49, 56, ]
printseq(B1)
print('\n'+'\n')

C1 = sumseq(A1,B1)
printseq(C1)
print('\n'+'\n')

print(A1, '\n')
print(B1, '\n')
print(C1, '\n')