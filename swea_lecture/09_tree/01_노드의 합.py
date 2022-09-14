t = int(input())

for tc in range(1, t+1):
    # n : 노드의 개수
    # m : 리프 노도의 개수 // 리프 노드 : 자식이 없는 노드
    # l : 출력할 노드 번호
    n, m, l = map(int, input().split())

    tree = [0] * (n+1)
    # m개에 걸쳐 리프노드 번호와 1000이하의 자연수가 주어지니까 tree배열에 넣음
    for i in range(m):
        idx, val = map(int, input().split())
        tree[idx] = val

    def post(now):
        if now > n:
            return
        post(now * 2)
        post(now * 2 + 1)
        if now > 1:
            tree[now//2] += tree[now]
    post(1)
    print(tree)
    print(f'#{tc} {tree[l]}')

# ex)
# 5 3 2
# 4 1
# 5 2
# 3 3

# tree
# idx = 0 1 2 3 4 5
# val = 0 0 0 3 1 2

# post(1)
# if 1 > 5
# post(2)
# post(3)