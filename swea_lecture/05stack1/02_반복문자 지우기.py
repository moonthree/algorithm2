t = int(input())

for tc in range(1, t+1):
    words = list(input())
    flag = 0
    while flag == 0:
        cnt = 0
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                del words[i]
                del words[i]
                break
        for i in range(len(words) - 1):
            if words[i] == words[i + 1]:
                cnt += 1
        if cnt == 0:
            flag = 1
    print(f'#{tc} {len(words)}')