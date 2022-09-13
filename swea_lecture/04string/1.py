tc = int(input())

for test in range(1, tc+1):
    a, b = input().split()
    print(f'#{test} {len(a.replace(b, "*"))}')