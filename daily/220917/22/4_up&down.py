
ret = 1
def recur(level, stair):
    global ret
    order = input()
    if level == 4:
        ret = stair
        return stair

    if order == 'up':
        recur(level + 1, stair + 1)
    else:
        recur(level + 1, stair - 1)


recur(0, 0)

if ret > 0:
    print(f'{ret}')
else:
    print(f'B{abs(ret-1)}')