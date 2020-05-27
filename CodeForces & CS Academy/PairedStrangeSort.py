
def pair_strange_sort(array):
    array.sort(key = lambda X: (X[0], X[1]))
    return array

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split(' '))))
sorted_array = pair_strange_sort(array)
for element in sorted_array:
    print(str(element[0]) + " " +  str(element[1]))
