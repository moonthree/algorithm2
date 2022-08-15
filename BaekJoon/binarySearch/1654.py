# n개의 랜선을 만들어야 한다.
# k개의 랜선을 가지고 있으나 길이가 제각각이다.
# n개의 랜선을 모두 같은 길이로 만들고 싶으므로 k개의 랜선을 잘라서 만들어야 하며, 자른 랜선은 붙일 수 없다.

# 이때 보유한 k개의 랜선으로 n개를 만들 수 있는 랜선의 최대 길이를 구하라.

k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

st = 1
ed = max(arr)
target = n


while True:
    len = (st + ed) // 2
    cnt = 0
    for i in arr:
        cnt += i//len

    if cnt == target:
        print(len)
        break
    elif target < cnt:
        st = len + 1
    elif target > cnt:
        ed = len - 1


#def bs(st, ed, target):