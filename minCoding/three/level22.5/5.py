a, b = input().split()

arr_map = [[3, 5, 4, 2, 2, 3],
           [1, 3, 3, 3, 4, 2],
           [5, 4, 4, 2, 3, 5]]

price = ['T', 'P', 'G', 'K', 'C']

y = 0
x = int(b)
if a == 'A':
    y = 0
elif a == 'B':
    y = 1
elif a == 'c':
    y = 2

print(price[arr_map[y][x-1]-1])