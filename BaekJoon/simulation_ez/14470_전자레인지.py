# a도의 고기를
# 전자레인지로 b도까지 데운다
# 고기가 0도보다 낮으면 얼어있고, 0도보다 높으면 얼어 있지 않다.
# 온다가 0도일때 고기는 얼어 있을수도, 얼어있지 않을 수도 있다.
# 얼음 + 0도미만 -> 온도가 c초에 1도씩 오른다.
# 얼어 있고 0도 -> 해동에 d초가 걸린다.
# 얼어 있지 않을 때 -> 온도가 e초에 1도씩 오른다.

meat_temp = int(input())
target_temp = int(input())

ice_meat = int(input())
melt_meat = int(input())
hot_meat = int(input())

cnt = 0
if meat_temp < 0:
    while meat_temp != 0:
        meat_temp += 1
        cnt += ice_meat
    if meat_temp == 0:
        cnt += melt_meat
    while meat_temp != target_temp:
        meat_temp += 1
        cnt += hot_meat
else:
    while meat_temp != target_temp:
        meat_temp += 1
        cnt += hot_meat

print(cnt)