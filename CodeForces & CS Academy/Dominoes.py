n, k = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

i = j = 0
Max = P = 0
while i < len(L) and j < len(L):
    if L[i] - L[j] - i + j < k:
        if i - j + 1 > P:
            P = i - j + 1
            Max = i - j + 1 + k
        i += 1
    else:
        j += 1

print(Max)