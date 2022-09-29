# 파이썬에서 해쉬를 딕셔너리로 구현 많이 한다.
dict1 = {}
dict2 = dict()
burger = {'cy': 3000, 'wp': 5000}
# 싸이버거 가격만 출력하기
print(burger['cy'])

burger = {
    'mst': {'cy': 3000, 'chips': 500},
    'mc': {'bm': 5000, 'chips': 700}
}
# 맥도날드의 빅맥 가격만 출력하기
print(burger['mc']['bm'])

# 맘스터치의 칩스 가격 1000원 인상하고 출력하기
burger['mst']['chips'] += 1000
print(burger['mst']['chips'])

# 없는 거 출력하려해서 key에러 발생
#print(burger['mst']['coke'])

# coke가 있으면 출력 없으면 없음 출력
print(burger['mst'].get('coke','없음'))

# 딕셔너리 mst 삭제
# del burger['mst']
# burger.pop('mst')

