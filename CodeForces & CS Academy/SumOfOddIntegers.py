t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    if k % 2 != n % 2:
        print("NO")
    elif n >= k * k:
        print("YES")
    else:
        print("NO")