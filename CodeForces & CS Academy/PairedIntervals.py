def contained_intervals(intervals):
    L = []
    for i in intervals:
        L.append((i['x'], i['y']))

    L.sort(key=lambda X: (X[0], -X[1]))

    maxdr = L[0][1]
    contained = 0
    for i in range(len(L)):
        if i + 1 < len(L) and L[i + 1] == L[i]:
            contained += 1
        elif i > 0 and maxdr >= L[i][1]:
            contained += 1
        maxdr = max(maxdr, L[i][1])

    return contained

###

n = int(input())
intervals = []
for i in range(n):
    x, y = map(int, input().split(' '))
    intervals.append({
        "x": x,
        "y": y
    })

answer = contained_intervals(intervals)
print(answer)