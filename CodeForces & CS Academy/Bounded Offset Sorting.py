from heapq import heappop, heappush, heapify

def boundedOffsetSorting(lst, N, M):

    heap = lst[:M + 1]
    heapify(heap)

    
    mainIndex = 0
    for otherElements in range(M + 1, N):
        lst[mainIndex] = heappop(heap)
        heappush(heap, lst[otherElements])
        mainIndex += 1

    while heap:
        lst[mainIndex] = heappop(heap)
        mainIndex += 1

    return lst

N, M = [int(x) for x in input().split()]
lst = [int(x) for x in input().split()]

print(boundedOffsetSorting(lst, N, M))