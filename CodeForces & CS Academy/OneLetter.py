n = int(input())
L = []
for i in range(n):
    word = input()
    L.append(min(word))
L.sort()
finalWord = ''
for i in range(len(L)):
    finalWord = finalWord + L[i]

print(finalWord)
