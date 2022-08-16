words = input()
words_list = []
for i in words:
    words_list.append(i)

bucket = [0]*(ord('z')+1)

for i in range(len(words_list)):
    bucket[ord(words_list[i])] += 1

max_cnt = 0
max_idx = 0
for i in range(len(bucket)):
    if bucket[i] > max_cnt:
        max_cnt = bucket[i]
        max_idx = i

print(chr(max_idx))