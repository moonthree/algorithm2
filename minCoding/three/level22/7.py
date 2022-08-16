word = input()
arr = ['A', 'B', 'C', 'D']
path = ['']*10
total = 0
def tree(level):
    global total
    if level == 3:
        cnt = 0
        total += 1
        for i in range(level):
            if path[i] == word[i]:
                cnt += 1
                if cnt == 3:
                    print(f'{total}번째')
        return
    for i in range(len(arr)):
        path[level] = arr[i]
        tree(level+1)
tree(0)