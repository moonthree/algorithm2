t = int(input())

for tc in range(1, t+1):
    arr = list(input().split())
    stack = []
    flag = 0
    for i in arr:
        if '0' <= i <= '9':
            stack.append(int(i))
        elif i == '.':
            break
        elif i == '+':
            if len(stack) < 2:
                flag = 1
                break
            stack.append(stack.pop(-2) + stack.pop(-1))
        elif i == '-':
            if len(stack) < 2:
                flag = 1
                break
            stack.append(stack.pop(-2) - stack.pop(-1))
        elif i == '*':
            if len(stack) < 2:
                flag = 1
                break
            stack.append(stack.pop(-2) * stack.pop(-1))
        elif i == '/':
            if len(stack) < 2:
                flag = 1
                break
            stack.append(stack.pop(-2) // stack.pop(-1))

    if flag or len(stack) > 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack.pop()}')