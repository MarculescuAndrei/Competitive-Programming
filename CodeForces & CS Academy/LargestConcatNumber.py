from functools import cmp_to_key
def cmp(x, y):
    return -1 if x<y else ( 0 if x==y else 1)
def maxnum(x):
    return ''.join(sorted((str(n) for n in x),
                              key=cmp_to_key(lambda x,y:cmp(y+x, x+y))))

n = int(input())
L=[]
for i in range(n):
    x = input()
    L.append(int(x))
OK = 1
for i in L:
    if i != 0:
        OK = 0
        break
if OK == 1:
    print(0)
else:
    print(maxnum(L))