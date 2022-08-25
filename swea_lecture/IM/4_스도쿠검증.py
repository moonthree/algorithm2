def sudoku_garo(y):
    bucket = [0]*10
    for x in range(9):
        bucket[arr[y][x]] += 1
    for i in range(1, 10):
        if bucket[i] != 1:
            return 0
    return 1

def sudoku_sero(x):
    bucket = [0]*10
    for y in range(9):
        bucket[arr[y][x]] += 1
    for i in range(1, 10):
        if bucket[i] != 1:
            return 0
    return 1

def sudoku_rect(y, x):
    bucket = [0] * 10
    for dy in range(y, y+3):
        for dx in range(x, x+3):
            bucket[arr[dy][dx]] += 1
    for i in range(1, 10):
        if bucket[i] != 1:
            return 0
    return 1

t = int(input())

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    sudoku = 1
    while sudoku:
        for y in range(9):
            sudoku = sudoku_garo(y)
            if not sudoku:
                break
        if not sudoku:
            break
        for x in range(9):
            sudoku = sudoku_sero(x)
            if not sudoku:
                break
        if not sudoku:
            break
        for y in range(0, 7, 3):
            for x in range(0, 7, 3):
                sudoku = sudoku_rect(y, x)
                if not sudoku:
                    break
            if not sudoku:
                break
        if not sudoku:
            break
        break

    print(f'#{tc} {sudoku}')