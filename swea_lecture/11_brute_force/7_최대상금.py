def dfs(level):
    global result

    if not level:
        temp = int(''.join(num_arr))

        if result < temp:
            result = temp
        return
    for i in range(len(num_arr)):
        for j in range(i+1, len(num_arr)):
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]
            temp_key = ''.join(num_arr)
            if visited.get((temp_key, level-1), 1):
                visited[(temp_key, level-1)] = 0
                dfs(level-1)
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]

t = int(input())

for tc in range(1, t+1):
    num, n = input().split()
    num_arr = list(num)
    n = int(n)
    visited = {}
    result = 0
    dfs(n)
    print(f'#{tc} {result}')