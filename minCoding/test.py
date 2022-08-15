lst = [5,5]
n= int(input())

for _ in range(n):
    s= input()
    if s == 'up':
        lst[0] += 1
    elif s == 'down':
        lst[0] -= 1
    elif s == 'left':
        lst[1] -= 1
    elif s == 'right':
        lst[1] += 1
    elif s == 'click':
        print(lst)