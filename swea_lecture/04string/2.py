n = int(input())

for tc in range(1, n+1):
    str1 = list(set(input()))
    str2 = input()

    long = int(-21e8)
    for i in str1:
        if str2.count(i) > long:
            long = str2.count(i)

    print(f'#{tc} {long}')
