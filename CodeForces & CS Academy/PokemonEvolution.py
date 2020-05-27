L = input().split()
V = (int(L[0]) * int(L[3]) + int(L[1])) // (int(L[2]) + int(L[3]))

if int(V) > int(L[0]):
    print(L[0])
else:
    print(V)