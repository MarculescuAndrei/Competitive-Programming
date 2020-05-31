n = int(input())
dict = {}

for i in range(n):
    w = input()
    w = ''.join(sorted(w))
    if (w in dict):
        dict[w] += 1
    else:
        dict[w] = 1
max = -1
for i in dict:
    if (dict[i] > max):
        max = dict[i]
print(max)