words = input()

card_list = []
for i in words:
    card_list.append(i)

bucket = [0]*ord('a')

for i in range(len(card_list)):
    bucket[ord(card_list[i])] += 1

cnt = 0
for i in range(len(bucket)):
    if bucket[i] != 0:
        cnt += 1
print(f'{cnt}개')