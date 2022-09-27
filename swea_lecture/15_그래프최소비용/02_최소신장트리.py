import heapq

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]