a, b, c = map(int, input().split())

for _ in range(c):
    for i in range(a, b+1):
        print(i, end=' ')
    print()
# t = []
# for i in range(a, b+1):
#     t.append(i)
#
# for _ in range(c):
#     print(*t)