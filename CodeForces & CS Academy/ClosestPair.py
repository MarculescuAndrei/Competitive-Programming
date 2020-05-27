
import sys


def closest_pair(l1, l2):
    l1.sort()
    l2.sort()

    result = sys.maxsize

    i = 0
    j = 0
    while (i < len(l1) and j < len(l2)):
        if abs(int(l1[i]) - int(l2[j])) < result:
            result = abs(int(l1[i]) - int(l2[j])

        if (int(l1[i]) < int(l2[j])) :
            i += 1
        else:
            j += 1

    return result

n = int(input())
l1 = input().split()
l2 = input().split()

print(closest_pair(l1, l2))