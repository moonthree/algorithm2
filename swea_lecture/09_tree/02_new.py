'''
1
5 1
2 1 2 5 1 6 5 3 6 4
'''

t = int(input())

for tc in range(1, t+1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접리스트 만들기
    tree = [[0] * 2 for _ in range(e + 2)]
    # L R
    #[[0 ,0], 부모
    # [0, 0], # 1
    # [0, 0], # 2
    # [0, 0], # 3
    # [0, 0], # 4
    # [0, 0], # 5
    # [0, 0]] # 6

    for i in range(len(arr)//2):
        parent, child = arr[i*2], arr[i*2+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    # L R
    #[[0 ,0], 부모
    # [6, 0], # 1
    # [1, 5], # 2
    # [0, 0], # 3
    # [0, 0], # 4
    # [3, 0], # 5
    # [4, 0]] # 6

    cnt = 0
    def preorder(now):
        global cnt
        if now:
            cnt += 1
            preorder(tree[now][0])
            preorder(tree[now][1])

    preorder(n)
    print(f'#{tc} {cnt}')