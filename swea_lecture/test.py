arr = [4,4,5,7,8,10,20,22,23,24]
target = int(input())
st, ed = 0, 9
while 1:
    if st > ed:
        print('x')
        break
    md = (st+ed) // 2
    if arr[md] == target:
        print("O")
        break
    elif arr[md] > target:
        ed = md - 1
    elif arr[md] < target:
        st = md + 1