arr = ['E', 'W', 'A', 'B', 'C']

word = input()

path = []
used = [0]*5

def recur(level):
    if level == 4:
        for i in path:
            print(i, end='')
        print()
        return

    for i in range(len(arr)):
        # if used[i] == 1 or arr[i] == word:
        #     continue
        if used[i] == 0 and arr[i] != word:
            used[i] = 1
            path.append(arr[i])
            recur(level+1)
            path.pop()
            used[i] = 0

recur(0)

