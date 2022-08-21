words = [input() for _ in range(4)]

for i in range(len(words)-1):
    for j in range(i+1, len(words)):
        if len(words[i]) > len(words[j]):
            words[i], words[j] = words[j], words[i]

for i in words:
    print(i)