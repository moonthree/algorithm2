import heapq

n = int(input())

heap = []
for i in range(n):
    a = int(input())
    heapq.heappush(heap, a)

print(heap)
total = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    total += a+b

print(total)