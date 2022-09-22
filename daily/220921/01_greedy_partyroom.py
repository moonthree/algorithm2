# 6
# 10 11
# 14 15
# 11 13
# 10 12
# 13 15
# 13 14

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

sort1 = sorted(arr, key=lambda x: x[1])
#print(sort1)
cnt = 1
room = [sort1[0]]

for i in range(1, n):
    if sort1[i][0] >= room[0][1]:
        cnt += 1
        #print(room)
        room.pop()
        room.append(sort1[i])


print(cnt)