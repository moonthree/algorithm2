# # =============================================

# 정렬 후 출력하기

mst = {'cy': 3000, 'chips': 500, 'coke': 300}

# 가격 오름차순 으로 정렬 후 출력하기
# 출력결과
# coke 300
# chips 500
# cy 3000

ret = sorted(mst.items(), key=lambda x: x[1])

for i in ret:
    print(i[0], i[1])

# 가격 내림차순 으로 정렬 후 출력하기
# 출력결과
# cy 3000
# chips 500
# coke 300
# ret=sorted(mst.items(),key=lambda x:-x[1])
# 또는
ret = sorted(mst.items(), key=lambda x: x[1], reverse=True)
for i in ret:
    print(i[0], i[1])

# 이름 기준으로 오름차순
# 출력결과
# chips 500
# coke 300
# cy 3000


# ret=sorted(mst.items(),key=lambda x:x[0])
# 또는
ret = sorted(mst.items())

for i in ret:
    print(i[0], i[1])

# 이름 기준으로 내림차순
# 출력결과
# cy 3000
# coke 300
# chips 500

ret = sorted(mst.items(), key=lambda x: x[0], reverse=True)
for i in ret:
    print(i[0], i[1])

# =============================================
