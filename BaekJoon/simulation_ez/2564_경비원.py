x, y = map(int, input().split())
n = int(input())

arr = [[0]*x for i in range(y)]
arr_list = []

for i in range(1, n+2):
    a, b = map(int, input().split())
    if a == 1:
        arr_list.append([a, 0, b])
    elif a == 2:
        arr_list.append([a, y, b])
    elif a == 3:
        arr_list.append([a, b, 0])
    elif a == 4:
        arr_list.append([a, b, x])
ssum = 0

for i in range(n):
    temp = []
    if (arr_list[i][0] == 1 and arr_list[n][0] == 2) or (arr_list[i][0] == 2 and arr_list[n][0] == 1) or (arr_list[i][0] == 3 and arr_list[n][0] == 4) or (arr_list[i][0] == 4 and arr_list[n][0] == 3):
        if arr_list[n][0] <= 2:
            temp.append(y+arr_list[i][2]+arr_list[n][2])
            temp.append(y+abs(x-arr_list[i][2])+abs(x-arr_list[n][2]))
        elif arr_list[n][0] > 2:
            temp.append(x + arr_list[i][1] + arr_list[n][1])
            temp.append(x + abs(y - arr_list[i][1]) + abs(y - arr_list[n][1]))
        ssum += min(temp)
    else:
        ssum += abs(arr_list[i][1] - arr_list[n][1]) + abs(arr_list[i][2] - arr_list[n][2])

print(ssum)




# for dy in range(y):
#     for dx in range(x):
#         print(arr[dy][dx], end=' ')
#     print()