n, d = input().split()
L = []
for i in range(int(n)+1):
    if i == 0:
        L.append([0 ,0])
    else:
        m, f = input().split()
        L.append([int(m), int(f)])

L.sort(key = lambda X: X[0])

Sum = 0
for i in range(1, int(n)+1):
    Sum += L[i][1]
    L[i][1] = Sum

j = dif = 0
answer = 0
for i in range(1, int(n)+1):

    if L[i][0] - L[j][0] < int(d):
        dif = L[i][0] - L[j][0]
    else:
        dif = L[i][0] - L[j][0]

        while dif >= int(d):
            j += 1
            dif = L[i][0] - L[j][0]
    if j == 0:
        answer = max(answer, L[i][1] - L[j][1])
    else:
        answer = max(answer, L[i][1] - L[j-1][1])


print(answer)