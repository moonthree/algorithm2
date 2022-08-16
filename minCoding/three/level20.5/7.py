words = input()

for i in range(len(words)):
    for j in range(i+1):
        print(words[j], end='')
    print()