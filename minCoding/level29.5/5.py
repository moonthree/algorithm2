arr = [list(map(int, input().split())) for _ in range(4)]

first_flag = True
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] == 1:
            print(f'({y},{x})')
            first_flag = False
            break
    if first_flag == False:
        break

second_flag = True
for y in range(len(arr)-1, -1 , -1):
    for x in range(len(arr[y]) - 1, -1, -1):
        if arr[y][x] == 1:
            print(f'({y},{x})')
            second_flag = False
            break
    if second_flag == False:
        break