def up_down(n, stair):
    if n == 5:
        if stair > 0:
            print(f'{stair}')
        elif stair <= 0:
            print(f'B{abs(stair-1)}')
        return
    direct = input()
    if direct == 'up':
        up_down(n+1, stair+1)
    elif direct == 'down':
        up_down(n+1, stair-1)

up_down(0, 1)
