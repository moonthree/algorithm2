arr = [[0]*4 for _ in range(3)]

loc_y = []
loc_x = []
flag = 0

for _ in range(3):
    a, b = map(int, input().split())
    loc_y.append(a)
    loc_x.append(b)

loc_y.sort()
loc_x.sort()

for i in range(len(loc_y)-1):
    if loc_y[i] == loc_y[i+1]:
        flag = 1
for i in range(len(loc_x)-1):
    if loc_x[i] == loc_x[i+1]:
        flag = 1

if flag:
    print('위험')
else:
    print('안전')