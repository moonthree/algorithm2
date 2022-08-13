words = input()

for i in range(len(words)-1, -1, -1):
    for j in words[i:]:
        print(j, end='')
    print()