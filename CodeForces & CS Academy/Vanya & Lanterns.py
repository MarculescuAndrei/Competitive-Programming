
n, l = [int(x) for x in input().split()]
L = [int (x) for x in input().split()]
L.sort()
aux = 0
for i in range(n-1):
    aux = max(aux, (float)(L[i+1] - L[i]))
aux = aux / 2
aux = max(aux, max( float(L[0]), float((l - L[n-1]))))
print('{0:.10f}'.format(aux))

