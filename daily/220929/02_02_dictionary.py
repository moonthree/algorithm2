# 연습문제

# 딕셔너리 key value 출력하기
burger = {
    'mst': {'cy': 3000, 'chips': 500},
    'mc': {'bm': 5000, 'chips': 700}
}

# 출력결과 1
# mst bm

for i in burger:
    print(i, end=' ')
print()

for i in burger.keys():
    print(i, end=' ')
print()

key = (burger.keys())
print(*key)
print()

# 출력결과 2
# {'cy':3000,'chips':500}
# {'bm':5000,'chips':700}
for i in burger.values():
    print(i, end=' ')
print()

# 출력결과 3
# 3000
# 500
# 5000
# 700
print()
for i in burger.values():
    for j in i.values():
        print(j)
print()

# 출력결과 4
# mst {'cy': 3000, 'chips': 500}
# mc {'bm': 5000, 'chips': 700}

for i, j in burger.items():
    print(i, j)
print()

# 출력결과 5
# cy 3000
# chips 500
# bm 5000
# chips 700
for i in burger.values():
    for y, x in i.items():
        print(y, x)

# =============================================
