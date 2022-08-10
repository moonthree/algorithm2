image = [[1, 5, 5, 4], [4, 2, 1, 1], [3, 9, 3, 2], [4, 5, 9, 1]]

# 00 01 02
# 10 11 12

directy = [0, 0, 1, 1, 1]
directx = [1, 2, 0, 1, 2]

Max = int(-21e8)
maxy = 0
maxx = 0

def rectSum(y, x):
    sums = 0
    for i in range(5):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy < 0 or dy > 3 or dx < 0 or dx > 3:
            continue
        sums += image[dy][dx]
    return sums

for i in range(4):
    for j in range(4):
        result = rectSum(i, j)
        if result > Max:
            Max = result
            maxy = i
            maxx = j

print(f'({maxy},{maxx})')