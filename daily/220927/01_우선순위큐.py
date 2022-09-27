import heapq # 우선순위 큐를 사용하기 위한 모듈

arr = []
heapq.heappush(arr, 4)      # 최소합 디폴트 -> 값이 가장 작은것ㅇ 우선순위가 높음
heapq.heappush(arr, 15)
heapq.heappush(arr, 2)
heapq.heappush(arr, 7)
heapq.heappush(arr, 5)
heapq.heappush(arr, 9)

for i in range(len(arr)):
    print(heapq.heappop(arr), end=' ')