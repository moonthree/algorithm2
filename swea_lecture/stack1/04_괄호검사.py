t = int(input())

for tc in range(1, t+1):
    words = input()
    stack = []
    flag = 0
    for i in words:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                flag = 1
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                flag = 1
                break
        elif i == '}':
            if len(stack) == 0:
                flag = 1
                break
            if stack[-1] == '{':
                stack.pop()
            else:
                flag = 1
                break

    if flag:
        print(f'#{tc} 0')
    else:
        if len(stack):
            print(f'#{tc} 0')
        else:
            print(f'#{tc} 1')