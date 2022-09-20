from collections import deque

n = int(input())

arr = [[0]*n for _ in range(n)]
acc = [0]*n
time = [0]*n
used = [0]*n
q = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    if len(temp) < 3:
        time[i] = temp[0]
    else:
        time[i] = temp[0]
        acc[i] = temp[1]
        for j in range(2, len(temp)):
            arr[temp[j]][i] = 1

for i in range(n):
    if acc[i] == 0:
        used[i] = 1
        q.append(i)

for i in arr:
    print(i)
print()
print('acc:', acc)
print(time)
print(used)
# print(acc)
# print(used)
#print(q)
while q:
    now = q.popleft()
    print(time[now])
    for i in range(n):
        if arr[now][i] == 1 and used[i] == 0:
            if acc[i] == 1:
                used[i] = 1
                acc[i] -= 1
                q.append(i)
            else:
                acc[i] -= 1
