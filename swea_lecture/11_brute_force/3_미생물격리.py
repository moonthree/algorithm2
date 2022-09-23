# 1. 이동
# 2. 미생물 위치
# 3. 빨간줄이면 //2, 방향 반대로, 살아남은 미생물 수가 0이 되면 군집이 사라짐
# 4. 만나면 합치고 큰 쪽으로
# 5. 상 : 1 // 하 : 2 // 좌 : 3 // 우 : 4
import copy
t = int(input())
for tc in range(1, t+1):
    cell, time, microbe = map(int, input().split())
    arr = [[0]*cell for _ in range(cell)]
    
    arr_microbe = []
    for i in range(microbe):
        y, x, num, direct = map(int, input().split())
        arr_microbe.append([y, x, num, direct])
    # print(arr_microbe[0][0])
    # print(arr_microbe[0][1])
    for _ in range(time):
        # 1. 이동
        for i in range(len(arr_microbe)):
            y, x, num, direct = arr_microbe[i]
            if direct == 1:
                arr_microbe[i] = [y-1, x, num, direct]
            elif direct == 2:
                arr_microbe[i] = [y+1, x, num, direct]
            elif direct == 3:
                arr_microbe[i] = [y, x-1, num, direct]
            elif direct == 4:
                arr_microbe[i] = [y, x+1, num, direct]
        #print(arr_microbe)
        # 2. 빨간줄이면
        for i in range(len(arr_microbe)):
            y, x, num, direct = arr_microbe[i]
            if y == 0 or x == 0:
                # // 2
                num = int(num / 2)
                # 방향 바꾸기
                if direct == 1 or direct == 3:
                    direct += 1
                elif direct == 2 or direct == 4:
                    direct -= 1
            arr_microbe[i] = [y, x, num, direct]
        # 3. 위치 같으면 합치기
        new_microbe = []
        for i in range(len(arr_microbe)):
            y, x, num, direct = arr_microbe[i]
            new = [y, x, 0, 0]
            if new not in new_microbe:
                new_microbe.append([y, x, 0, 0])
        arr_microbe.sort(key=lambda x: x[2])
        for i in range(len(arr_microbe)):
            y, x, num, direct = arr_microbe[i]
            for j in range(len(new_microbe)):
                ny, nx, nnum, ndirect = new_microbe[j]
                if y == ny and x == nx:
                    new_microbe[j] = [ny, nx, nnum+num, ndirect]
            #temp.sort(key=lambda x: x[2])


        #print(new_microbe)

        # 4. 세력 없으면 삭제
        #print(arr_microbe)
        fin_microbe = []
        for i in range(len(new_microbe)):
            if new_microbe[i][2] != 0:
                fin_microbe.append(new_microbe[i])

        arr_microbe = fin_microbe

    #크기 출력
    total = 0
    for j in arr_microbe:
        total += j[2]
    print(f'#{tc} {total}')