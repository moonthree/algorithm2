fastfood = [
    {'name': 'mst', 'burger': 3000, 'chips': 500, 'tasty': 'C'},
    {'name': 'mc', 'burger': 5000, 'chips': 700, 'tasty': 'A'},
    {'name': 'bk', 'burger': 7000, 'chips': 300, 'tasty': 'A'},
]
# 맛 오름차순 and 버거가격 내림차순으로 정렬해서 출력하기

good = sorted(fastfood, key=lambda x: -x['burger'])
print(good)
ret = sorted(good, key=lambda x: x['tasty'])

for i in ret:
    for y, x in i.items():
        print(y, x)
    print()