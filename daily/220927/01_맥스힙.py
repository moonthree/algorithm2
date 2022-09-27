import heapq
arr = [4, 87, 4, 24, 23, 8, 3, 7, 4]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, -arr[i])
for i in range(len(arr)):
    print(heapq.heappop(heap)*-1, end=' ')

print()
# rev = lambda x:x*-1
# heap = list(map(rev,arr))
# for i in range(len(arr)):
#     print(-heapq.heappop(heap), end=' ')