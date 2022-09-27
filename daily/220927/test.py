import heapq

arr = [4, 87, 4, 24, 8, 23, 3, 7, 4]  # max heap

rev = lambda x: x * -1

heap1 = list(map(rev, arr))

heapq.heapify(heap1)  # heap 의 형태로 저장

for i in range(len(arr)):
    print(-heapq.heappop(heap1))
