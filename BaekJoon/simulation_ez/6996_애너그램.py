t = int(input())

for tc in range(1, t+1):
    a, b = map(str, input().split())
    if sorted(a) == sorted(b):
        print(f'{a} & {b} are anagrams')
    else:
        print(f'{a} & {b} are NOT anagrams')