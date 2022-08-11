t = int(input())

for i in range(t):
    n = int(input())
    num_list = list(map(int, input().split()))

    MAX = int(-21e8)
    MIN = int(21e8)
    for j in range(n):
        if num_list[j] > MAX:
            MAX = num_list[j]

    for j in range(n):
        if num_list[j] < MIN:
            MIN = num_list[j]

    print(f'#{i+1} {MAX-MIN}')