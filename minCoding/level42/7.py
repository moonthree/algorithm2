price = [15, 20, 44, 22, 55, 16, 45]
price2 = []

product = input()

for i in range(len(product)):
    price2.append(price[ord(product[i]) - 97])

n = int(input())
depth = len(price2)-n
Max = -21e8
used = [0]*len(price2)
def dfs(level, total):
    global Max
    if level == depth:
        if total%10 == 0:
            if Max < total:
                Max = total
        return
    for i in range(len(price2)):
        if used[i] == 1:
            continue
        used[i] = 1
        dfs(level+1, total+price2[i])
        used[i] = 0
dfs(0, 0)
print(Max)
