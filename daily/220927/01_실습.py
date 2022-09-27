import heapq

arr = [4, 87, 4, 24, 23, 8, 3, 7, 4]
arr2 = []
for i in arr:
    heapq.heappush(arr2, i)
print(arr2)

for i in range(len(arr)):
    print(heapq.heappop(arr2), end=' ')

print()

arr3 = [4, 87, 4, 24, 23, 8, 3, 7, 4]
heapq.heapify(arr3)
for i in range(len(arr3)):
    print(heapq.heappop(arr3), end=' ')