# 다익스트라
# 시작점에서 도착점까지의 최소 비용, dfs보다 효율적
# 가중치가 음수면 못 씀
# 1. 인접행렬로 풀기
# 2. 인집리스트로 풀기

# 인접행렬
# used = 경유지 check
# result = 시작점 -> 도착점 비용

inf = 21e8

arr = [
    [0, 3, inf, 9, 5],
    [inf, 0, 7, inf, 1],
    [inf, inf, 0, 1, inf],
    [inf, inf, inf, 0, inf],
    [inf, inf, 1, inf, 0]
]

used = [0]*5
result = [0, 3, inf, 9, 5]
used[0] = 1 # 시작점 'A'라고 가정함

def select_ky():
    MIN = 21e8
    MINidx = 0
    for i in range(5):
        if used[i] == 0 and result[i] < MIN:
            MIN = result[i]
            MINidx = i;
    return MINidx

def dijkstra():
    for _ in range(4):
        via = select_ky()       # 경유지 선택
        used[via] = 1
        for j in range(5):
            baro = result[j]    # 바로 
            ky = result[via] + arr[via][j] # 경유지 거쳐서
            if baro > ky:
                result[j] = ky
dijkstra()
print(*result)