town = [['C', 'D', 'A'], ['B', 'M', 'Z'], ['Q', 'P', 'O']]

blacklist = input()

black = []
for i in blacklist:
    black.append(i)

cnt = 0
for i in black:
    for j in range(len(town)):
        for k in range(len(town[j])):
            if i == town[j][k]:
                cnt += 1
                
print(f'{cnt}명')