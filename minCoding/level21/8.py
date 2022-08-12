y = 5
x = 5

n = int(input())

for _ in range(n):
    move = input()

    if move == 'up':
        y -= 1
    elif move == 'down':
        y += 1
    elif move == 'left':
        x -= 1
    elif move == 'right':
        x += 1
    elif move == 'click':
        print(f'{y},{x}')
