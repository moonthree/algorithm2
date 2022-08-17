import sys
sys.stdin = open("6_input.txt", "r")

for _ in range(1):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]

    for y in range(1):
        for x in range(100):
            temp_r = []
            temp_l = []
            temp_r.append(arr[y][0:(50-x)])
            temp_l.append(arr[y][100-x:0])
            print(temp_r, end=' ')
            print(len(temp_r[0]))
            print(temp_l, end=' ')
            print(len(temp_l[0]))
            print()



