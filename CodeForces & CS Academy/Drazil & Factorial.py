n = int(input())
a = input()

NrList = [0] * 9

for i in a:

    if int(i) == 2:
        NrList[2] += 1
    elif int(i) == 3:
        NrList[3] += 1
    elif int(i) == 4:
        NrList[2] += 2
        NrList[3] += 1
    elif int(i) == 5:
        NrList[5] += 1
    elif int(i) == 6:
        NrList[3] += 1
        NrList[5] += 1
    elif int(i) == 7:
        NrList[7] += 1
    elif int(i) == 8:
        NrList[2] += 3
        NrList[7] += 1
    elif int(i) == 9:
        NrList[2] += 1
        NrList[3] += 2
        NrList[7] += 1

X = ''
for i in range(len(NrList)):
    if NrList[i] != 0:
        X += str(i) * NrList[i]

print(X[::-1])